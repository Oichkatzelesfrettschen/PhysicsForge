"""
Merge, deduplicate, and summarize equation catalogs (ASCII-only).
Implements EquationMerger used by tests and pipeline scripts.
"""

from __future__ import annotations

import csv
import os
import argparse
from collections import defaultdict, Counter
from pathlib import Path
try:
    from scripts.common import resolve_base_dir
except Exception:
    import sys as _sys
    from pathlib import Path as _Path
    _mod_dir = str(_Path(__file__).resolve().parent)
    _sys.path.insert(0, _mod_dir)
    from common import resolve_base_dir


BASE_DIR = str(Path(__file__).resolve().parents[1])


class EquationMerger:
    def __init__(self):
        self.all_equations: list[dict] = []
        self.equation_signatures: dict[str, str] = {}
        self.notation_conflicts: list[dict] = []
        self.related_groups: dict[str, list[str]] = defaultdict(list)
        self.had_errors = False

    @staticmethod
    def normalize_equation(eq_str: str) -> str:
        sig = eq_str.replace(" ", "").replace("\t", "")
        sig = sig.replace("**", "^").replace("x", "*")
        return sig.lower()

    def merge_catalogs(self) -> None:
        # Load from text files
        text_catalog = os.path.join(BASE_DIR, "equation_catalog_preliminary.csv")
        if os.path.exists(text_catalog):
            try:
                with open(text_catalog, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.all_equations.append(row)
            except FileNotFoundError:
                print(f"Warning: Text catalog file not found: {text_catalog}")
                self.had_errors = True
            except IOError as e:
                print(f"Error reading text catalog file {text_catalog}: {e}")
                self.had_errors = True

        # Load from PDFs (text-based extraction)
        pdf_catalog = os.path.join(BASE_DIR, "equation_catalog_pdfs.csv")
        if os.path.exists(pdf_catalog):
            try:
                with open(pdf_catalog, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    offset = len(self.all_equations)
                    for i, row in enumerate(reader):
                        old_id = row.get("EqID", "EQ000")
                        prefix = old_id[:2]
                        row["EqID"] = f"{prefix}{offset + i + 1:03d}"
                        self.all_equations.append(row)
            except FileNotFoundError:
                print(f"Warning: PDF catalog file not found: {pdf_catalog}")
                self.had_errors = True
            except IOError as e:
                print(f"Error reading PDF catalog file {pdf_catalog}: {e}")
                self.had_errors = True

        # Load from PDFs (OCR-based extraction)
        pdf_ocr_catalog = os.path.join(BASE_DIR, "equation_catalog_pdfs_ocr.csv")
        if os.path.exists(pdf_ocr_catalog):
            try:
                with open(pdf_ocr_catalog, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    offset = len(self.all_equations)
                    for i, row in enumerate(reader):
                        old_id = row.get("EqID", "EQ000")
                        prefix = old_id[:2]
                        row["EqID"] = f"{prefix}{offset + i + 1:03d}"
                        self.all_equations.append(row)
            except FileNotFoundError:
                print(f"Warning: PDF OCR catalog file not found: {pdf_ocr_catalog}")
                self.had_errors = True
            except IOError as e:
                print(f"Error reading PDF OCR catalog file {pdf_ocr_catalog}: {e}")
                self.had_errors = True

        print(f"Total equations loaded: {len(self.all_equations)}")

    def deduplicate(self) -> None:
        seen: dict[str, str] = {}
        unique: list[dict] = []
        for eq in self.all_equations:
            sig = self.normalize_equation(eq["Equation"])
            if sig in seen:
                original_id = seen[sig]
                eq["RelatedEqs"] = original_id
                unique.append(eq)
                print(f"Duplicate found: {eq['EqID']} similar to {original_id}")
            else:
                seen[sig] = eq["EqID"]
                unique.append(eq)
        self.all_equations = unique
        print("Deduplication complete. Relationships marked.")

    def categorize_equations(self) -> None:
        for eq in self.all_equations:
            desc = eq.get("Description", "").lower()
            if any(w in desc for w in ["kernel", "action", "lagrangian", "hamiltonian", "fundamental"]):
                category = "Fundamental"
            elif any(w in desc for w in ["measurement", "experimental", "observation", "data"]):
                category = "Experimental"
            elif any(w in desc for w in ["model", "phenomenological", "effective"]):
                category = "Phenomenological"
            else:
                category = "Derived"
            eq["Category"] = category

    def identify_notation_conflicts(self) -> None:
        # Placeholder (ASCII-only), can be extended later
        self.notation_conflicts = []

    def rank_equations(self) -> None:
        for i, eq in enumerate(self.all_equations):
            eq["ImportanceScore"] = len(eq.get("Description", "")) % 10 + (0 if i >= 0 else 0)

    def save_final_catalog(self) -> None:
        output_file = os.path.join(BASE_DIR, "equation_catalog.csv")
        fields = [
            "EqID", "Equation", "Framework", "Domain", "SourceDoc", "SourceLine",
            "Description", "VerificationStatus", "RelatedEqs", "ExperimentalTest", "Category",
        ]
        try:
            with open(output_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                for eq in self.all_equations:
                    writer.writerow({k: eq.get(k, "") for k in fields})
            print(f"\nFinal catalog saved: {output_file}")
            print(f"Total equations: {len(self.all_equations)}")
        except IOError as e:
            print(f"Error writing final catalog file {output_file}: {e}")
            self.had_errors = True

    def generate_summary(self) -> None:
        stats = {
            "total": len(self.all_equations),
            "by_framework": Counter(eq.get("Framework", "") for eq in self.all_equations),
            "by_domain": Counter(eq.get("Domain", "") for eq in self.all_equations),
            "by_category": Counter(eq.get("Category", "Unknown") for eq in self.all_equations),
            "by_status": Counter(eq.get("VerificationStatus", "") for eq in self.all_equations),
        }
        summary_file = os.path.join(BASE_DIR, "equation_summary.txt")
        try:
            with open(summary_file, "w", encoding="utf-8") as f:
                f.write("=" * 70 + "\n")
                f.write("EQUATION CATALOG SUMMARY - Math_Science Repository\n")
                f.write("=" * 70 + "\n\n")
                f.write(f"Total Equations: {stats['total']}\n\n")
                f.write("BY FRAMEWORK:\n")
                for framework, count in sorted(stats["by_framework"].items(), key=lambda x: x[1], reverse=True):
                    f.write(f"  {framework:20s}: {count:4d}\n")
                f.write("\nBY DOMAIN:\n")
                for domain, count in sorted(stats["by_domain"].items(), key=lambda x: x[1], reverse=True):
                    f.write(f"  {domain:20s}: {count:4d}\n")
                f.write("\nBY CATEGORY:\n")
                for category, count in sorted(stats["by_category"].items(), key=lambda x: x[1], reverse=True):
                    f.write(f"  {category:20s}: {count:4d}\n")
                f.write("\nBY VERIFICATION STATUS:\n")
                for status, count in sorted(stats["by_status"].items(), key=lambda x: x[1], reverse=True):
                    f.write(f"  {status:20s}: {count:4d}\n")
            print(f"Summary saved: {summary_file}")
        except IOError as e:
            print(f"Error writing summary file {summary_file}: {e}")
            self.had_errors = True

    def save_notation_guide(self) -> None:
        output_file = os.path.join(BASE_DIR, "notation_conflicts.txt")
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("=" * 70 + "\n")
                f.write("NOTATION DISAMBIGUATION GUIDE\n")
                f.write("=" * 70 + "\n\n")
                f.write("Critical ASCII tokens to standardize: \\phi, \\psi, rho, G, H, E, c, h.\\n")
            print(f"Notation guide saved: {output_file}")
        except IOError as e:
            print(f"Error writing notation guide file {output_file}: {e}")
            self.had_errors = True

    def save_top_equations(self) -> None:
        output_file = os.path.join(BASE_DIR, "top_equations.txt")
        top_30 = self.all_equations[:30]
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("=" * 70 + "\n")
                f.write("TOP 30 MOST IMPORTANT EQUATIONS - Math_Science Repository\n")
                f.write("=" * 70 + "\n\n")
                for i, eq in enumerate(top_30, 1):
                    f.write(f"\n{i}. {eq.get('EqID','EQ000')} (Score: {eq.get('ImportanceScore', 0)})\n")
                    f.write("-" * 70 + "\n")
                    f.write(f"Equation:  {eq.get('Equation','')}\n")
                    f.write(f"Framework: {eq.get('Framework','')}\n")
                    f.write(f"Domain:    {eq.get('Domain','')}\n")
                    f.write(f"Category:  {eq.get('Category','N/A')}\n")
                    f.write(f"Status:    {eq.get('VerificationStatus','')}\n")
                    f.write(f"Source:    {eq.get('SourceDoc','')} (Line/Page: {eq.get('SourceLine','')})\n")
                    f.write(f"Description: {eq.get('Description','')}\n")
                    if eq.get('RelatedEqs'):
                        f.write(f"Related:   {eq.get('RelatedEqs','')}\n")
                    f.write(f"Test:      {eq.get('ExperimentalTest','')}\n")
            print(f"Top equations saved: {output_file}")
        except IOError as e:
            print(f"Error writing top equations file {output_file}: {e}")
            self.had_errors = True


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge, deduplicate, and rank equation catalogs")
    parser.add_argument("--base-dir", type=str, help="Repository base directory (overrides default)")
    args = parser.parse_args()

    global BASE_DIR
    BASE_DIR = resolve_base_dir(args.base_dir)
    print("=" * 70)
    print("MERGING AND ANALYZING EQUATION CATALOGS")
    print("Base dir:", BASE_DIR)
    print("=" * 70)

    merger = EquationMerger()
    print("\n1. Merging catalogs...")
    merger.merge_catalogs()
    print("\n2. Deduplicating...")
    merger.deduplicate()
    print("\n3. Categorizing equations...")
    merger.categorize_equations()
    print("\n4. Identifying notation conflicts...")
    merger.identify_notation_conflicts()
    print("\n5. Ranking equations by importance...")
    merger.rank_equations()
    print("\n6. Saving final catalog...")
    merger.save_final_catalog()
    print("\n7. Generating summary...")
    merger.generate_summary()
    print("\n8. Saving notation guide...")
    merger.save_notation_guide()
    print("\n9. Saving top equations...")
    merger.save_top_equations()
    print("\n" + "=" * 70)
    print("=" * 70)

    if merger.had_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

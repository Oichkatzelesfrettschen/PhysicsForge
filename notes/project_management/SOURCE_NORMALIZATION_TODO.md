# Source Normalisation TODO

This checklist tracks outstanding cleanup items required before migrating the
Markdown manuscripts into the LaTeX synthesis project.

## High-Priority

- **Alpha001.06_DRAFT_Aether_Framework.md**
  - ~~Deduplicate the embedded copies of the Genesis narrative (lines 155, 23173,
    23962, 46148, 69619, 95538, 143686).~~ (resolved)
  - Isolate Genesis-specific content into its own source file prior to LaTeX
    migration.
- **MATHEMATICS_REFERENCE.md**
  - Replace missing references (Superframework_Expansion, etc.) with available
    bibliographic entries or annotate as unavailable.
  - Define the confidence scoring methodology and add footnotes for each entry.
- **top_equations.md / equation_summary.md**
  - Regenerate from a real `equation_catalog.csv` dataset; current numbers are
    unverifiable.
- **Maximal_Extraction_SET1_SET2.md**
  - Tag speculative claims (fractal Cayley-Dickson extensions) with citations
    or relocate to a speculative appendix.
- **math5GenesisFrameworkUnveiled.md**
  - Extract remaining Phase 3+ content into narrative modules and audit claims
    (consciousness resonance, multiverse tuning forks) for placement or removal.

- **Genesis Phase 5-8 modules**
  - Reconcile summaries with cited equations and ensure speculative content is clearly annotated in the LaTeX narrative.
- **Experimental chapters (Ch22--Ch23)**
  - Add citations, numeric targets, and instrument tolerances once source documents are validated.
- **Applications chapters (Ch28--Ch30)**
  - Replace outline bullets with quantitative analyses and vetted references before publication.
## Medium-Priority

- **Alpha003.02_Aether_Chrystalline_Fluidic_Framework.md**
  - Resolve dimensional inconsistencies in `ρ_total = ρ_ZPE + gφ(t)` and
    clarify coupling constants.
  - Correct the Casimir force sign and document parameter ranges.
- **Aether-Crystalline-Framework.md**
  - Recast mixed-unit expressions (e.g., `F(t, κ)`) into dimensionally
    consistent equations or provide derivations.
- **math5GenesisFrameworkUnveiled.md / math4GenesisFramework.md**
  - Convert inline TeX fragments to fenced math blocks for LaTeX import.
  - Annotate speculative technology forecasts (e.g., multiverse tuning forks).
- **draft reply to pais.md**
  - Introduce explicit coupling constants for `E_ZPE` integral and
    `L_int = g φ sin(ωt)` interaction; add instrumentation tolerances to
    proposed experiments.

## Low-Priority

- Replace remaining narrative flourishes (motivational calls to action) with
  neutral prose suited for technical publication.
- Consolidate repeated glossary sections scattered across multiple manuscripts.
- Populate newly added LaTeX chapter stubs with vetted content once each source
  document passes audit.
- Validate Pais-related gravitomagnetic and coupling equations against
  literature or flag prominently as speculative in the synthesis text.

Update this list as issues are resolved or newly discovered during migration.

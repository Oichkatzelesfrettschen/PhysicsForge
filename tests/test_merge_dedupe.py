from scripts.merge_and_analyze_equations import EquationMerger


def test_deduplicate_marks_related(tmp_path):
    # Create two rows with same normalized eq but different sources
    merger = EquationMerger()
    merger.all_equations = [
        {
            'EqID': 'X001', 'Equation': 'E = m c^2', 'Framework': 'General', 'Domain': 'GR',
            'SourceDoc': 'a.md', 'SourceLine': 1, 'Description': 'energy', 'VerificationStatus': 'Theoretical', 'RelatedEqs': ''
        },
        {
            'EqID': 'X002', 'Equation': 'E=m c^2', 'Framework': 'General', 'Domain': 'GR',
            'SourceDoc': 'b.md', 'SourceLine': 5, 'Description': 'energy', 'VerificationStatus': 'Theoretical', 'RelatedEqs': ''
        },
    ]

    merger.deduplicate()
    rel = [e for e in merger.all_equations if e['EqID'] == 'X002'][0]['RelatedEqs']
    assert rel == 'X001'


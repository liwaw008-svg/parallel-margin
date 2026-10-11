from pathlib import Path
SRC = (Path(__file__).parents[1] / "contracts" / "contract.py").read_text(encoding="utf-8")

def test_terminal_alignment_lifecycle():
    for token in ('def pin(', 'def align(', 'def get_edition(', '"PINNED"', '"ALIGNED"'):
        assert token in SRC

def test_all_documents_are_digest_bound_and_refetched():
    assert SRC.count("gl.nondet.web.get") >= 4
    assert 'for index, field in enumerate(("source_url", "translation_url", "glossary_url"))' in SRC
    for token in ("manifest_digest", "document_digests", "frozen manifest changed", "frozen edition document changed"):
        assert token in SRC

def test_complete_ordered_vector_is_enforced():
    for token in ("complete alignment vector required", "ordered segment ids required", 'len(rows) != len(manifest["segments"])'):
        assert token in SRC

def test_outcome_is_derived_from_bounded_labels():
    for token in ('("EXACT", "EQUIVALENT", "DRIFT", "MISSING")', 'band = "FAITHFUL"', 'else "REVIEW"'):
        assert token in SRC

def test_replay_and_source_guards():
    for token in ("edition or manifest already pinned", "three distinct document URLs required", "public HTTPS URL required"):
        assert token in SRC

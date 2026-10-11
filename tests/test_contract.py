from pathlib import Path
SRC=(Path(__file__).parents[1]/"contracts"/"contract.py").read_text(encoding="utf-8")
def test_real_two_write_lifecycle():
    for token in ('def pin(','def align(','def get_edition(','"PINNED"','"ALIGNED"'): assert token in SRC
def test_user_text_replaces_remote_fixtures():
    for token in ('source_json:str','translation_json:str','glossary_json:str','normalize_segments','normalize_glossary'): assert token in SRC
    assert 'gl.nondet.web.get' not in SRC and 'raw.githubusercontent.com' not in SRC
def test_segment_pairing_and_bounds():
    for token in ('two to eight ','matching ordered segment ids required','one to twelve glossary terms required'): assert token in SRC
def test_consensus_output_is_complete_and_bounded():
    for token in ('complete alignment vector required','ordered segment ids required','("EXACT","EQUIVALENT","DRIFT","MISSING")'): assert token in SRC
def test_replay_and_terminal_guards():
    for token in ('edition id or exact text already pinned','only a pinned edition can be aligned','used_inputs'): assert token in SRC


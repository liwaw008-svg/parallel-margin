# Parallel Margin

Parallel Margin is a GenLayer translation-fidelity primitive. One public edition ticket binds an ordered source, its translation, a glossary, and the exact segment sequence. Validators independently fetch all four records, preserve their SHA-256 digests, and classify every segment as `EXACT`, `EQUIVALENT`, `DRIFT`, or `MISSING`.

## Why consensus is necessary

Translation equivalence is semantic, but the evidence envelope is deterministic. The model cannot skip a segment, add a label, change the order, or replace a source. The contract derives the final `FAITHFUL`, `USABLE`, or `REVIEW` band from the complete consensus vector.

## Lifecycle

1. `pin(manifest_url)` freezes the manifest and all three referenced documents as `PINNED`.
2. `align(edition_id)` refetches and digest-checks everything, then performs one complete alignment round.
3. The edition becomes terminal `ALIGNED`; `get_edition` exposes the complete audit trail.

Duplicate edition IDs and manifest digests are rejected. The supplied fixture demonstrates an English/French clinic-consent edition.

## Verify

```text
python -m pytest -q
genvm-lint contracts/contract.py
```

## Public artifacts

- Site: https://parallel-margin.pages.dev/
- Repository: https://github.com/liwaw008-svg/parallel-margin
- Network: StudioNet

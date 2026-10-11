# Parallel Margin

A bilingual workbench for checking whether a translation preserved the source, line by line.

Writers paste two to eight matching segment pairs and declare the glossary that must survive the crossing. The first transaction freezes that edition. The second asks GenLayer validators to classify every segment as `EXACT`, `EQUIVALENT`, `DRIFT`, or `MISSING`.

No hosted manifest and no GitHub content URL is part of the user journey. Duplicate edition IDs and identical text bundles are rejected; an aligned edition is terminal.

## Walkthrough

- Name the edition and choose two different languages.
- Write source and translation together in the split workbench.
- Add the bilingual terms that cannot drift.
- Freeze the edition on StudioNet.
- Run the margin audit and inspect each marked segment.

## Checks

```text
python -m pytest -q
genvm-lint contracts/contract.py
```

## Links

- https://parallel-margin.pages.dev/
- https://github.com/liwaw008-svg/parallel-margin
- https://explorer-studio.genlayer.com/address/0x3bf853420279E444CAA364FAAafb526eb06722Cf
- StudioNet


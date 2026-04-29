# TNG Persona Repo Notes

- Keep the dataset reproducible from transcript source. Prefer deterministic parsing over LLM-only preprocessing.
- When updating parsing logic, rerun the full pipeline and refresh generated outputs in `data/` and `docs/DATASET_REPORT.md`.
- Treat `docs/persona-notes.md` as the human-facing synthesis layer and the scripts as the source of truth.
- Avoid adding heavyweight dependencies unless they materially improve extraction quality.

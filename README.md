# Perceptual Sense Lab

Streamlit exercises for vision and hearing thresholds. All student work happens in `pages/`.

## Quick Start
- Install tools: see `docs/install.md`.
- Set up and run once: `uv python install 3.11 && uv sync && uv run streamlit run app.py`
- Open the app at http://localhost:8501.

## What You Edit
- Only files in `pages/`.
- Every required change is marked with a `TODO` docstring and a `NotImplementedError`.
- Shared 3AFC helpers live in `pages/_shared_3afc_student.py`; the rest are per-experiment pages.

## Files With TODOs
- Vision: `pages/greyscale_resolution.py`, `pages/smallest_noticeable_size.py`
- Hearing: `pages/pitch_frequency_range.py`, `pages/sound_gap_detection.py`, `pages/amplitude_threshold.py`, `pages/pitch_threshold.py`
- Shared: `pages/_shared_3afc_student.py`

## Daily Commands
- Run app: `uv run streamlit run app.py`
- Lint: `uv run ruff check .`
- Tests: `uv run pytest`

## Done Checklist
- No `NotImplementedError` remains in `pages/`.
- Pages load without crashes; bounds checks and clamps are in place.
- Lint and tests pass.
- Contrast page reports threshold %, log CS, and an estimated per-channel bit depth.
- 3AFC tasks stop after 6 reversals and use the last 4 to estimate the threshold.
- 3AFC pages should plot trial index vs. level with correct/incorrect markers and a threshold line.

## Documentation
- Setup: `docs/install.md`
- Assignment scope: `docs/assignment.md`
- Function guidance: `docs/student_functions.md`
- Architecture: `docs/app_logic.md`

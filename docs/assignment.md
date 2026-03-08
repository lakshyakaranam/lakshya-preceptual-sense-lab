# Assignment Guide

## Goal
Complete every `TODO` in the `pages/` directory so each experiment runs safely and without crashes. Do not redesign the UI or architecture.

## Scope
- Edit only files inside `pages/`.
- All required work is marked by a `TODO` docstring plus a `NotImplementedError`.
- Function names and signatures must stay unchanged.

### Files with TODOs
- Vision: `greyscale_resolution.py`, `smallest_noticeable_size.py`
- Hearing: `pitch_frequency_range.py`, `sound_gap_detection.py`, `amplitude_threshold.py`, `pitch_threshold.py`
- Shared helpers: `_shared_3afc_student.py`

## Order to Tackle (easy → hard)
1) `greyscale_resolution.py`  
2) `smallest_noticeable_size.py`  
3) `pitch_frequency_range.py`  
4) `_shared_3afc_student.py`  
5) `sound_gap_detection.py`  
6) `amplitude_threshold.py`  
7) `pitch_threshold.py`

## Rules of the Road
- Keep outputs compatible with the page code.
- Add safety checks (bounds, empty lists, divide-by-zero).
- Do not remove the instruction blocks.

## When You Are Done
- No `NotImplementedError` remains in `pages/`.
- Each page loads and runs without crashing.
- Adaptive values are clamped to configured limits.
- `uv run ruff check .` passes.
- `uv run pytest` passes.

## Quick Validation Loop
1. Implement one function.
2. Run the app page that uses it.
3. Read the first error line in any traceback; fix that.
4. Repeat until the page is stable, then move to the next TODO.

## Where to Get Help
1. `docs/student_functions.md`
2. `docs/app_logic.md`
3. `docs/install.md`

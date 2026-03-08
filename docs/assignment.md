# Assignment Guide

## Goal
Complete every `TODO` in the `pages/` directory so each experiment matches the spec below and runs safely. Do not redesign the UI or architecture.

## Scope
- Edit only files inside `pages/`.
- All required work is marked by a `TODO` docstring plus a `NotImplementedError`.
- Function names and signatures must stay unchanged.

### Files with TODOs
- Vision: `greyscale_resolution.py`, `smallest_noticeable_size.py`
- Hearing: `pitch_frequency_range.py`, `sound_gap_detection.py`, `amplitude_threshold.py`, `pitch_threshold.py`
- Shared helpers: `_shared_3afc_student.py`

## Vision Tasks

### Contrast Sensitivity (Pelli-style)
- Show single letters with decreasing contrast.
- Collect “can identify” responses until the letter is not legible.
- Report contrast threshold (%) and log contrast sensitivity.
- Also estimate per-channel bit depth from the percent threshold (e.g., ~8-bit ≈ 4% steps).

### Smallest Noticeable Size (Tumbling E style)
- Render an E-like shape with equal stroke and gap widths (t = d).
- Shrink the shape at a fixed viewing distance until forks are indistinguishable.
- Compute angular resolution (MAR) in arcminutes using screen geometry and distance.

## Hearing Tasks

### Pitch Frequency Range
- Play tones between 20 Hz and 20 kHz via slider or numeric input.
- Record the highest clearly audible frequency (at least to the nearest 50 Hz).

### 3AFC Adaptive Tests (shared rules)
- Format: 3 intervals, one target + two references.
- Adaptive rule: 2-down/1-up; harder after two consecutive correct, easier after any wrong.
- Step size shrinks on reversals; stop after the 6th reversal.
- Threshold = average of the last 4 reversals.
- Plot trial index vs. level with correct/incorrect markers and a threshold line.

#### Sound Gap Detection
- References: continuous noise bursts.
- Target: identical noise with a brief gap; report threshold gap in milliseconds.

#### Pitch Threshold
- References: steady reference tone (~2 s).
- Target: small pitch shift vs. reference; report threshold in Hz.

#### Amplitude Threshold
- References: steady reference tone (~2 s).
- Target: small amplitude change vs. reference; report threshold in dB.
- Keep pitch/time constant; avoid unsafe listening levels.

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
- 3AFC staircases use 2-down/1-up, stop after 6 reversals, and estimate threshold from the last 4 reversals.

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

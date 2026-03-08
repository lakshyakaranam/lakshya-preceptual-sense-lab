# Application Overview

## How It Runs
1. `app.py` renders the home page with links to each experiment in `pages/`.
2. A page loads config from `config/test_config.json`.
3. User actions update `st.session_state`; Streamlit reruns the script each time.
4. Adaptive pages stop when their finish criteria are met.

## Directory Map
- `pages/`: experiment flows plus student `TODO`s.
- `pages/_shared_3afc_student.py`: shared adaptive helpers for 3AFC pages.
- `utils/`: reusable plumbing (audio, config loading, adaptive logic, UI helpers).
- `config/`: parameter values and limits.
- `tests/`: unit tests for reusable modules.
- `docs/`: these guides.

## Utilities You Use but Don’t Edit
- `utils/test_config.py`: loads and caches config JSON.
- `utils/audio_tools.py`: builds waveforms and WAV bytes.
- `utils/adaptive_3afc.py`: adaptive staircase state and reversal tracking.
- `utils/three_afc.py`: shared 3AFC UI and response handling.

## Safety Expectations
- Return the documented types.
- Clamp levels and indices to configured bounds.
- Validate inputs before math; avoid divide-by-zero and empty-list crashes.
- Keep seeded behavior deterministic.

## Quick Debug Loop
1. Change one function.
2. Run the related page.
3. Read the first error line and fix that issue.
4. Repeat, then run `uv run pytest` and `uv run ruff check .`.

# Student Function Reference

Use this as a checklist while clearing each `TODO` in `pages/`.

## Vision: Contrast Sensitivity (`pages/greyscale_resolution.py`)
- `student_build_preview_triplets(letters_pool, rows, seed)`  
  - Return exactly `rows` strings of length 3, using a local `random.Random(seed)`. If `rows <= 0` or `letters_pool` is empty, return `[]`.
- `student_compute_contrast_levels(rows, step_log10)`  
  - For row `i`, level = `100 * 10 ** (-(i * step_log10))`. Return an empty list when `rows <= 0`.
- `student_advance_contrast_state(trial_index, response_yes, total_levels)`  
  - If response is `No`, finish. If `Yes`, move to the next index. Clamp within `[0, total_levels - 1]`. Mark finished when the schedule ends.
- `student_compute_log_contrast_sensitivity(threshold_percent)`  
  - Compute `log10(1 / (threshold_percent / 100))`. Guard against zero or negative input.

## Vision: Tumbling E (`pages/smallest_noticeable_size.py`)
- `student_next_size_index(current_index, is_correct, max_index)`  
  - Correct → `index + 1`; incorrect → `index - 1`; clamp to `[0, max_index]`.
- `student_build_trial_log_row(...)`  
  - Return a dict with all expected columns plus correctness; round MAR for readability.
- `student_validate_screen_geometry(distance_cm, screen_width_mm, screen_width_px)`  
  - Return `True` only when all values are positive and usable.
- `student_compute_mar_arcmin(size_px, mm_per_px, distance_cm)`  
  - Compute MAR (arcmin) using geometry; guard against zero/negative inputs.
- `student_format_trial_log_row(...)`  
  - Wrapper that enforces the same schema as the trial table.

## Hearing: Pitch Range (`pages/pitch_frequency_range.py`)
- `student_tone_preset(level, default_frequency_hz)`  
  - Map `easy` / `medium` / `hard` to `(frequency_hz, amplitude)`; provide a safe fallback for unknown levels.
- `student_estimate_audible_bounds(probe_history_hz, heard_flags)`  
  - Pair frequencies with heard flags; return min and max of heard frequencies, or a safe fallback if none were heard.
- `student_validate_audio_params(frequency_hz, amplitude)`  
  - Frequency within 20–20,000 Hz and amplitude in `(0, 1]`.

## Shared 3AFC Core (`pages/_shared_3afc_student.py`)
- `shared_student_apply_reversal_update(...)`  
  - One 2-down/1-up step; maintain streak logic; clamp to `[min_level, max_level]`.
- `shared_student_update_staircase_state(...)`  
  - Wrapper to keep staircase behavior consistent with the above.
- `shared_student_build_three_interval_targets(target_index)`  
  - Return a 3-item list with exactly one `True`.
- `shared_student_estimate_threshold_from_reversals(reversals, fallback_level, tail_count=4)`  
  - If enough reversals, average the last `tail_count`; otherwise use `fallback_level`.
- `shared_student_compute_recent_accuracy(history, window=12)`  
  - Percent correct over the last `window` trials; return 0–100.
- `shared_student_validate_audio_params(amplitude, stimulus_value)`  
  - Validate amplitude and the stimulus-specific value; strict `True`/`False`.
- `shared_student_plot_staircase(...)` and `shared_student_plot_staircase_with_threshold(...)`  
  - Plot levels over trials, mark correct vs incorrect, and draw a threshold line. Handle empty/short histories without crashing.

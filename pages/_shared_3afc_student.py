"""Shared TODOs for all 3AFC assignment pages.

Why this file exists:
- All 3AFC pages use the same staircase, accuracy, and plotting patterns.
- Shared logic is implemented here once and reused by all 3AFC pages.

Used by:
- pages/sound_gap_detection.py
- pages/amplitude_threshold.py
- pages/pitch_threshold.py

Implementation expectations:
- Keep return types exactly as annotated.
- Prefer small, pure functions with no Streamlit state mutations.
- Validate/clamp values to avoid invalid outputs.
"""
import matplotlib.pyplot as plt
import streamlit as st

def shared_student_apply_reversal_update(
    *,
    current_level: float,
    step: float,
    is_correct: bool,
    correct_streak: int,
    down_n: int,
    min_level: float,
    max_level: float,
) -> tuple[float, int]:
    """TODO: Apply one 2-down/1-up staircase update.

    Inputs:
        current_level: current adaptive stimulus level.
        step: step size for level change.
        is_correct: whether the response is correct.
        correct_streak: consecutive correct count before this trial.
        down_n: number of correct responses needed to step down.
        min_level: minimum allowed level.
        max_level: maximum allowed level.

    Returns:
        Tuple `(next_level, next_correct_streak)` after one update.

    Safety requirements:
        - Clamp level to `[min_level, max_level]`.
        - Treat `down_n < 1` as 1 to avoid zero-step loops.
    """
    down_n = max(down_n, 1)
    if is_correct:
        next_correct_streak = correct_streak + 1
        if next_correct_streak % down_n == 0:
                # down_n correct answers in a row
                next_level = max(current_level - step, min_level)
        else:
            next_level = current_level

    else:
        next_correct_streak = 0
        next_level = min(current_level + step, max_level)
    return(next_level, next_correct_streak)



def shared_student_plot_staircase(
    history: list[dict], threshold: float, y_label: str, title: str
) -> None:
    """TODO: Plot the staircase trace for the given history.

    Expected plot content:
        - X-axis: trial number.
        - Y-axis: level value per trial.
        - Visual distinction for correct vs incorrect trials.
        - Threshold drawn as a horizontal dashed line.

    Safety requirements:
        - Do not crash for empty or very short history lists.
    """
    if not history:
        return
    trial_no = []
    levels = []
    colors = []
    for i in range(len(history)):
        trial_no.append(i+1)
        levels.append(history[i]["Level"])
        if history[i]["Correct"] == "Yes":
            colors.append("green")
        else:
            colors.append("red")

    plt.figure(figsize=(12, 6))
    plt.axhline(y=threshold, linestyle = '--', label = 'Threshold')
    
    plt.scatter(trial_no, levels, color = colors, label = y_label)
    plt.scatter([], [], color = "green", label = "Correct")
    plt.scatter([], [], color = "red", label = "Wrong")
    plt.xlabel('Trial No')
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    st.pyplot(plt.gcf())


def shared_student_build_three_interval_targets(*, target_index: int) -> list[bool]:
    """TODO: Build a length-3 target mask with exactly one `True` entry.

    Example:
        target_index=1 -> [False, True, False]
    """
    three_interval = []
    for i in range(3):
        if i == target_index:
            three_interval.append(True)
        else:
            three_interval.append(False)
    return three_interval


def shared_student_update_staircase_state(
    *,
    current_level: float,
    step: float,
    is_correct: bool,
    correct_streak: int,
    down_n: int,
    min_level: float,
    max_level: float,
) -> tuple[float, int]:
    """TODO: Reusable helper that keeps staircase behavior consistent.

    This can wrap or share logic with `shared_student_apply_reversal_update`.
    """
    return shared_student_apply_reversal_update(
        current_level = current_level,
        step = step,
        is_correct = is_correct,
        correct_streak = correct_streak,
        down_n = down_n,
        min_level = min_level,
        max_level = max_level
    )


def shared_student_estimate_threshold_from_reversals(
    *, reversals: list[float], fallback_level: float, tail_count: int = 4
) -> float:
    """TODO: Estimate threshold using the trailing reversal points.

    Recommended behavior:
        - When there are enough reversals, average the last `tail_count` values.
        - Otherwise return `fallback_level`.
    """
    if len(reversals) >= tail_count:
        # enough reversals to determine a threshold value
        last_sum = sum(reversals[-tail_count:])
        threshold = last_sum / tail_count
    else:
        # if there are not enough reversals, the threshold will be set to fallback level
        threshold = fallback_level
    return threshold


def shared_student_compute_recent_accuracy(history: list[dict], window: int = 12) -> float:
    """TODO: Compute a trailing percent-correct accuracy metric.

    Output should be a percentage in the `[0, 100]` range.
    """
    if history == []:
        return
    valid_terms = history[-window:] # grab last "window" terms
    num_correct = 0
    for row in valid_terms:
        if row["Correct"] == "Yes":
            num_correct += 1
    percent = (num_correct / len(valid_terms)) * 100
    return percent


def shared_student_validate_audio_params(*, amplitude: float, stimulus_value: float) -> bool:
    """TODO: Validate amplitude and stimulus-specific numeric values.

    Returns:
        `True` when inputs are in safe ranges, otherwise `False`.
    """
    in_limits = False
    if 0 <= amplitude <= 1:
        if stimulus_value > 0:
            in_limits = True
    return in_limits


def shared_student_plot_staircase_with_threshold(
    *, history: list[dict], threshold: float, y_label: str, title: str
) -> None:
    """TODO: Wrapper that draws the staircase and highlights the threshold.

    Hint:
        Call `shared_student_plot_staircase(...)` internally to avoid duplicate code.
    """
    return shared_student_plot_staircase(
        history = history,
        threshold = threshold,
        y_label = y_label,
        title = title
    )
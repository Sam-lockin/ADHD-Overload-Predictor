import pandas as pd
import numpy as np

# -------------------------------
# Self-reported overload labeling
# -------------------------------

def label_overload(input_path="data/raw_behavior_data.csv",
                   output_path="data/labeled_overload_data.csv"):

    df = pd.read_csv(input_path)

    overload_scores = []

    for _, row in df.iterrows():
        # ---- Felt pressure (pushes overload up) ----
        pressure = (
            0.4 * row["stress_level"] +
            0.3 * row["task_count"] +
            0.2 * row["screen_time_hours"]
        )

        # ---- Felt coping (pulls overload down) ----
        coping = (
            0.35 * row["sleep_hours"] +
            0.45 * row["focus_score"]
        )

        # ---- Base overload before emotion ----
        base_overload = pressure - coping

        # ---- Normalize into a rough 0–100 scale ----
        base_overload = base_overload * 10 + 50

        # ---- Moderate self-report noise ----
        noise = np.random.normal(loc=0, scale=7)

        overload_score = base_overload + noise

        # ---- Clamp to valid range ----
        overload_score = max(0, min(100, overload_score))

        overload_scores.append(overload_score)

    df["overload_score"] = overload_scores

    df.to_csv(output_path, index=False)
    print(f"✅ Labeled data saved to {output_path}")


if __name__ == "__main__":
    label_overload()

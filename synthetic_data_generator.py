import pandas as pd
import random

def generate_adhd_college_data(n=2000, output_path="data/raw_behavior_data.csv"):
    data = []

    for _ in range(n):
        sleep_hours = round(random.uniform(3, 9), 1)
        screen_time_hours = round(random.uniform(2, 12), 1)
        stress_level = random.randint(1, 10)
        task_count = random.randint(1, 12)
        focus_score = random.randint(1, 10)

        data.append([
            sleep_hours,
            screen_time_hours,
            stress_level,
            task_count,
            focus_score
        ])

    df = pd.DataFrame(data, columns=[
        "sleep_hours",
        "screen_time_hours",
        "stress_level",
        "task_count",
        "focus_score"
    ])

    df.to_csv(output_path, index=False)
    print(f"✅ Generated {n} rows of raw ADHD behavioral data at {output_path}")

if __name__ == "__main__":
    generate_adhd_college_data(n=2000)










# import pandas as pd
# import random

# # Number of synthetic rows
# def generate_adhd_college_data(n=2000, output_path="data/overload_log.csv"):
#     data = []

#     for _ in range(n):
#         sleep_hours = round(random.uniform(3, 9), 1)              # college sleep range
#         screen_time_hours = round(random.uniform(2, 12), 1)       # phone + laptop
#         stress_level = random.randint(1, 10)                      # 1 = chill, 10 = panic
#         task_count = random.randint(1, 12)                        # assignments + chores
#         focus_score = random.randint(1, 10)                       # self-reported focus

#         # # Overload logic
#         # overload_score = 0

#         # if sleep_hours < 5:
#         #     overload_score += 2
#         # if screen_time_hours > 8:
#         #     overload_score += 2
#         # if stress_level > 6:
#         #     overload_score += 2
#         # if task_count > 6:
#         #     overload_score += 2
#         # if focus_score < 4:
#         #     overload_score += 2

#         # if overload_score <= 2:
#         #     overload_level = "Low"
#         # elif overload_score <= 5:
#         #     overload_level = "Medium"
#         # else:
#         #     overload_level = "High"

#         data.append([
#             sleep_hours,
#             screen_time_hours,
#             stress_level,
#             task_count,
#             focus_score,
#             overload_level
#         ])

#     df = pd.DataFrame(data, columns=[
#         "sleep_hours",
#         "screen_time_hours",
#         "stress_level",
#         "task_count",
#         "focus_score",
#         "overload_level"
#     ])

#     df.to_csv(output_path, index=False)
#     print(f"✅ Generated {n} rows of synthetic ADHD college data at: {output_path}")


# if __name__ == "__main__":
#     generate_adhd_college_data(n=2000)
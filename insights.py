import pandas as pd
import matplotlib.pyplot as plt

# Load labeled regression data
df = pd.read_csv("data/labeled_overload_data.csv")

print("Data loaded. Rows:", len(df))

# Helper function for consistent plots
def plot_relationship(x, y, xlabel, ylabel, title, filename):
    plt.figure(figsize=(6, 4))
    plt.scatter(df[x], df[y], alpha=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# 1. Sleep vs Overload
plot_relationship(
    x="sleep_hours",
    y="overload_score",
    xlabel="Sleep Hours",
    ylabel="Overload Score",
    title="Sleep vs Cognitive Overload",
    filename="sleep_vs_overload.png"
)

# 2. Screen Time vs Overload
plot_relationship(
    x="screen_time_hours",
    y="overload_score",
    xlabel="Screen Time (hours)",
    ylabel="Overload Score",
    title="Screen Time vs Cognitive Overload",
    filename="screen_vs_overload.png"
)

# 3. Stress vs Overload
plot_relationship(
    x="stress_level",
    y="overload_score",
    xlabel="Stress Level (1–10)",
    ylabel="Overload Score",
    title="Stress vs Cognitive Overload",
    filename="stress_vs_overload.png"
)

# 4. Task Count vs Overload
plot_relationship(
    x="task_count",
    y="overload_score",
    xlabel="Task Count",
    ylabel="Overload Score",
    title="Task Load vs Cognitive Overload",
    filename="tasks_vs_overload.png"
)

# 5. Focus vs Overload
plot_relationship(
    x="focus_score",
    y="overload_score",
    xlabel="Focus Score (1–10)",
    ylabel="Overload Score",
    title="Focus vs Cognitive Overload",
    filename="focus_vs_overload.png"
)

print("All insight plots generated successfully.")

# import matplotlib
# matplotlib.use('TkAgg')

# import pandas as pd
# import matplotlib.pyplot as plt

# # Load data
# df = pd.read_csv("data/overload_log.csv")

# print("\n=== Dataset Preview ===")
# print(df.head())

# # 1. Sleep vs Overload
# plt.figure()
# df.boxplot(column='sleep_hours', by='overload_level')
# plt.title('Sleep Hours vs Overload Level')
# plt.suptitle('')
# plt.xlabel('Overload Level')
# plt.ylabel('Sleep Hours')
# plt.show()

# # 2. Screen Time vs Overload
# plt.figure()
# df.boxplot(column='screen_time_hours', by='overload_level')
# plt.title('Screen Time vs Overload Level')
# plt.suptitle('')
# plt.xlabel('Overload Level')
# plt.ylabel('Screen Time (hours)')
# plt.show()

# # 3. Stress vs Overload
# plt.figure()
# df.boxplot(column='stress_level', by='overload_level')
# plt.title('Stress Level vs Overload Level')
# plt.suptitle('')
# plt.xlabel('Overload Level')
# plt.ylabel('Stress Level')
# plt.show()

# # 4. Number of Tasks vs Overload
# plt.figure()
# df.boxplot(column='num_tasks_today', by='overload_level')
# plt.title('Number of Tasks vs Overload Level')
# plt.suptitle('')
# plt.xlabel('Overload Level')
# plt.ylabel('Number of Tasks')
# plt.show()

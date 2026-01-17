import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/overload_log.csv", encoding="latin1")

print("Data loaded. Rows:", len(df))

# 1. Sleep vs Overload
plt.figure()
df.boxplot(column='sleep_hours', by='overload_level')
plt.title('Sleep Hours vs Overload Level')
plt.suptitle('')
plt.xlabel('Overload Level')
plt.ylabel('Sleep Hours')
plt.savefig("sleep_vs_overload.png")
plt.close()

# 2. Screen Time vs Overload
plt.figure()
df.boxplot(column='screen_time_hours', by='overload_level')
plt.title('Screen Time vs Overload Level')
plt.suptitle('')
plt.xlabel('Overload Level')
plt.ylabel('Screen Time (hours)')
plt.savefig("screen_vs_overload.png")
plt.close()

# 3. Stress vs Overload
plt.figure()
df.boxplot(column='stress_level', by='overload_level')
plt.title('Stress Level vs Overload Level')
plt.suptitle('')
plt.xlabel('Overload Level')
plt.ylabel('Stress Level')
plt.savefig("stress_vs_overload.png")
plt.close()

# 4. Tasks vs Overload
plt.figure()
df.boxplot(column='num_tasks_today', by='overload_level')
plt.title('Number of Tasks vs Overload Level')
plt.suptitle('')
plt.xlabel('Overload Level')
plt.ylabel('Number of Tasks')
plt.savefig("tasks_vs_overload.png")
plt.close()

print("Plots saved successfully!")



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

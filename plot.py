import pandas as pd
import matplotlib.pyplot as plt

# Load the power usage data from the CSV file
input_file = "total_power_usage.csv"
data = pd.read_csv(input_file)

# Extract data for plotting
time_seconds = data["Second"]
total_power = data["Total Power (W)"]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time_seconds, total_power, color="blue", label="Total Power (W)", linewidth=2)

# Add titles and labels
plt.title("Total Power Consumption Over Time", fontsize=16)
plt.xlabel("Time (Seconds)", fontsize=14)
plt.ylabel("Total Power (W)", fontsize=14)

# Grid and legend
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()

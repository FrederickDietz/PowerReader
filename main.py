#the idea was to get it down as simple as possible.
#it currently operates for about an hour before generating the file
#it has between a 30% and 50% margin of error due to its highly simple nature.
#I would've loved to have found a way to do this only on standard libraries, but that didn't happen
#V 1.00B
import psutil
import pandas as pd
import time

# Define approximate TDP values for your hardware
CPU_TDP = 65  # in Watts (adjust for your CPU)
MEMORY_TDP = 10  # Estimated constant power for memory

def estimate_total_power():
    """Estimate total power consumption in Watts."""
    # Get CPU usage and calculate power
    cpu_usage = psutil.cpu_percent(interval=1)  # Average over 1 second
    cpu_power = (cpu_usage / 100) * CPU_TDP

    # Memory power (constant approximation)
    mem_power = MEMORY_TDP

    # Calculate total power consumption
    total_power = cpu_power + mem_power

    return total_power

def monitor_power(duration=3600):
    """Monitor and log total power usage every second for the given duration."""
    power_data = []

    for second in range(duration):
        # Estimate total power consumption
        total_power = estimate_total_power()

        # Log data with a timestamp
        power_data.append({
            "Second": second + 1,
            "Total Power (W)": total_power,
            "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

        # Print progress every 60 seconds
        if (second + 1) % 60 == 0:
            print(f"Logged {second + 1} seconds of data...")

    return power_data

# Monitor power usage for 3600 seconds (1 hour)
print("Monitoring power usage for 1 hour...")
data = monitor_power(duration=3600)

# Convert to a DataFrame
df = pd.DataFrame(data)

# Display the grid
print(df)

# Save to a CSV file
output_file = "total_power_usage.csv"
df.to_csv(output_file, index=False)
print(f"Power usage data saved to {output_file}")

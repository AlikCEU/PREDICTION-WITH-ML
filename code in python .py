import pandas as pd

# Load dataset
file_path = "/mnt/data/WVS_subset.csv"
df = pd.read_csv(file_path, low_memory=False)

# Convert all values to numeric where possible
df = df.apply(pd.to_numeric, errors='coerce')

# Define missing values and replace them with NaN
missing_values = [-5, -4, -2]
df.replace(missing_values, pd.NA, inplace=True)

# Define selected variables for analysis
selected_variables = ["Q19", "Q22", "Q71", "Q49", "Q57"]

# Compute descriptive statistics excluding missing values
detailed_stats = df[selected_variables].dropna().describe().transpose()

# Rename columns for clarity
detailed_stats = detailed_stats.rename(columns={
    "count": "Count",
    "mean": "Mean",
    "std": "Std Dev",
    "min": "Min",
    "25%": "25%",
    "50%": "50% (Median)",
    "75%": "75%",
    "max": "Max"
})

# Display the cleaned summary statistics
import ace_tools as tools
tools.display_dataframe_to_user(name="Detailed Summary Statistics", dataframe=detailed_stats)

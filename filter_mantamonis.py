import pandas as pd

# === CONFIG ===
input_file = "Mantamonis_bacterial_contamination_analysis.xlsx"
output_file = "filtered_output.csv"

# Read Excel file
df = pd.read_excel(input_file)

# Columns we want (case-insensitive)
target_columns = {"preliminary verdict:", "seq coverage"}

# Create mapping of lowercase column names to original names
col_map = {col.lower(): col for col in df.columns}

# Find matching columns (case-insensitive)
selected_cols = [col_map[col] for col in target_columns if col in col_map]

if len(selected_cols) != len(target_columns):
    missing = target_columns - set(col_map.keys())
    raise ValueError(f"Missing columns: {missing}")

# Filter dataframe
filtered_df = df[selected_cols]

# Save to new Excel file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered file saved as: {output_file}")


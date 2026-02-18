import pandas as pd
import matplotlib.pyplot as plt

# === CONFIG ===
input_file = "filtered_output.csv"

# Load Excel
df = pd.read_csv(input_file)

# Case-insensitive column mapping
target_columns = {"preliminary verdict:", "seq coverage"}
col_map = {col.lower(): col for col in df.columns}

selected_cols = [col_map[col] for col in target_columns if col in col_map]

if len(selected_cols) != len(target_columns):
    missing = target_columns - set(col_map.keys())
    raise ValueError(f"Missing columns: {missing}")

df = df[selected_cols]

# Rename for easier access (normalized names)
df.columns = [col.lower() for col in df.columns]

# Ensure numeric type
df["seq coverage"] = pd.to_numeric(df["seq coverage"], errors="coerce")

# Drop rows with missing values
df = df.dropna(subset=["seq coverage", "preliminary verdict:"])

# =========================
# 1️⃣ Histogram of Coverage
# =========================
plt.figure(figsize=(8, 5))
plt.hist(df["seq coverage"], bins=20)
plt.xlabel("Seq Coverage")
plt.ylabel("Frequency")
plt.title("Distribution of Seq Coverage")
plt.tight_layout()
plt.show()

# ==========================================
# 2️⃣ Boxplot by Preliminary Verdict
# ==========================================
plt.figure(figsize=(8, 5))

groups = df.groupby("preliminary verdict:")["seq coverage"]
data = [group for name, group in groups]

plt.boxplot(data, labels=groups.groups.keys())
plt.xlabel("Preliminary Verdict")
plt.ylabel("Seq Coverage")
plt.title("Seq Coverage by Preliminary Verdict")
plt.tight_layout()
plt.savefig("test_plot.png")


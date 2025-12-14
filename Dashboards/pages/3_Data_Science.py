import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Science – Dataset Governance")

# ---------- DB CONNECTION ----------
conn = sqlite3.connect("database/platform.db")
query = """
SELECT id, name, size_bytes, rows, source
FROM datasets_metadata
"""
df = pd.read_sql_query(query, conn)

# ---------- SAFETY CHECK ----------
if df.empty:
    st.warning("No datasets found in database.")
    st.stop()

# ---------- CLEAN DATA ----------
df["size_mb"] = df["size_bytes"] / (1024 * 1024)

# ---------- DISPLAY DATA ----------
st.subheader("Available Datasets")
st.dataframe(
    df[["name", "size_mb", "rows", "source"]],
    use_container_width=True
)

# ---------- ANALYSIS ----------
st.subheader("📈 Resource Consumption Analysis")

largest_dataset = df.loc[df["size_mb"].idxmax()]
st.info(
    f"**Largest dataset:** {largest_dataset['name']} "
    f"({largest_dataset['size_mb']:.2f} MB)"
)

# ---------- VISUALIZATION ----------
fig, ax = plt.subplots()
ax.bar(df["name"], df["size_mb"])
ax.set_ylabel("Size (MB)")
ax.set_title("Dataset Size by Name")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

# ---------- GOVERNANCE INSIGHT ----------
st.subheader("🛡️ Governance Recommendation")

heavy_datasets = df[df["size_mb"] > 50]

if not heavy_datasets.empty:
    st.warning(
        "Some datasets consume high storage.\n\n"
        "✅ Recommendation:\n"
        "- Archive rarely used large datasets\n"
        "- Apply access controls\n"
        "- Schedule regular audits"
    )
else:
    st.success(
        "All datasets are within acceptable size limits.\n"
        "No immediate governance action required."
    )

st.info("IT-owned datasets consume more storage than HR, suggesting archiving policies for logs.")
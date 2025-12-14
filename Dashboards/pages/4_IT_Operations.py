import streamlit as st
import pandas as pd
from services.database_manager import DatabaseManager

st.set_page_config(page_title="IT Operations", layout="wide")

st.title("🛠 IT Operations – Service Desk Performance")

# Connect to database
db = DatabaseManager("database/platform.db")
db.connect()

# Fetch tickets (ONLY existing columns)
rows = db.fetch_all("""
SELECT title, priority, status, assigned_to
FROM it_tickets
""")

if not rows:
    st.warning("No IT tickets found.")
    st.stop()

# Convert to DataFrame
df = pd.DataFrame(
    rows,
    columns=["Title", "Priority", "Status", "Assigned To"]
)

# ---------------- DISPLAY ----------------
st.subheader("📋 IT Support Tickets")
st.dataframe(df, use_container_width=True)

# ---------------- ANALYSIS ----------------
st.subheader("📊 Bottleneck Analysis")

status_counts = df["Status"].value_counts()
st.bar_chart(status_counts)

worst_status = status_counts.idxmax()
st.error(f"🚨 Bottleneck detected: **{worst_status}** status has the most tickets.")

# Staff workload
st.subheader("👨‍💻 Staff Workload Distribution")
staff_counts = df["Assigned To"].value_counts()
st.bar_chart(staff_counts)

top_staff = staff_counts.idxmax()
st.warning(
    f"⚠️ Staff member **{top_staff}** is handling the most tickets. Consider workload balancing."
)

# ---------------- FINAL INSIGHT ----------------
st.subheader("✅ Management Recommendation")

st.success(
    "Reduce delays by improving workflow for high-volume statuses and redistributing "
    "tickets from overloaded staff."
)
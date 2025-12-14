import streamlit as st
from services.database_manager import DatabaseManager
from models.security_incident import SecurityIncident

st.title("🛡️ Cybersecurity Dashboard")

db = DatabaseManager("database/platform.db")
rows = db.fetch_all("""
SELECT id, incident_type, severity, status, description
FROM security_incidents
""")

incidents = [
    SecurityIncident(*row) for row in rows
]

# KPI
open_count = sum(1 for i in incidents if i.get_status() == "Open")
resolved_count = sum(1 for i in incidents if i.get_status() == "Resolved")
phishing_count = sum(1 for i in incidents if i.get_incident_type() == "Phishing")

st.metric("Open Incidents", open_count)
st.metric("Resolved Incidents", resolved_count)
st.metric("Phishing Incidents", phishing_count)

st.subheader("Incident List")
for i in incidents:
    st.write(i)

    import pandas as pd

st.subheader("Incident Status Overview")

status_data = {
    "Open": open_count,
    "Resolved": resolved_count
}

df = pd.DataFrame(
    list(status_data.items()),
    columns=["Status", "Count"]
)

st.bar_chart(df.set_index("Status"))
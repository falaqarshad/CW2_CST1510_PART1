import streamlit as st
from services.database_manager import DatabaseManager
from models.security_incident import SecurityIncident

st.title("🛡️ Cybersecurity Incidents")

# Connect to DB
db = DatabaseManager("database/platform.db")
db.connect()

rows = db.fetch_all("""
    SELECT id, incident_type, severity, status, description
    FROM cyber_incidents
""")

incidents = [
    SecurityIncident(*row) for row in rows
]

# ---- DISPLAY INCIDENTS ----
if not incidents:
    st.info("No incidents found.")
else:
    for incident in incidents:
        with st.expander(str(incident)):
            st.write("Incident Type:", incident.get_incident_type())
            st.write("Severity:", incident.get_severity())
            st.write("Status:", incident.get_status())
            st.write("Description:", incident.get_description())

# ---- ANALYSIS (PART 1 REQUIREMENT) ----
st.divider()
st.subheader("📊 Incident Analysis")

phishing_count = sum(
    1 for i in incidents if i.get_incident_type().lower() == "phishing"
)

severity_count = {}
for i in incidents:
    severity_count[i.get_severity()] = severity_count.get(i.get_severity(), 0) + 1

st.metric("Phishing Incidents", phishing_count)
st.bar_chart(severity_count)

st.subheader("⏱️ Response Bottleneck")

status_count = {}
for i in incidents:
    status_count[i.get_status()] = status_count.get(i.get_status(), 0) + 1

st.bar_chart(status_count)

worst_status = max(status_count, key=status_count.get)
st.warning(f"Biggest bottleneck: {worst_status}")

phishing_count = sum(1 for i in incidents if i.type == "Phishing")
st.metric("Phishing Incidents", phishing_count)
st.warning("Phishing incidents dominate the backlog → response bottleneck")
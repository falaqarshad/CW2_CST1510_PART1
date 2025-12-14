import sqlite3

conn = sqlite3.connect("database/platform.db")
cursor = conn.cursor()

cursor.executemany("""
INSERT INTO security_incidents (incident_type, severity, status, description)
VALUES (?, ?, ?, ?)
""", [
    ("Phishing", "High", "Open", "Suspicious email targeting staff"),
    ("Malware", "Medium", "Resolved", "Malware detected on workstation"),
    ("Phishing", "Critical", "Open", "Credential harvesting attempt"),
    ("DDoS", "Low", "Resolved", "Short denial-of-service spike"),
])

conn.commit()
conn.close()

print("✅ Security incidents seeded")
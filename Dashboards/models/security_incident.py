class SecurityIncident:
    """
    Represents a cybersecurity incident.
    """

    def __init__(self, incident_id, incident_type, severity, status, description):
        self._id = incident_id
        self._incident_type = incident_type
        self._severity = severity
        self._status = status
        self._description = description

    def get_id(self) -> int:
        return self._id

    def get_incident_type(self) -> str:
        return self._incident_type

    def get_severity(self) -> str:
        return self._severity

    def get_status(self) -> str:
        return self._status

    def get_description(self) -> str:
        return self._description

    def __str__(self):
        return f"Incident {self._id}: {self._incident_type} ({self._severity})"
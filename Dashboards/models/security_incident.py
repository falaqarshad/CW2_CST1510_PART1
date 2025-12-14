class SecurityIncident:
    def __init__(self, incident_id, incident_type, severity, status, description):
        self.__id = incident_id
        self.__incident_type = incident_type
        self.__severity = severity
        self.__status = status
        self.__description = description

    def get_incident_type(self):
        return self.__incident_type

    def get_severity(self):
        return self.__severity

    def get_status(self):
        return self.__status

    def update_status(self, new_status):
        self.__status = new_status

    def __str__(self):
        return f"{self.__incident_type} | {self.__severity} | {self.__status}"
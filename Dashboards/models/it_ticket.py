class ITTicket:
    """Represents an IT support ticket in the platform."""

    def __init__(self, ticket_id, title, priority, status, assigned_to, created_at, resolved_at):
        self._id = ticket_id
        self._title = title
        self._priority = priority
        self._status = status
        self._assigned_to = assigned_to
        self._created_at = created_at
        self._resolved_at = resolved_at

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_priority(self):
        return self._priority

    def get_status(self):
        return self._status

    def get_assigned_to(self):
        return self._assigned_to

    def get_created_at(self):
        return self._created_at

    def get_resolved_at(self):
        return self._resolved_at
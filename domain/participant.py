class Participant:
    def __init__(self, name):
        self.name = name
        self.event_ids = []

    def add_event_id(self, event_id):
        self.event_ids.append(event_id)

    def __str__(self):
        return f"Participant: {self.name}"

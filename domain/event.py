class Event:
    def __init__(self, event_id, title, city, participants, max_participants, start_date, end_date):
        self.event_id = event_id
        self.title = title
        self.city = city
        self.participants = participants
        self.max_participants = max_participants
        self.start_date = start_date
        self.end_date = end_date

    def add_participant(self, participant_name):
        self.participants.append(participant_name)

    def __str__(self):
        return f"Event: {self.title}, City: {self.city}, Participants: {len(self.participants)}"

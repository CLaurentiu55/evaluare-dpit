from datetime import datetime, timedelta


class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def delete_event(self, event_id):
        self.events = [event for event in self.events if event.event_id != event_id]

    def modify_event(self, event_id, new_event):
        for i, event in enumerate(self.events):
            if event.event_id == event_id:
                self.events[i] = new_event
                break

    def get_events(self):
        return self.events

    def get_events_by_city(self, city):
        return [event for event in self.events if event.city == city]

    def get_participants_for_event(self, event_id):
        return [participant for participant in self.get_all_participants() if event_id in participant.event_ids]

    def get_events_sorted_by_participants(self):
        return sorted(self.events, key=lambda event: len(event.participants), reverse=True)

    def get_events_starting_soon(self, days=7):
        today = datetime.today()
        end_date = today + timedelta(days=days)
        return [event for event in self.events if today <= event.start_date <= end_date]

    def get_events_in_month_sorted_by_duration(self, month):
        events_in_month = [event for event in self.events if event.start_date.month == month]
        return sorted(events_in_month, key=lambda event: (event.end_date - event.start_date).days, reverse=True)

    def get_all_participants(self):
        all_participants = []
        for event in self.events:
            all_participants.extend(event.participants)
        return all_participants

    def get_event_by_id(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None

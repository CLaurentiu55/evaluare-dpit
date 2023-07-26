from datetime import datetime
from domain.event import Event
from domain.participant import Participant


class UI:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    @staticmethod
    def print_events(events):
        for event in events:
            print(
                f"ID: {event.event_id}, "
                f"Title: {event.title}, "
                f"City: {event.city}, "
                f"Participants: {len(event.participants)}")

    @staticmethod
    def print_participants(participants):
        for participant in participants:
            print(participant)

    @staticmethod
    def display_main_menu():
        print("Main Menu:")
        print("1) Organizer Menu")
        print("2) Participant Menu")
        print("0) Exit")

    @staticmethod
    def display_organizer_menu():
        print("Organizer Menu:")
        print("1) Add Event")
        print("2) Delete Event")
        print("3) Modify Event")
        print("4) View Events")
        print("5) View Events in a City")
        print("6) View Participants for Event")
        print("7) View Events Sorted by Participants")
        print("0) Back")

    @staticmethod
    def display_participant_menu():
        print("Participant Menu:")
        print("1) View Events")
        print("2) Register for Event")
        print("3) View Events Starting Soon")
        print("4) View Events in a Month Sorted by Duration")
        print("0) Back")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")

            if choice == '0':
                print("Exiting...")
                break
            elif choice == '1':
                self.run_organizer_menu()
            elif choice == '2':
                self.run_participant_menu()
            else:
                print("Invalid choice! Please try again.")

    def run_organizer_menu(self):
        while True:
            self.display_organizer_menu()
            choice = input("Enter your choice: ")

            if choice == '0':
                break
            elif choice == '1':
                self.add_event()
            elif choice == '2':
                self.delete_event()
            elif choice == '3':
                self.modify_event()
            elif choice == '4':
                self.view_events()
            elif choice == '5':
                self.view_events_by_city()
            elif choice == '6':
                self.view_participants_for_event()
            elif choice == '7':
                self.view_events_sorted_by_participants()
            else:
                print("Invalid choice! Please try again.")

    def run_participant_menu(self):
        while True:
            self.display_participant_menu()
            choice = input("Enter your choice: ")

            if choice == '0':
                break
            elif choice == '1':
                self.view_events()
            elif choice == '2':
                self.register_for_event()
            elif choice == '3':
                self.view_events_starting_soon()
            elif choice == '4':
                self.view_events_in_month_sorted_by_duration()
            else:
                print("Invalid choice! Please try again.")

    def add_event(self):
        event_id = input("Enter the event ID: ")
        title = input("Enter the event title: ")
        city = input("Enter the city: ")
        participants = []
        max_participants = int(input("Enter the maximum number of participants: "))
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date (YYYY-MM-DD): ")

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

            event = Event(event_id, title, city, participants, max_participants, start_date, end_date)
            self.event_manager.add_event(event)
            print("Event added successfully!")
        except ValueError:
            print("Invalid date format! Please use the format YYYY-MM-DD.")

    def delete_event(self):
        event_id = input("Enter the event ID to delete: ")
        event = self.event_manager.get_event_by_id(event_id)
        if event:
            self.event_manager.delete_event(event_id)
            print("Event deleted successfully!")
        else:
            print("Event not found!")

    def modify_event(self):
        event_id = input("Enter the event ID to modify: ")
        event = self.event_manager.get_event_by_id(event_id)
        if event:
            title = input(f"Enter the new title (leave empty to keep the current one: {event.title}): ")
            city = input(f"Enter the new city (leave empty to keep the current one: {event.city}): ")
            participants = input(f"Enter the new number of participants (leave empty to keep the current one: {len(event.participants)}): ")
            max_participants = input(f"Enter the new maximum number of participants (leave empty to keep the current one: {event.max_participants}): ")
            start_date_str = input(f"Enter the new start date (YYYY-MM-DD) (leave empty to keep the current one: {event.start_date}): ")
            end_date_str = input(f"Enter the new end date (YYYY-MM-DD) (leave empty to keep the current one: {event.end_date}): ")

            if title:
                event.title = title
            if city:
                event.city = city
            if participants:
                event.participants = int(participants)
            if max_participants:
                event.max_participants = int(max_participants)
            if start_date_str:
                try:
                    event.start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format! Start date not modified.")
            if end_date_str:
                try:
                    event.end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format! End date not modified.")

            print("Event modified successfully!")
        else:
            print("Event not found!")

    def view_events(self):
        events = self.event_manager.get_events()
        self.print_events(events)

    def view_events_by_city(self):
        city = input("Enter the city name: ")
        events = self.event_manager.get_events_by_city(city)
        self.print_events(events)

    def view_participants_for_event(self):
        event_id = input("Enter the event ID: ")
        participants = self.event_manager.get_participants_for_event(event_id)
        self.print_participants(participants)

    def view_events_sorted_by_participants(self):
        events = self.event_manager.get_events_sorted_by_participants()
        self.print_events(events)

    def register_for_event(self):
        event_id = input("Enter the event ID you want to register for: ")
        participant_name = input("Enter your name: ")

        event = self.event_manager.get_event_by_id(event_id)

        if not event:
            print("Event not found.")
            return

        if len(event.participants) >= event.max_participants:
            print("Event is already full. Cannot register.")
            return

        participant = Participant(participant_name)
        event.add_participant(participant_name)
        participant.add_event_id(event_id)
        self.event_manager.modify_event(event_id, event)

        print(f"{participant_name} successfully registered for the event '{event.title}' (Event ID: {event_id}).")

    def view_events_starting_soon(self):
        events = self.event_manager.get_events_starting_soon()
        self.print_events(events)

    def view_events_in_month_sorted_by_duration(self):
        month = int(input("Enter the month (1-12): "))
        events = self.event_manager.get_events_in_month_sorted_by_duration(month)
        self.print_events(events)

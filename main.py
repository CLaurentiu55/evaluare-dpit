from service.event_manager import EventManager
from ui.console import UI

event_manager = EventManager()
ui = UI(event_manager)
ui.run()
from datetime import datetime
from flask import abort, make_response
from user import USER

class Event:
    def __init__(self, event_id, event_name, event_date, event_time):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create(user_id, event):
    if user_id in USER:
        event_id = len(USER[user_id]["events"]) + 1
        new_event = Event(event_id, event["event_name"], event["event_date"], event["event_time"])
        USER[user_id]["events"].append(new_event.__dict__)
        return make_response("", 201)
    else:
        abort(
            404, f"Person with ID {user_id} not found"
        )

def read_one(user_id, event_id):
    if user_id in USER:
        events = USER[user_id]["events"]
        for event in events:
            if event["event_id"] == event_id:
                return event
        abort(
            404, f"Event with ID {event_id} not found for person with ID {user_id}"
        )
    else:
        abort(
            404, f"Person with ID {user_id} not found"
        )

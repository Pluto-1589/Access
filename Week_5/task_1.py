import datetime


class Calendar:
    """datetime module and the sorted() function to effectively manage events in the calendar. The main focus is on implementing functionality for adding, deleting, and retrieving calendar events.

    The constructor initializes the class. It should create an empty data structure to store events, and it should keep track of a unique, incrementing event ID.

    Otherwise, assign a unique ID to the event and store it in the calendar data structure. This ID should start at 1 and increase with each event entry that is being added. Finally, the assigned ID for the added event gets returned.

     datetime.date and datetime.time.

    Hint: Use Python's built-in sorted() function to order the events by their start_time before returning them."""

    def __init__(self):
        self.events = {}
        self.id_tracker = 1

    def add_event(self, date_str, start_time, end_time, description):
        """add_event(date_str, start_time, end_time, description): Adds a new event to the calendar. It takes the following parameters: date_str (string): The date for the event in YYYY-MM-DD format.
        start_time (string): The start time in HH:MM format. end_time (string): The end time in HH:MM format.
        description (string): The description of the event. If the start_time is greater than or equal to end_time, the method should raise an Exception. To raise an exception, you simply execute the statement raise Exception("your desired error message"), providing an error message to the Exception constructor as a string."""

        # check if start time is equal or greater than end time, if so exception
        if start_time >= end_time:
            raise Exception(
                "Invalid input, start time is greater or the same as end time")

        # create a local event id which has the same value as the class's id tracker
        event_id = self.id_tracker
        # assign information of to a dedicated variable
        event_info = (date_str, start_time, end_time, description)

        # increment class's id tracker by 1
        self.id_tracker += 1

        # add to events dict
        self.events[event_id] = event_info

        return event_id

    def get_events(self, date_str):
        """ get_events(date_str): Gets the list of events for a given date. It takes one parameter:
        date_str (string): The date in YYYY-MM-DD format.The method returns an empty list if no events are scheduled for the given date. Otherwise, it returns a list of tuples, where each tuple contains: (event_id, start_time, end_time, description) of the events scheduled for the given date. Make sure to format it accordingly based on this example: (1, '21:00', '23:59', 'Sleep'). The list of events should be sorted by start_time."""

        # empty lst if date str not found in values of events dict
        if all(date_str != event[0] for event in self.events.values()):
            return []
        else:
            date_lst = []
            for k, v in self.events.items():
                if date_str in v[0]:
                    date_lst.append(k)
                    for i in v:
                        date_lst.append(i)

            # date_lst.sort(key=lambda x: x[1])

            return date_lst

    def delete_event(self, event_id):
        """ 4. delete_event(event_id): Deletes an event from the calendar. It takes one parameter:event_id (integer): The unique identifier of the event.The method raises an Exception if the event with the given event_id does not exist. Otherwise, it removes the entry from the calendar data structure. Finally, the deleted event tuple (event_id, start_time, end_time, description) gets returned."""
        if event_id not in self.events:
            raise Exception("ID does not exist in calendar")
        else:
            end_val = self.events[event_id]
            del (self.events[event_id])
            return end_val


# You can play around with your implementation in the following body.
# The contained statements will be ignored while evaluating your solution.
if __name__ == "__main__":

    cal = Calendar()

    event_id_dinner = cal.add_event(
        "2024-12-24", "18:00", "20:00", "Christmas Dinner with Family")
    print(event_id_dinner)
    event_id_sleep = cal.add_event("2024-12-24", "21:00", "23:59", "Sleep")
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_dinner)
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_sleep)
    print(cal.get_events("2024-12-24"))

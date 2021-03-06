class Events:
    """
    A list of events, with support for reactions.
    """
    def __init__(self, reactor=None):
        self.reactor = reactor
        self.events = []

    def happening(self, event):
        """
        Add an event to the event list, and triggers reactions for this event.
        If no reactor is provided, only adds events.
        """
        self.events.append(event)
        if self.reactor:
            self.reactor.apply_events_triggered_by(event)
        return self

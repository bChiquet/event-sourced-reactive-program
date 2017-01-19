class Events:
    def __init__(self, reactor):
        self.reactor = reactor
        self.events = []

    def happening(self, event):
        self.events.append(event)
        self.reactor.apply_events_triggered_by(event)

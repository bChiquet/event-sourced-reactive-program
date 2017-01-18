event_reaction_map = {}


def apply_events_triggered_by(event):
        if event in event_reaction_map:
            for reaction in event_reaction_map[event]:
                reaction()


def react_to(event):
    def reaction_subscription(reaction):
        subscribe_reaction(reaction)
        return reaction

    def subscribe_reaction(reaction):
        if event in event_reaction_map:
            event_reaction_map[event].append(reaction)
        else:
            event_reaction_map[event] = [reaction]

    return reaction_subscription


@react_to("complaint")
def react_to_complaint():
    print("That's outrageous !")
    events.happening("reaction")


@react_to("reaction")
def react_to_reaction():
    print("You said it, mate !")


class Events:
    def __init__(self):
        self.events = []

    def happening(self, event):
        self.events.append(event)
        apply_events_triggered_by(event)


events = Events()
events.happening("complaint")

class Reactor:
    def __init__(self):
        self.event_reaction_map = {}

    def apply_events_triggered_by(self, event):
            if event in self.event_reaction_map:
                for reaction in self.event_reaction_map[event]:
                    reaction()

    def react_to(self, event):
        def reaction_subscription(reaction):
            subscribe_reaction(reaction)
            return reaction  # In order for reaction to be uncallable from the outside, you can return pass function.

        def subscribe_reaction(reaction):
            if event in self.event_reaction_map:
                self.event_reaction_map[event].append(reaction)
            else:
                self.event_reaction_map[event] = [reaction]

        return reaction_subscription

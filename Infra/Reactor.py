class Reactor:
    """
    A map linking events and planned reactions.
    """
    def __init__(self):
        self.event_reaction_map = {}

    def apply_events_triggered_by(self, event):
        """
        Triggers all the reactions declared for an event.
        NOTE : Reactions are fired in the order they are declared. This may change, don't use this property.
        """
        if event in self.event_reaction_map:
            for reaction in self.event_reaction_map[event]:
                reaction()  # TODO should probably create better interface(s) for reaction to receive event-linked info

    def react_to(self, event):
        # TODO Think about giving the pattern of an event and not an event itself
        # Get pattern matching ? Split events into event and event "classes" ?
        # I like that anything can be an event, but then pattern matching is not simple...
        """
        (intended to be used as a decorator)
        Declares a function to be triggered when an event happens.
        :param event: the event to be linked to a function
        :return: the decorator linking a function to the event.
        """
        def reaction_subscription(reaction):
            subscribe_reaction(reaction)
            return reaction

        def subscribe_reaction(reaction):
            if event in self.event_reaction_map:
                self.event_reaction_map[event].append(reaction)
            else:
                self.event_reaction_map[event] = [reaction]

        return reaction_subscription

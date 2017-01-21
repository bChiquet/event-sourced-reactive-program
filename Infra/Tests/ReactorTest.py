from unittest import TestCase
from unittest.mock import MagicMock, call

from Infra.Reactor import Reactor


class ReactorTest(TestCase):
    def test_react_to_adds_events_to_event_trigger_list(self):
        reaction = lambda: print("mock reaction")
        reactor = Reactor()

        decorator = reactor.react_to("event")
        decorator(reaction)

        self.assertIn("event", reactor.event_reaction_map)
        self.assertIn(reaction, reactor.event_reaction_map["event"])

    def test_apply_events_triggers_functions_subscribed_for_an_event(self):
        reaction = MagicMock()
        other_reaction = MagicMock()
        reactor = Reactor()
        decorator = reactor.react_to("event")
        decorator(reaction)
        decorator(other_reaction)

        reactor.apply_events_triggered_by("event")

        self.assertEqual([call()], reaction.call_args_list)
        self.assertEqual([call()], other_reaction.call_args_list)

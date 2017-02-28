from unittest import TestCase
from unittest.mock import Mock

from Infra.ESR.Events import Events


class EventsTest(TestCase):
    def test_event_should_be_added_to_events_list(self):
        reactor = Mock()
        events = Events(reactor)\
            .happening("event")\
            .happening("otherEvent")
        self.assertEqual(events.events, ["event", "otherEvent"])

    def test_adding_an_event_should_fire_reactor_for_that_event(self):
        reactor = Mock()
        Events(reactor).happening("event")
        reactor.apply_events_triggered_by.assert_called_once_with("event")

    def test_when_Events_is_created_without_reactor_do_not_call_reactor(self):
        Events().happening("event")

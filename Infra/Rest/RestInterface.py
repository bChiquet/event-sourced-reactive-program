from flask import Flask
from Infra.Rest.RequestManager import RequestManager

OK = ""


class RestAPI:
    """
    An API to bind REST requests to events.
    """
    def __init__(self, name, events):
        self.events = events
        # TODO think about how to properly segregate the specific server implementation.
        # This should only be an interface and not strongly linked to Flask.
        self.net = Flask(name)

    def add_event(self, url=None, event=None, handler=None, **options):
        # TODO if both event and handler are provided, would it not be smarter to execute both ?
        # If yes, should they be ordered ?
        """
        Binds an URL on the server to the creation of an event.
        If a handler is provided instead of the event, executes
        the handler instead (handler must create event).
        :param url: the server URL which will be bound to the event.
        :param event: event to be created when request comes.
        :param handler: custom request handler.
        :param options: currently used for Flask optional args.
        :return: TODO manage split request/answer execution
        """
        def valid_url_and_event():
            return \
                (event is not None or handler is not None) \
                and url is not None

        def prepare_handler():
            def default_handler():
                self.events.happening(event)
                return OK

            if handler is None:
                return default_handler
            else:
                return handler(self.events)

        if valid_url_and_event():
            handler = prepare_handler()
            # TODO URL rule subscription should probably not be managed now.
            # Better do it in the request manager (should request manager really be separate ?)
            self.net.add_url_rule(url, url, handler, **options)
            return RequestManager()

    def start(self):
        self.net.run()

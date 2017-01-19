from flask import Flask


class RestAPI:
    def __init__(self, name, events):
        self.events = events
        self.net = Flask(name)

    def add_event_url(self, url=None, event=None, handler=None, **options):
        def valid_url_and_event():
            return \
                (event is not None or handler is not None) \
                and url is not None

        def prepare_handler():
            def default_handler():
                self.events.happening(event)
                return ""

            if handler is None:
                return default_handler
            else:
                return handler(self.events)

        if valid_url_and_event():
            handler = prepare_handler()
            self.net.add_url_rule(url, None, handler, **options)

    def run(self):
        self.net.run()

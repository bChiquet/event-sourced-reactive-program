from flask import Flask

OK = ""


def business_api(events):
    # About Async request/response : http://codevoyagers.com/2016/09/01/from-flask-to-aiohttp/
    # this needs 3.5
    server = Flask("")

    @server.route("/complain")
    def simple_complaint():
        events.happening("complaint")
        return OK

    return server

from flask import Flask

OK = ""


def business_api(events):
    server = Flask("")

    @server.route("/complain")
    def simple_complaint():
        events.happening("complaint")
        return OK

    return server

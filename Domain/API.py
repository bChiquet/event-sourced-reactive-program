def business_api(server):

    def extra_hot_complaint(events):
        def handler():
            print("ow, extra hot!")
            events.happening("complaint")
            return server.OK
        return handler

    server.add_event_url(url="/hot-complaint", handler=extra_hot_complaint)
    server.add_event_url(url="/complaint", event="complaint", methods=['POST'])

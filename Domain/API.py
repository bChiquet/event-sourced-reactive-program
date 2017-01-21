from Infra.Rest.RestInterface import OK


def business_api(server):

    def extra_hot_complaint(events):  # TODO this signature probably needs improvement.
        def handler():
            print("ow, extra hot!")
            events.happening("complaint")
            return OK
        return handler

    def make_answer(*args, **kwargs):  # TODO what signature for this ?
        return "a complaint response was made"

    server.add_event(url="/hot-complaint", handler=extra_hot_complaint)
    server.add_event(url="/complain-with-infos", event="precise-complaint", methods=['POST'])

    server.add_event(url="/complain", event="complaint")\
          .answer_when(event="complaint-response", response=make_answer)

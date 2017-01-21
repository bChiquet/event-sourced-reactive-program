class RequestManager:
    # TODO split the request service in two parts, 1) request parsing and 2) response :
    # -Request parsing and response should be triggerable by different events.
    # -Context should be stored without having to actively wait for the response event.

    def answer_when(self, event, response):
        # TODO this would respond by fetching stored request context when event is triggered.
        pass

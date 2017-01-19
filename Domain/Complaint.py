def reactions(events, reactor):

    @reactor.react_to("complaint")
    def express_outrage():
        print("That's outrageous !")
        events.happening("outrage")

    @reactor.react_to("outrage")
    def concur():
        print("You said it, mate !")

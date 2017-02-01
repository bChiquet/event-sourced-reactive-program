from Domain.API import business_api
from Domain.Complaint import business_reactions
from Infra.Events import Events
from Infra.Reactor import Reactor

reactor = Reactor()
events = Events(reactor)
business_reactions(events, reactor)

business_api(events).run()

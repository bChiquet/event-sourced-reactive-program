from Domain.API import business_api
from Domain.Complaint import business_reactions
from Infra.ESR.Events import Events
from Infra.ESR.Reactor import Reactor

reactor = Reactor()
events = Events(reactor)

business_reactions(events, reactor)

business_api(events).run()

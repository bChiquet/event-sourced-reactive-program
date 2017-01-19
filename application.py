from Domain.Complaint import reactions
from Infra.Events import Events
from Infra.Reactor import Reactor

reactor = Reactor()
events = Events(reactor)

business = reactions(events, reactor)

events.happening("complaint")

# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.events.event_base import Event

class RouteStartedPayload(Record):
    product_uuid = String()
    product_quantity = String()

class EventRouteStarted(Event):
    data = RouteStartedPayload()
# -*- coding: utf-8 -*-
import pulsar, _pulsar
from pulsar.schema import *

from app.broker.commands.command_base import Command

class CreateRoutePayload(Record):
    product_uuid = String()
    product_quantity = String()

class CreateRouteValidate(Command):
    data = CreateRoutePayload()
# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.commands.command_base import Command

class StockValidaterPayload(Record):
    product_uuid = String()
    product_quantity = String()

class CommandStockValidate(Command):
    data = StockValidaterPayload()
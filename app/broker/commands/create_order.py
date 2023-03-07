# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os
import datetime

class Command(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class CreateOrderPayload(Record):
    id_producto = String()
    cantidad_producto = String()
    tipo_orden = String()

class CommandCreateOrder(Command):
    data = CreateOrderPayload()
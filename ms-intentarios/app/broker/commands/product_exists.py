# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os
import datetime

def time_millis():
    return int(time.time() * 1000)

class Command(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class ProductExistsPayload(Record):
    message = String()

class CommandProductExists(Command):
    data = ProductExistsPayload()
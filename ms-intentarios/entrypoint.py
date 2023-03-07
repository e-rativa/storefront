from flask_restful import Api
from flask_cors import CORS
from app import create_app
import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)


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

class StockValidaterPayload(Record):
    product_uuid = String()
    product_quantity = String()

class CommandStockValidate(Command):
    data = StockValidaterPayload()

api = Api(app)
CORS(app)

if __name__ == '__main__':
    app.run()


client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('inventarios',
        consumer_type=_pulsar.ConsumerType.Shared,
        subscription_name='sub_check_inventarios',
        schema=AvroSchema(CommandStockValidate))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value().data)
    print('=========================================')



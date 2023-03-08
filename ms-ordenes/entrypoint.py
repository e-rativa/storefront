from flask_restful import Api
from flask_cors import CORS
from app import create_app
import pulsar, _pulsar
from pulsar.schema import *
import os
import uuid
import time
from app.broker.controllers.command_controller import CommandController

commandController = CommandController()

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

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

class CreateOrderPayload(Record):
    product_uuid = String()
    product_quantity = String()
    order_type = String()

class CommandCreateOrder(Command):
    data = CreateOrderPayload()


class StockValidaterPayload(Record):
    product_uuid = String()
    product_quantity = String()

class CommandStockValidate(Command):
    data = StockValidaterPayload()



if __name__ == '__main__':
    app.run(debug=True)


client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('ordenes',
        consumer_type=_pulsar.ConsumerType.Shared,
        subscription_name='sub_ordenes_creadas',
        schema=AvroSchema(CommandCreateOrder))

consumer_stock = client.subscribe('productos',
        consumer_type=_pulsar.ConsumerType.Shared,
        subscription_name='sub_existencia_productos',
        schema=AvroSchema(CommandStockValidate))

while True:
    msg = consumer.receive()
    

    if msg.topic_name() == 'persistent://public/default/ordenes':
        print('envia el stock')
        orden_data = msg.value().data
        data = {
            'product_uuid' : orden_data.product_uuid,
            'product_quantity' : orden_data.product_quantity,
        }
        commandController.StockCommandValidator(data)

    msg_stock = consumer_stock.recive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg_stock.topic_name())
    print('=========================================')

    if msg_stock.topic_name() == 'persistent://public/default/productos':
        print('productos validos')
        stock_data = msg_stock.value().data
        data = {
            'product_uuid' : stock_data.product_uuid,
            'product_quantity' : stock_data.product_quantity,
        }
        commandController.RouteCommandCreate(data)

client.close()


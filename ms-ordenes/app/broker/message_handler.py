# def message_received(message):
#     print('Mensaje recibido:', message.data())
import pulsar, _pulsar
from pulsar.schema import *
from app.broker.commands.command_config import CommandCreateOrder

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('ordenes',
        consumer_type=_pulsar.ConsumerType.Shared,
        subscription_name='sub_ordenes_creadas',
        schema=AvroSchema(CommandCreateOrder))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.data())
    print('=========================================')

    print('==== Envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()
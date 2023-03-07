from app.broker.commands.create_order import CreateOrderPayload, CommandCreateOrder
from app.broker.dispatcher import Dispatcher
import pulsar
from pulsar.schema import *

dispatcher = Dispatcher()

class CommandController:

    def OrderCommandCreator(self, comando):
        topico = 'ordenes'
        payload = CreateOrderPayload(
            id_producto=str(comando['id_producto']),
            cantidad_producto=str(comando['cantidad_producto']),
            tipo_orden=str(comando['tipo_orden'])
            
        )
        
        comando_integracion = CommandCreateOrder(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topico, AvroSchema(CommandCreateOrder))
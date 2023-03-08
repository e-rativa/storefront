from app.broker.commands.product_exists import ProductExistsPayload, CommandProductExists
from app.broker.dispatcher  import Dispatcher
import pulsar
from pulsar.schema import *

dispatcher = Dispatcher()

class CommandController:

    def ProductCommandExists(self, data):
        topic = 'productos'
        payload = ProductExistsPayload(
            product_uuid=str(data['product_uuid']),
            product_quantity=str(data['product_quantity']),            
        )
        
        comando_integracion = CommandProductExists(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(CommandProductExists))
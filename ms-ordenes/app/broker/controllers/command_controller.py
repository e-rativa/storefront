


from app.broker.commands.stock_validate import StockValidaterPayload, CommandStockValidate
from app.broker.dispatcher  import Dispatcher
import pulsar
from pulsar.schema import *

dispatcher = Dispatcher()

class CommandController:

    def StockCommandValidator(self, data):
        topic = 'inventarios'
        payload = StockValidaterPayload(
            product_uuid=str(data['product_uuid']),
            product_quantity=str(data['product_quantity']),            
        )
        
        comando_integracion = CommandStockValidate(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(CommandStockValidate))
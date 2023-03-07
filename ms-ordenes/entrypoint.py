from flask_restful import Api
from flask_cors import CORS
from app import create_app
from app.broker.message_handler import message_received

import os

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

# client = pulsar.Client('pulsar://localhost:6650')
# consumer = client.subscribe('ordenes',
#         consumer_type=_pulsar.ConsumerType.Shared,
#         subscription_name='sub_ordenes_creadas')

# while True:
#     msg = consumer.receive()
#     print('=========================================')
#     print("Mensaje Recibido: '%s'" % msg.value().data)
#     print('=========================================')

#     print('==== Envía correo a usuario ====')

#     consumer.acknowledge(msg)

# client.close()


if __name__ == '__main__':
    app.run(debug=True)
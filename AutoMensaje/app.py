from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from answer import reserva, menu, horario, redes_sociales

app = Flask(__name__)

# Lista para almacenar las reservas
reservations = []
users = {}

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From')
    response = MessagingResponse()
    message = response.message()

    if from_number not in users:
        users[from_number] = {"state": "initial"}
        message.body('Bienvenido a nuestro restaurante. Por favor, selecciona una opción: \n1. Reservar \n2. Menú \n3. Horario \n4. Redes Sociales')
    else:
        user = users[from_number]
        state = user["state"]

        if state == "initial":
            if "reservar" in incoming_msg:
                user["state"] = "reservar"
                reserva(user, incoming_msg, message, reservations)
            elif "menú" in incoming_msg or "menu" in incoming_msg:
                user["state"] = "menu"
                menu(message)
                users.pop(from_number)
            elif "horario" in incoming_msg:
                user["state"] = "horario"
                horario(message)
                users.pop(from_number)
            elif "redes sociales" in incoming_msg:
                user["state"] = "redes sociales"
                redes_sociales(message)
                users.pop(from_number)
            else:
                message.body('Opción no válida. Por favor, selecciona una opción: \n1. Reservar \n2. Menú \n3. Horario \n4. Redes Sociales')

        elif state == "reservar":
            reserva(user, incoming_msg, message, reservations)

    return str(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

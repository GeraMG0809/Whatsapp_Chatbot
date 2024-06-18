from twilio.twiml.messaging_response import MessagingResponse

def reserva(user, incoming_msg, message, reservations):
    state = user["state"]

    if state == "reservar":
        user["state"] = "name"
        message.body('Por favor, indícanos tu nombre para comenzar la reserva.')
    elif state == "name":
        user["name"] = incoming_msg
        user["state"] = "person"
        message.body(f'Hola {user["name"]}, por favor indícanos la cantidad de personas que asistirán.')
    elif state == "person":
        user["person"] = incoming_msg
        user["state"] = "date"
        message.body('Por favor, indícanos la fecha de tu reserva (DD/MM/YYYY).')
    elif state == "date":
        user["date"] = incoming_msg
        user["state"] = "time"
        message.body('Gracias. Ahora, indícanos la hora de tu reserva (HH:MM).')
    elif state == "time":
        user["time"] = incoming_msg
        user["state"] = "confirmed"
        message.body(f'Tu reserva está casi lista. Nombre: {user["name"]}, Fecha: {user["date"]}, Hora: {user["time"]}, Personas: {user["person"]}. Por favor, confirma que esta información es correcta respondiendo "sí" o "no".')
    elif state == "confirmed":
        if incoming_msg in ['sí', 'si', 'sí', 'sI', 'SI']:
            reservations.append(user)
            message.body('¡Reserva confirmada! Te esperamos en nuestro restaurante.')
        else:
            message.body('Lo siento, por favor comienza de nuevo enviando "reservar".')
        user["state"] = "initial"

def menu(message):
    message.body("Somos un restaurante de comida italiana y griega.")

def horario(message):
    message.body("Nuestro horario es de Lunes a Sábado de 10:00am a 10:00pm, los Domingos descansamos.")

def redes_sociales(message):
    message.body("Síguenos en nuestras redes sociales para más información y promociones.")

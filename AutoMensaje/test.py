import pywhatkit as kit

# Asegúrate de incluir el código de país en el número de teléfono
phone_number = "+523327476525"
message = "hello world"

# Enviar el mensaje de inmediato
kit.sendwhatmsg_instantly(phone_number, message)

print("Mensaje enviado")

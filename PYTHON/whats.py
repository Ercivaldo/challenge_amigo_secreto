import pywhatkit

numero_telefone = "+5511999999999"  # Número no formato internacional
mensagem_telefone = "Olá, teste"    # Texto da mensagem

# Envia a mensagem instantaneamente
pywhatkit.sendwhatmsg_instantly(numero_telefone, mensagem_telefone)



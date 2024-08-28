import base64

# El string que quieres convertir
input_string = "HolaMundo"

# Convertir el string a bytes
input_bytes = input_string.encode("utf-8")

# Codificar en base64
base64_bytes = base64.b64encode(input_bytes)

# Convertir el resultado de bytes a string
base64_string = base64_bytes.decode("utf-8")

print("String original:", input_string)
print("String en base64:", base64_string)

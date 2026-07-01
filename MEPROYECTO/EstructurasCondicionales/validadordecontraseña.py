contrasena = "Python3.9!"
largo_suficiente = len(contrasena) >= 8
tiene_mayuscula = any(c.isupper() for c in contrasena)
tiene_numero = any(c.isdigit() for c in contrasena)
tiene_especial = any(not c.isalnum() for c in contrasena)
if largo_suficiente and tiene_mayuscula and tiene_numero and tiene_especial:
    print("Contraseña válida: cumple todos los criterios de seguridad")
else:
    print("Contraseña inválida: no cumple con los criterios")
from datetime import datetime
hora_actual = datetime.now().hour
NOMBRE = "Sergio"
if 23 <= hora_actual < 12:
    print(f"¡Buenos días, {NOMBRE}!")
elif 12 <= hora_actual < 20:
    print(f"¡Buenas tardes, {NOMBRE}!")
else:
    print(f"¡Buenas noches, {NOMBRE}!")
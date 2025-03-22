informacion_personal = {
    "nombre": "Flor Muñoz",
    "edad": 23,
    "ciudad": "Guayaquil",
    "profesion": "Ingeniero"
}

informacion_personal["ciudad"] = "Guayaquil"

informacion_personal["profesion"] = "Desarrollador de Software"

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0994979401"

del informacion_personal["edad"]

print(informacion_personal)
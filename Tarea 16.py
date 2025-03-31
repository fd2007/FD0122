# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    file.write("Primera nota: Me gusta mucho ir a la iglesia los domingos.\n")
    file.write("Segunda nota: Siempre practico lectura de la Biblia.\n")
    file.write("Tercera nota: Mi mayor pasa tiempo favorito es dormir.\n")

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    for line in file:  # Lee el archivo línea por línea
        print(line.strip())  # Muestra cada línea sin el salto de línea extra

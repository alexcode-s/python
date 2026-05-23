import pickle

datos = {
    "nombre": "Ana",
    "edad": 25,
    "notas": [7.5, 8.0, 9.2]
}

# Guardar un fichero
with open("datos.pkl", "wb") as f:
    pickle.dump(datos, f)

# Guardar varios objetos
with open("datos.pkl", "wb") as f:
    pickle.dump(10, f)
    pickle.dump([1, 2, 3], f)

# Cargar un objeto
with open("datos.pkl", "rb") as f:
    datos = pickle.load(f)

# Cargar varios objetos
with open("datos.pkl", "rb") as f:
    a = pickle.load(f)
    b = pickle.load(f)

# Ejemplo completo

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30}
]

with open("personas.pkl", "wb") as f:
    pickle.dump(personas, f)

with open("personas.pkl", "rb") as f:
    personas_cargadas = pickle.load(f)

print(personas_cargadas)

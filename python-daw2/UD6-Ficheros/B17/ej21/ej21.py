import re

# Configuración de nombres de ficheros
entrada = "pokemon_in.txt"
salida = "pokemon_out.txt"

def validar_pokemon(pokemon_str):
    """
    Valida un solo pokemon y devuelve (True, error) o (False, mensaje)
    """
    # Expresión regular:
    # ^\s*(\d+)\s+      -> Empieza por espacios opcionales, luego dígitos (grupo 1) y espacio
    # ([a-zA-Z\s\.]+)$  -> Sigue con letras, espacios o puntos (grupo 2) hasta el final
    match = re.match(r"^\s*(\d+)\s+([a-zA-Z\s\.]+)$", pokemon_str)

    if not match:
        return False, f"Formato inválido en '{pokemon_str}' (números o símbolos no permitidos)"

    numero = int(match.group(1))
    nombre = match.group(2).strip()

    # Validación del rango de la Pokedex
    if numero < 1 or numero > 151:
        return False, f"Número {numero} fuera de la 1ª generación (1-151)"

    return True, ""


def procesar_pokedex():
    total_pokemons_correctos = 0
    lineas_validas = []

    try:
        with open(entrada, "r", encoding="utf-8") as f_in:
            for linea in f_in:
                linea = linea.strip()
                if not linea: continue  # Saltamos líneas vacías

                # Separamos los pokemons de la línea
                partes = linea.split("; ")

                # 1. Validación: Máximo 3 pokemons por línea
                if len(partes) > 3:
                    print(f"Línea errónea detectada: {linea}")
                    print("Motivo: Más de 3 pokemons en la línea evolutiva")
                    continue

                # 2. Validar cada pokemon individualmente en la línea
                error_en_linea = False
                for p in partes:
                    es_valido, motivo = validar_pokemon(p)
                    if not es_valido:
                        print(f"Línea errónea detectada: {linea}")
                        print(f"Motivo: {motivo}")
                        error_en_linea = True
                        break  # Si uno falla, toda la línea se descarta

                # 3. Si toda la línea es correcta, guardamos
                if not error_en_linea:
                    lineas_validas.append(linea)
                    total_pokemons_correctos += len(partes)

        # Escritura de resultados
        with open(salida, "w", encoding="utf-8") as f_out:
            for l in lineas_validas:
                f_out.write(l + "\n")

        print(f"\nSe han grabado {total_pokemons_correctos} pokemons correctos en el fichero de salida")

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {entrada}")


# Ejecución del programa
procesar_pokedex()
## JACKSON ARTURO VASQUEZ CASTRO

#!/usr/bin/env python

import sys

# Variables para almacenar la clave y los gastos actuales
current_key = None
current_gastos = []

# Itera sobre las líneas de entrada
for line in sys.stdin:
    # Elimina espacios en blanco y divide los campos
    line = line.strip()
    
    # Verificar si la línea tiene el formato esperado
    if "\t" in line:
        key, gasto = line.split("\t")
        
        # Verificar si los valores son numéricos
        try:
            gasto = int(gasto)
        except ValueError:
            # Manejar errores si el valor de gasto no es un número
            print(f"ERROR: Valor no numérico en la línea: {line}", file=sys.stderr)
            continue
        
        # Si la clave actual coincide con la clave anterior, agrega el gasto a la lista
        if key == current_key:
            current_gastos.append(gasto)
        else:
            # Si la clave ha cambiado, emite la moda para la clave anterior
            if current_key:
                moda = max(set(current_gastos), key=current_gastos.count)
                print(f"{current_key}\t{moda}")
            current_key = key
            current_gastos = [gasto]

# Emite la moda para la última clave
if current_key:
    moda = max(set(current_gastos), key=current_gastos.count)
    print(f"{current_key}\t{moda}")


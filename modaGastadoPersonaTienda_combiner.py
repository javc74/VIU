## JACKSON ARTURO VASQUEZ CASTRO

#!/usr/bin/env python

import sys

current_key = None
current_gastos = []

# Itera sobre las líneas de entrada
for line in sys.stdin:
    # Elimina espacios en blanco y divide los campos
    line = line.strip()
    key, gasto = line.split("\t")
    
    # Si la clave actual coincide con la clave anterior, agrega el gasto a la lista
    if key == current_key:
        current_gastos.append(int(gasto))
    else:
        # Si la clave ha cambiado, emite la moda para la clave anterior
        if current_key:
            moda = max(set(current_gastos), key = current_gastos.count)
            print(f"{current_key}\t{moda}")
        current_key = key
        current_gastos = [int(gasto)]

# Emite la moda para la última clave
if current_key:
    moda = max(set(current_gastos), key = current_gastos.count)
    print(f"{current_key}\t{moda}")

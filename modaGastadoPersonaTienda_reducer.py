## JACKSON ARTURO VASQUEZ CASTRO

#!/usr/bin/env python

import sys

current_key = None
current_gastos = []

for line in sys.stdin:
    line = line.strip()
    key, gasto = line.split("\t")
 
    if key == current_key:
        current_gastos.append(int(gasto))
    else:
        if current_key:
            # Calculamos la moda para la clave actual
            moda = max(set(current_gastos), key=current_gastos.count)
            print(f"{current_key}\t{moda}")
        current_key = key
        current_gastos = [int(gasto)]

if current_key:
    moda = max(set(current_gastos), key=current_gastos.count)
    print(f"{current_key}\t{moda}")

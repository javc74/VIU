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
            # Emitimos la suma de los gastos para la clave actual
            print(f"{current_key}\t{sum(current_gastos)}")
        current_key = key
        current_gastos = [int(gasto)]

if current_key:
    print(f"{current_key}\t{sum(current_gastos)}")



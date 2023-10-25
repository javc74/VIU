## JACKSON ARTURO VASQUEZ CASTRO

#!/usr/bin/env python

import sys

# Variables para almacenar la clave y la moda actual
current_key = None
current_moda = None

# Itera sobre las líneas de entrada
for line in sys.stdin:
    # Elimina espacios en blanco y divide los campos
    line = line.strip()
    
    # Verificar si la línea tiene el formato esperado
    if "\t" in line:
        key, moda = line.split("\t")
        
        # Si la clave actual coincide con la clave anterior, actualiza la moda
        if key == current_key:
            current_moda = moda
        else:
            # Si la clave ha cambiado, emite el resultado para la clave anterior
            if current_key:
                print(f"{current_key}\t{current_moda}")
            current_key = key
            current_moda = moda

# Emite el resultado para la última clave
if current_key:
    print(f"{current_key}\t{current_moda}")

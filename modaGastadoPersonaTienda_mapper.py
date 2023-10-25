## JACKSON ARTURO VASQUEZ CASTRO

#!/usr/bin/env python

import sys


# Itera sobre las líneas de entrada
for line in sys.stdin:
    # Elimina espacios en blanco y divide los campos
    line = line.strip()
    
    # Verificar si la línea tiene el formato esperado
    if ";" in line:
        persona, tienda, gasto = map(str.strip, line.split(";"))
        
        # Emitir clave: persona+tienda, valor: gasto
        print(f"{persona};{tienda}\t{gasto}")
    else:
        # Manejar líneas que no cumplen con el formato esperado
        print(f"ERROR: Formato inválido en la línea: {line}", file=sys.stderr)
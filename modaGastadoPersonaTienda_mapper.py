## JACKSON ARTURO VASQUEZ CASTRO

#!/usr/bin/env python

import sys

# Itera sobre las líneas de entrada
for line in sys.stdin:
    # Elimina espacios en blanco y divide los campos
    line = line.strip()
    persona, tienda, gasto = line.split(";")
    # Emitir clave: persona+tienda, valor: gasto
    print(f"{persona};{tienda}\t{gasto}")

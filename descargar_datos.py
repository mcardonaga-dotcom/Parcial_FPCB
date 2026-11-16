"""Descarga las estimaciones de carga de tuberculosis de la OMS (WHO TB burden estimates).

Fuente: https://www.who.int/teams/global-tuberculosis-programme/data (pestaña "CSV files").
Si el enlace directo deja de funcionar, descargue el archivo manualmente desde esa página
y guárdelo en la carpeta datos/.
"""
import os
from datetime import date

import pandas as pd

URL = "https://extranet.who.int/tme/generateCSV.asp?ds=estimates"

os.makedirs("datos", exist_ok=True)
tb = pd.read_csv(URL)
ruta = f"datos/TB_burden_countries_{date.today().isoformat()}.csv"
tb.to_csv(ruta, index=False)
print(f"Se guardaron {tb.shape[0]} registros y {tb.shape[1]} columnas en {ruta}")
print("Si usa este archivo nuevo, actualice su nombre en la primera celda de código del cuaderno.")

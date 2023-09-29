import pandas as pd

archivos = ['/content/MedalleroOlímpicos.xlsx', '/content/MedalleroPanamericanos.xlsx']

dfs = [pd.read_excel(archivo) for archivo in archivos]
print(dfs)

resultado = pd.concat(dfs)
resultado.to_excel('MedalleroFinal.xlsx', index=False)
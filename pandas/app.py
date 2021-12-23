import pandas as pd
# Abrir documento excel
# df = pd.read_excel('../xls/ejemplo.xls', sheet_name='Hoja1')

# print(df.head(6))

# Graficar datos de excel
import matplotlib.pyplot as plt
work = "../xls/ejemplo.xls"
df = pd.read_excel(work, sheet_name='Hoja1')
# print(df.head(6))
values = df[['cursos', 'creditos']]
# print(values)
a = values.plot.bar(x='cursos', y='creditos', rot=0)
plt.show()
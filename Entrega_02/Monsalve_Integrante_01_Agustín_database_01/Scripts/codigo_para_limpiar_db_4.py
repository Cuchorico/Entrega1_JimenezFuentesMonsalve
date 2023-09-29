values ={"Año":[2020 , 2021 , 2022],"Deporte competitivo":[646579000 , 20521872000 , 22721155545],"Total":[2653804000 , 129552031000 , 217638105467]}

Gastos_IND = pd.DataFrame(values)
Gastos_IND["% del gasto total"]= Gastos_IND["Deporte competitivo"]/Gastos_IND["Total"]*100

Gastos_IND<
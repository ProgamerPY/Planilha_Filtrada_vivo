import pandas as pd 

vivo = pd.read_excel("Vendas.xlsx")

SelectColum = vivo[vivo["Serviço"].isin(["Seguro"])]

vivo = vivo[["Data","CPF","Serviço"]]

vivo.to_excel("Victor.xlsx")

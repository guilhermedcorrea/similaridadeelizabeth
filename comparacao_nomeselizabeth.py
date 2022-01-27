import pandas as pd
from itertools import zip_longest
from fuzzywuzzy import fuzz

def identifica_elementos(elizabeth, hausz):

    for x, y in zip_longest(elizabeth, hausz):

        ident = fuzz.ratio(x, y)
        refhausz = x
        refelizabeth = y
        ref = ident
        if type(refelizabeth) == str and ref > 40:
            print(ref, 'elizabeh ~>',refelizabeth,"Hausz",refhausz)


def remove_nomes(elementos):
    ajustados = []
    for elemento in elementos:
        valor = str(elemento).split()
        valor = valor[3:-11]
        x = " ".join(valor).lower().replace("hd polido","").replace("hd","").replace("cx2,02","").replace("esmaltado",
        "").replace("polido","").replace("escovado","").replace("nv","").replace(" ","").strip()
        ajustados.append(x)
    return ajustados
        

def ajuste_referencia(elementos):
    ajustados = []
    for elemento in elementos:
        valor = str(elemento).lower().replace(",",".").replace("_s","").replace("_sc","").replace("_",
        " ").replace("porcelanato","").replace("porcelanato ","").replace("pb","").replace(" ","").strip()
        ajustados.append(valor)
    return ajustados


df_hausz = pd.read_excel("D:\\Trabalhos Python\\hauszelizabeth.xlsx")
df_hausz["Produto"] = remove_nomes(df_hausz["Produto"])

df_elizabeth = pd.read_excel("D:\\Trabalhos Python\\fotoselizabethaltaresolucao.xlsx")
df_elizabeth["Referencia"] = ajuste_referencia(df_elizabeth["Referencia"])



lista_hausz = df_hausz["Produto"].tolist()

lista_elizabeth = df_elizabeth["Referencia"].tolist()

valores = identifica_elementos(lista_elizabeth, lista_hausz)
#ESERCIZI SULLE FUNZIONI:
def rewrite_dict(d:dict[str, int]) -> dict[str ,int]:
    somma = sum(list(d.values()))
    print(f"la somma è {somma}")
    d1 = {}
    for k in d:
        d1[k] = d[k]/somma
    return d1
d ={"scarpe":10, "vestito":30 , "occhiali":20}
out = rewrite_dict(d)
print(out)
#esempio di funzine con i dizionari

#definisci una funzione substract che prende due parametri e poi ritorna il risultato

def substract(z:int , y:int):
    a:int = z-y
    return a
out = substract (8,4)
print(out)

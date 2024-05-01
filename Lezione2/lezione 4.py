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

#
def median(l:list[float]) -> float:
    l= sorted(l)#dopoaverdefinitolafunzioneho ordinato la lista
    mid = len(l) //2
    if len(l)%2!=0:#(ildispari)
        print("la mia lista ha lunghezza disapri")
        mediana = l[mid]
    else:#(il pari)
        print("la mia lista ha lungheza pari")
        mediana = (l[mid] + l[mid -1]) /2

    return mediana
l=[2,9,0,-2,25,2,4]
mediana = median(l)
print(f"la mediana della lista{l} è {mediana}")

#fare una funzione dove prendo un sequenza cumulativa
def diff_cum(l:list[float]):
    x = l[0]
    for i in l[1:]:
        x = x-i
    return x
l=[1,2,3,4,5,6]
print(f'La differenza cumulativa è {diff_cum(l)}')

#esercizi per casa sulla lezione 4:

#8-1):


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
def display_message() -> str:
    message: str ="in this lessons i'm lernig about function"
    return message


print(display_message())

#8.2)
def favorite_book(title:str)-> str:
    print(f"one of my favorite book is'{title}")

title:str = "Frankestein"
favorite_book(title)

#8.3)
def make_shirt(size:str ,text:str)-> str:
    print(f"the tshirt be a size{size} and can read in that a text'{text}'.")

size:str = "S"
text:str= "Always darling"    
make_shirt(size,text)


def make_shirt2(size: str ,text: str)-> str:
    print(f"the tshirt be a size{size} and can read in that a text'{text}'.")

make_shirt2(size =  "M" ,text = "Always" )

#8.4)
def make_shirt3(size:str ="L" ,text:str = "i love python")-> str:
 print(f"the tshirt be a size{size} and can read in that a text'{text}'.")
 print(f"the tshirt be a size M and can read in that a text'{text}'.")
 print(f"the tshirt be a size S and can read in that a text'i hate python'.")


make_shirt3()

#8.5)
def describe_city(name:str,country:str ="united states of america") -> str:
     print(f"{name} ,{country}")    

describe_city(name= "NewYork")
describe_city(name= "LasVegas")
describe_city(name= "SanFrancisco")

#8.6)
def describe_country(name:str,country:str ) -> str:
     print(f"{name} ,{country}")    

describe_country(name= "NewYork" , country = "U.S.A")
describe_country(name= "Milan" , country = "Italy")
describe_country(name= "Paris" , country = "France")

#8.7)
def make_album(artist:str,title:str,song:int ) -> dict:
    album:dict = {
    "artist":artist,
    "title":title,
    "song":song
    }
    print(album)

make_album(artist="Pantera",title="walk",song=None )
make_album(artist="GreenDay",title="21guns",song=None )
make_album(artist="Nirvana",title="nevermind",song=None )
make_album(artist="Metallica",title="master of puppets",song=16 )

#8.8)
"""

def make_album2(album:dict) -> dict:
    print(album)

album: dict ={
     "artist":"",
     "title":"",
    }
for keyword in album :
    album[keyword] = input(f"{keyword}:")
make_album2(album)
"""

#8.9)
def show_messages(messages:list[str] ) -> str:
    for elem in messages:   
        print(elem)  

messages:list[str]=["goodmornig how are you?"
                   "are you ok?"
                   "i love you" ]
show_messages(messages)

#8.10-11)
def sent_messages(messages:list[str]) -> str:
    sent_messages:list[str]=[]
    i:int = 0
    while i in range(len(messages)):
        print(messages[i])
        sent_messages.append(messages[i])
    print(messages)
    print(sent_messages)

    messages2:list[str] =["goodmornig how are you?"
                          "are you ok?"
                        "i love you"]
    sent_messages(messages2)

#8.12)
def sandiwiches(*args ) -> list[str]:
    print(args)

sandiwiches("egg","ham","mayo" )
sandiwiches("bacon","egg","chese" )
sandiwiches("turkey","mayo","tomato" )

#8.3)
def sent_messages(first_name:str, last_name:str ,age:int, hair_colour:str, eye_colour:str) -> str:
    print(f"{first_name} {last_name} ,age {age}, hair{hair_colour} eye {eye_colour}") 

first_name: str = "MariaPaola"
last_name: str  = "Bongiorno"
age: int = 30
hair_colour: str = "blonde"
eye_colour: str  = "green"


#8.14)
def car_info(manufacturer:str,model:str,**kwargs ) -> dict:
    dictionary:dict = {"manifacture": manufacturer,
                       "model" :model, 
                       }
    if len(kwargs) > 0:
       for keyword in kwargs:
           dictionary.update({keyword : kwargs[keyword]})
    print(dictionary)

manufacturer:str = "audi"
model:str ="tt"
car_info(manufacturer ,model,colour = "red", two_package = True)



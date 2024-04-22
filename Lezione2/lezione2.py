#Maria Paola Bongiorno
#22/04/2024


#2.3)usa una variabile per rappresentare un nome di una persona, stampa il messaggio della persona
name :str = "Mary"
print("ciao ti và di mparare un pò di python insieme?")
#oppure ,così in cui la variabile contiene il messaggio
message: str = f"ciao{name}, ti và di imparare un pò di python insieme?"

#2.4)
name: str ="luca"
name_lower: str = name.lower()
name_upper: str = name.upper()
print( f" {name}, {name.lower} ,{name.upper}")



#2.5)
autore :str='Giuliocesare'
frase = "quoue tu bruts fili mi"
print(frase)

#2.6)
famousperson:str="famousperson"
message = "piange il telefono"
print(message)

#2.8)
filename:str ="prova.txt"
print(filename.removesuffix(".txt"))

#3.1)
name =["luca","elena","gino" , "giuseppe"]
print(name[0])
print(name[1])
print(name[2])
print(name[3])

#3.2)
print("ciao best " , name[0] , "come stai?")
print("ciao tata", name[1] ,"stai andado a casa?")
print("ciao bello" , name[2] , "vieni al cinema?")
print("ciao splendore" , name[3] , "vieni dal paninaro stasera?")

#3.3)
car :list =["Mercedes","Ferrari","Lamborghini","Maserati"]
message :list= ["vorreiguidare una", "mi piacerebbe avere una","mi piacerebbe comprarne una","desidero una"]
print(message[0] , car[0])

#3.4)
guests : list =["Terenzio" ,"Fabrizio" , "Annibale", "Marco"]
for name in guests:
    print(name, " vieni a cena?")


#3.5)
print("Terenzio")
guests[0]= "Tommaso"

for name in guests :
    print(name, " vieni a cena?")

#3.6)
print("ragazzi ho trovato un tavolo più grande")
guests.insert(0, "Cesare")
guests.insert(2, "Nerone")
guests.append("Caio")
invitations:list=[]
invitations.insert(0,"Sono felice di invitarti a cena")
invitations.insert(2,"Sono contenta di invitarti a cena")
invitations.append("Sono molto lieta di invitarti a cena")
for i in range(len(invitations)): 
   print(f"cari{guests[i]},{invitations[i]}, saluti")
#3.7
print( "Salveospitia causa di un problema possiamo ricevere solo due ospiti a cena")

for i in range(4):
    print(f"{guests[i]} , sono spiacente di dirvi che la cena è rimandata")                
guests.pop(0)
guests.pop(0)
guests.pop(0)
guests.pop(0)
for i in range(len(guests)):    
  print(f"cari,{guests[i]} , sono lieta di informarvi che siete invitati tuttavia a cena la prossima settimana") 

del guests[0:2]
print(guests)

#3.8)
locations :list =["Cina","Corea", "Canada","Usa","India"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations , reverse= True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)

#3.9)
guests:list=["Tommaso","Cesare","Nerone","caio"]
print(f"siete invitati voi {len(guests)} a cena")


#3.10)
languages :list =["Inglese","Coreano", "Giapponese","Indiano"]
print(languages)
languages.append("italiano")
print(languages)
languages.pop(2)
print(languages)
languages.remove("Coreano")
print(languages)
print(sorted(languages))
print(languages)
languages.sort(reverse=True)
print(languages)
languages.insert(1,"Cinese")
print(languages)

#6.1)
person:dict={"Nome":"Cesare",
             "cognome":"Vaccaro",
             "Età":"90",
             "città":"Pistoia"}
for key in person:
   print(person[key])

#6.2)
   favoritenumbers:dict={"Luca":24,
             "Astolfo":5,
             "Eurialo":90,
             "Teseo":18,
             "Achille":22}
for key in favoritenumbers:
   print(f"person:{key},favoritenumbers:{favoritenumbers[key]}")

#6.7
secondperson:dict={"Nome":"Cesarione",
             "cognome":"Vaccaro",
             "Età":"80",
             "città":"Pedara"}
thirdperson:dict={"Nome":"Mia",
             "cognome":"Vajakuk",
             "Età":"77",
             "città":"Perugia"}
people:list=[person,secondperson,thirdperson]
for i in people:
   print(i) 
       
#6.8)     
   firstpet:dict={"Animal":"dog",
             "nome":"Astolfo",
             "proprietario":"Eurialo"}            
secondpet:dict={"animal":"pappagallo",
             "nome":"Vanesio",
             "proprietario":"Alcide",}
thirdpet:dict={"animale":"gatto",
             "nome":"Vakuk",
             "proprietario":"Leuca",}
fourthpet:dict={"animale":"topo",
             "nome":"topolino",
             "proprietario":"Lucrezio",}
pets:list=[firstpet,secondpet,thirdpet,fourthpet]
for i in pets:
   print(i) 

#6.9)
   favorite_places:dict={"Terens":"Viterbo",
                        "Luca":"Torino",
                        "Odi":"Lucca",}
for key in favorite_places:
   print(f"{key}:{favorite_places[key]}")

#6.10
   favoritenumbers:dict={"Luca":("24and9"),
                        "Astolfo":("5and22"),
                        "Eurialo":("8and44"),
                        "Teseo":("18and7"),}
for key in favoritenumbers:
    print(f"person:{key},favoritenumbers:{favoritenumbers[key]}")
   #chiedere al prof questo esrcizio su come scrivere due numeri nei diz prima di consegna


#6.11)     
Milan:dict={"country":"Italy",
             "population":"1 372 580  of peoples",
             "fact":"founded by Celts"}    
Paris:dict={"country":"France",
             "population":"2 229 095  of peoples",
             "fact":"hosted two editions of the Olympic Games (1900 and 1924)"} 
London:dict={"country":"England",
             "population":"8 799 800  of peoples",
             "fact":"it has nine aiports"} 
Cities:dict={"Milan":Milan,
             "Paris":Paris,
             "London":London} 
for key in Cities:
          print(f"{key} :{Cities[key]}")                 













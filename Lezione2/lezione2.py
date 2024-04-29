#Maria Paola Bongiorno
#esercizi lezione 2:


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

#ESERCIZI LEZIONE 3:
#4-1e4.11
# List of favorite pizzas
favorite_pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]

# Copying the list of favorite pizzas to friend_pizzas
friend_pizzas = favorite_pizzas[:]

# Adding a new pizza to the original list
favorite_pizzas.append("Vegetarian")

# Adding a different pizza to the friend_pizzas list
friend_pizzas.append("Hawaiian")

# Printing a sentence for each pizza in the favorite_pizzas list
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("I like", pizza, "pizza.")

# Printing a sentence for each pizza in the friend_pizzas list
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("My friend likes", pizza, "pizza.")

# Statement about loving pizza
print("\nI really love pizza!")

#4-2
# List of animals with a common characteristic
animals = ["dog", "cat", "rabbit"]

# Print the name of each animal using a for loop
print("Animals:")
for animal in animals:
    print(animal)

# Print a statement about each animal
print("\nStatements about each animal:")
for animal in animals:
    print(f"A {animal} would make a great pet.")

# Print what these animals have in common
print("\nCommon characteristic:")
print("Any of these animals would make a great pet.")

#4-3
# Print numbers from 1 to 20 using a for loop
for num in range(1, 21):
    print(num)

#4-4
#Print numbers from 1 to 1 million using a for loop:
for num in range(1, 1000001):
    print(num)


4-5
# Verify the range of numbers from 1 to 1 million using min() and max()
start = 1
end = 1000000
print("Start of the range:", min(range(start, end + 1)))
print("End of the range:", max(range(start, end + 1)))

# Calculate the sum of numbers from 1 to 1 million using sum()
total_sum = sum(range(start, end + 1))
print("Sum of numbers from 1 to 1 million:", total_sum)

#4-7
# Make a list of odd numbers from 1 to 20 using range() with a step of 2
odd_numbers = list(range(1, 21, 2))

# Print each odd number using a for loop
for number in odd_numbers:
    print(number)

4-8
# Make a list of the first 10 cubes
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)

# Print out the value of each cube
for cube in cubes:
    print(cube)

#4-9
# Generate a list of the first 10 cubes using list comprehension
cubes = [num ** 3 for num in range(1, 11)]

# Print out the value of each cube
for cube in cubes:
    print(cube)

4-10
# Generate a list of the first 10 cubes using list comprehension
cubes = [num ** 3 for num in range(1, 11)]

# Print out the value of each cube
for cube in cubes:
    print(cube)

# Print the first three items in the list
print("The first three items in the list are:", cubes[:3])

# Print three items from the middle of the list
middle_index = len(cubes) // 2
print("Three items from the middle of the list are:", cubes[middle_index:middle_index + 3])

# Print the last three items in the list
print("The last three items in the list are:", cubes[-3:])

#4-12
# Define the lists of foods
fruits = ['apple', 'banana', 'orange', 'grape']
vegetables = ['carrot', 'broccoli', 'spinach', 'kale']
desserts = ['cake', 'ice cream', 'cookies', 'pie']

# Print the list of fruits
print("Fruits:")
for i in range(len(fruits)):
    print(fruits[i])

# Print the list of vegetables
print("\nVegetables:")
for i in range(len(vegetables)):
    print(vegetables[i])

# Print the list of desserts
print("\nDesserts:")
for i in range(len(desserts)):
    print(desserts[i])


4-15
#1
cubes:list
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)

#2
for num in range(1, 21):
    print(num)

#3

for number in odd_numbers:
    print(number)


#4-16
# Test 1: Checking if 5 is equal to 5
print("Is 5 == 5? I predict True.")
print(5 == 5)

# Test 2: Checking if 'apple' is equal to 'banana'
print("\nIs 'apple' == 'banana'? I predict False.")
print('apple' == 'banana')

# Test 3: Checking if 10 is not equal to 20
print("\nIs 10 != 20? I predict True.")
print(10 != 20)

# Test 4: Checking if 15 is greater than 10
print("\nIs 15 > 10? I predict True.")
print(15 > 10)

# Test 5: Checking if 30 is less than or equal to 30
print("\nIs 30 <= 30? I predict True.")
print(30 <= 30)

# Test 6: Checking if 'dog' is in ['cat', 'dog', 'rabbit']
print("\nIs 'dog' in ['cat', 'dog', 'rabbit']? I predict True.")
print('dog' in ['cat', 'dog', 'rabbit'])

# Test 7: Checking if 'orange' is not in ['apple', 'banana', 'grape']
print("\nIs 'orange' not in ['apple', 'banana', 'grape']? I predict True.")
print('orange' not in ['apple', 'banana', 'grape'])

# Test 8: Checking if (5 + 3) equals 7
print("\nIs (5 + 3) == 7? I predict False.")
print((5 + 3) == 7)

# Test 9: Checking if (6 * 2) is less than or equal to 12
print("\nIs (6 * 2) <= 12? I predict True.")
print((6 * 2) <= 12)

# Test 10: Checking if 'pear' is equal to 'pear'
print("\nIs 'pear' == 'pear'? I predict True.")
print('pear' == 'pear')

#4-17
# Test 1: Equality test with strings
print("Is 'apple' == 'apple'? I predict True.")
print('apple' == 'apple')

# Test 2: Inequality test with strings
print("\nIs 'banana' != 'orange'? I predict True.")
print('banana' != 'orange')

# Test 3: Numerical test for greater than
print("\nIs 10 > 5? I predict True.")
print(10 > 5)

# Test 4: Numerical test for less than
print("\nIs 20 < 30? I predict True.")
print(20 < 30)

# Test 5: Test using the and keyword
print("\nIs (10 > 5) and (20 < 30)? I predict True.")
print((10 > 5) and (20 < 30))

# Test 6: Test using the or keyword
print("\nIs (10 < 5) or (20 < 30)? I predict True.")
print((10 < 5) or (20 < 30))

# Test 7: Test whether an item is in a list
pets = ['dog', 'cat', 'rabbit']
print("\nIs 'cat' in pets? I predict True.")
print('cat' in pets)

# Test 8: Test whether an item is not in a list
print("\nIs 'bird' not in pets? I predict True.")
print('bird' not in pets)

# Test 9: Test using the lower() method
word = 'HELLO'
print("\nIs word.lower() == 'hello'? I predict True.")
print(word.lower() == 'hello')

# Test 10: Test using the lower() method for inequality
print("\nIs word.lower() != 'hello'? I predict False.")
print(word.lower() != 'hello')

#5-6

age = 30

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

#5-7
favorite_fruits = ['apple', 'banana', 'mango']

if 'apple' in favorite_fruits:
    print("You really like Apples!")

if 'banana' in favorite_fruits:
    print("You really like Bananas!")

if 'orange' in favorite_fruits:
    print("You really like Oranges!")

if 'mango' in favorite_fruits:
    print("You really like Mangoes!")

if 'strawberry' in favorite_fruits:
    print("You really like Strawberries!")

#5-10
# List of current users
current_users = ['john', 'mary', 'alex', 'jane', 'bob']

# List of new users
new_users = ['alex', 'sarah', 'mike', 'jOHN', 'emily']

# Convert current_users to lowercase
current_users_lower = [user.lower() for user in current_users]

# Loop through new_users to check for uniqueness
for user in new_users:
    # Convert user to lowercase for case-insensitive comparison
    user_lower = user.lower()
    # Check if user_lower exists in current_users_lower
    if user_lower in current_users_lower:
        print(f"The username '{user}' is not available. Please enter a new username.")
    else:
        print(f"The username '{user}' is available.")


#5-11
# Store the numbers 1 through 9 in a list
numbers = list(range(1, 10))

# Loop through the list
for number in numbers:
    # Check the last digit of the number to determine the proper ordinal ending
    if number == 1:
        ordinal = 'st'
    elif number == 2:
        ordinal = 'nd'
    elif number == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    
# Print the number with its proper ordinal ending print(f"{number
{ordinal}")










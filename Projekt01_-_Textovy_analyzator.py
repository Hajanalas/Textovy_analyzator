"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jana Halasova
email: hajanalas@gmail.com
discord: janah.444
"""

# Texty určené k analýze
Texts = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """, """
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""", """
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
         ]

# Registrovaní uživatelé
Registered_users = dict(bob="123", ann="pass123", mike="password123",
                        liz="pass123")

# Vyžádání uživatelského jména a hesla od uživatele
Username = input("username:")
Password = input("password:")

# Ověření, zda údaje odpovídají někomu z registrovaných uživatelů
if Registered_users.get(Username) == Password:
    print(f"""----------------------------------------
Welcome to the app, {Username} 
We have 3 texts to be analyzed.
----------------------------------------"""
          )
else:
    print(f'unregistered user, terminating the program..')
    exit()

# Výběr jednoho z výše uvedených textů uživatelem
Selected_number = input("Enter a number btw. 1 and 3 to select: ")
if not Selected_number.isnumeric():
    print("You have to input a number!")
    exit()
elif int(Selected_number) not in [1, 2, 3]:
    print("You have to input a number btw. 1 and 3!")
    exit()

Text_number = int(Selected_number) - 1
Selected_text = Texts[Text_number]

# Vytvoření seznamu slov z vybraného textu bez interp. znamének
Clear_text = list()

for word in Selected_text.split():
    Clear_text.append(word.strip(",.:;"))

# Určení počtu slov ve vybraném textu
Words_counter = len(Clear_text)

# Dále určení:
# - počtu slov začínajících velkým písmenem,
# - počtu slov psaných velkými písmeny,
# - počtu slov psaných malými písmeny,
# - počtu čísel (ne cifer) ve vybraném textu
Title_words = list()
Upper_words = list()
Lower_words = list()
Numeric_string = list()

for word in Clear_text:
    if word.istitle():
        Title_words.append(word)
    elif word.isupper() and word.isalpha():
        Upper_words.append(word)
    elif word.islower():
        Lower_words.append(word)
    elif word.isnumeric():
        Numeric_string.append(word)

Title_words_counter = len(Title_words)
Upper_words_counter = len(Upper_words)
Lower_words_counter = len(Lower_words)
Numeric_string_counter = len(Numeric_string)

# Určení sumy všech čísel (ne cifer) ve vybraném textu
Suma_numeric_string = 0
for int_number in [int(number) for number in Numeric_string]:
    Suma_numeric_string += int_number

# Výpis zjištěných údajů
print(f"""----------------------------------------
There are {Words_counter} words in the selected text.
There are {Title_words_counter} titlecase words.
There are {Upper_words_counter} uppercase words.
There are {Lower_words_counter} lowercase words.
There are {Numeric_string_counter} numeric strings.
The sum of all the numbers {Suma_numeric_string}
----------------------------------------"""
      )

# Zjištění délek jednotlivých slov ve vybraném textu a jejich
# četnosti
Lengths_of_words = {}

for word in Clear_text:
    if len(word) not in Lengths_of_words:
        Lengths_of_words[len(word)] = 1
    elif len(word) in Lengths_of_words:
        Lengths_of_words[len(word)] += 1

# Seřazení délek jednotlivých slov ve vybraném textu za účelem
# vytvoření grafu
Sorted_lengths = dict(sorted(Lengths_of_words.items()))

# Určení velikosti odsazení údaj; v grafu v závislosti
# na nejpočetnější délce slov v textu
Sorted_lengths_values = list(sorted(Sorted_lengths.values()))
Highest_value = Sorted_lengths_values[-1]
Indent = Highest_value + 2

# Zobrazení sloupcového grafu reprezentujícího četnost různých
# délek slov ve vybraném textu
print(f"""LEN|{"OCCURENCES":^{Indent}}|NR.
----------------------------------------"""
      )

for length in Sorted_lengths:
    print(f"{length:>3}|{"*"*Sorted_lengths[length]:<{Indent}}|{Sorted_lengths[length]}")

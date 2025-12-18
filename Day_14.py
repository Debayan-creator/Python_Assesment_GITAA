'''

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Exercises: Level 1
Explain the difference between map, filter, and reduce.
Explain the difference between higher order function, closure and decorator
Define a call function before map, filter or reduce, see examples.
Use for loop to print each country in the countries list.
Use for to print each name in the names list.
Use for to print each number in the numbers list.
'''

#map -> Transform the list
#filter -> stores value based on condition
#reduce -> iteration based on a opeartion with a single value as o.p

#Higher-Order Function → Works with functions
#Closure → Remembers data from its creation scope
#Decorator → Enhances another function’s behavior

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda n:n%2==0, numbers))
print("Even ",even)

double = list(map(lambda n:n*2, even))
print("Double ", double)

red = reduce(lambda a,b:a+b, double)
print("Sum ", red)

'''
Exercises: Level 2
Use map to create a new list by changing each country to uppercase in the countries list
Use map to create a new list by changing each number to its square in the numbers list
Use map to change each name to uppercase in the names list
Use filter to filter out countries containing 'land'.
Use filter to filter out countries having exactly six characters.
Use filter to filter out countries containing six letters and more in the country list.
Use filter to filter out countries starting with an 'E'
Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
Use reduce to sum all the numbers in the numbers list.
Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
'''
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland','Indian']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cap = list(map(lambda b: b.upper(), names))
print(cap)

square = list(map(lambda n:n*2, numbers))
print("Double ", square)

land = list(filter(lambda country: "land" in country, countries))
print(land)

six = list(filter(lambda country: len(country) ==6, countries))
print(six)

E = list(filter(lambda name: name.startswith('E'), countries))
print(E)

data = [1, "apple", 3.5, "banana", True, "cherry"]

Str = list(filter(lambda x: isinstance(x, str), data))
print(Str)

sentence = reduce(
    lambda prev, cur: prev + ", " + cur,
    countries[:-1]
) + ", and " + countries[-1] + " are north European countries"

print(sentence)

def categorize_countries(pattern):
    return list(filter(lambda country: pattern.lower() in country.lower(), countries))
print(categorize_countries("land"))


from itertools import islice

def get_first_ten(countries):
    return list(islice(countries,10))
    
print(get_first_ten(countries))


def get_first_ten(countries):
    return list(islice(countries,10))
    
print(get_first_ten(countries))


def get_last_ten(countries):
    return countries[-10:]
    
print(get_last_ten(countries))

'''
Exercises: Level 3
Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
Sort countries by name, by capital, by population
Sort out the ten most spoken languages by location.
Sort out the ten most populated countries.
'''

[
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": [
            "Arabic"
        ],
        "population": 40400000,
        "flag": "https://restcountries.eu/data/dza.svg",
        "currency": "Algerian dinar"
    },
    {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": [
            "English",
            "Samoan"
        ],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar"
    },
    {
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "languages": [
            "Catalan"
        ],
        "population": 78014,
        "flag": "https://restcountries.eu/data/and.svg",
        "currency": "Euro"
    },
    {
        "name": "Angola",
        "capital": "Luanda",
        "languages": [
            "Portuguese"
        ],
        "population": 25868000,
        "flag": "https://restcountries.eu/data/ago.svg",
        "currency": "Angolan kwanza"
    },
    {
        "name": "Anguilla",
        "capital": "The Valley",
        "languages": [
            "English"
        ],
        "population": 13452,
        "flag": "https://restcountries.eu/data/aia.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Antarctica",
        "capital": "",
        "languages": [
            "English",
            "Russian"
        ],
        "population": 1000,
        "flag": "https://restcountries.eu/data/ata.svg",
        "currency": "Australian dollar"
    }]
    
def sorting(countries):
    return sorted(countries, key=lambda c:c["name"])
    
print(sorting(countries))

def sorting(countries):
    return sorted(countries, key=lambda c:c["capital"])
    
print(sorting(countries))

def sorting(countries):
    return sorted(countries, key=lambda c:c["population"])
    
print(sorting(countries))

from collections import Counter

languages = []

for country in countries_data:
    languages.extend(country["languages"])

most_spoken_languages = Counter(languages).most_common(10)

print(most_spoken_languages)


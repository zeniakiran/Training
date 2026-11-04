# Define Class
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the main language spoken in India.")

    def type(self):
        print("India is a developing nation.")

# Define another class
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the main language spoken in USA.")

    def type(self):
        print("USA is a developed nation.")

# Create objects
country1 = India()
country2 = USA()

# Use a common interface
for country in (country1, country2):
    country.capital()
    country.language()
    country.type()
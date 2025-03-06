# Creating a function needed for this particular program

def find_country(ctname, ctnamee, ct_to_country):
    """Find the country a city belongs to."""
    for country, cities in ct_to_country.items():
        if ctname in cities and ctnamee in cities:
            return country
    return None

# Example data: Dictionary mapping countries to cities
ct_to_country = {
    "Australia": {"Sydney", "Melbourne", "Brisbane", "Perth"},
    "India": {"Mumbai", "Delhi", "Bangalore", "Chennai"},
    "UAE": {"Dubai", "Abu Dhabi", "Sharjah", "Ajman"},
}

# User input
ctnamee = input("Enter the first City name: ")
ctname = input("Enter the Second City name: ")
country = find_country(ctname, ctnamee, ct_to_country)

if country:
    print("Both cities are from the same country!")
else:
    print("Both cities are not from the same country or not found in the database.")

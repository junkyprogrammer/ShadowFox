# Creating a function needed for this particular program

def find_country(ctname, ct_to_country):
    """Find the country a city belongs to."""
    for country, cities in ct_to_country.items():
        if ctname in cities:
            return country
    return "City not found in database."

# Example data: Dictionary mapping countries to cities
ct_to_country = {
    "Australia": {"Sydney", "Melbourne", "Brisbane", "Perth"},
    "India": {"Mumbai", "Delhi", "Bangalore", "Chennai"},
    "UAE": {"Dubai", "Abu Dhabi", "Sharjah", "Ajman"},
}

# User input
ctname = input("Enter the name of the city: ")
country = find_country(ctname, ct_to_country)
print(f"{ctname} belongs to {country}.")

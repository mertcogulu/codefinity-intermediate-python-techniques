# Step 1: Define the list of temperatures in Celsius
temp_celsius = [0, 25, 30, 40, 100]

# Step 2: Create a custom function for conversion
def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# Step 3: Use map() with the custom function
temp_fahrenheit = map(celsius_to_fahrenheit, temp_celsius)

# Step 4: Convert the map object to a list and print
temp_fahrenheit_list = list(temp_fahrenheit)
print(temp_fahrenheit_list)
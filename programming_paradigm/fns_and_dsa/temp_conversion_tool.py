FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp_input = input("Enter the temperature to convert: ")
    temperature = float(temp_input)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature:.1f}°C is {result:.2f}°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature:.1f}°F is {result:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid input. Please enter a valid number for temperature.")

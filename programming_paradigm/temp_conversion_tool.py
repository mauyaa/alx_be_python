#!/usr/bin/env python3

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # Get temperature input
    temp_input = input("Enter the temperature to convert: ")
    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    # Get unit input
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit_input not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    # Convert and display result
    if unit_input == 'F':
        converted_temp = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted_temp}°C")
    else:  # unit_input == 'C'
        converted_temp = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted_temp}°F")

if __name__ == "__main__":
    main()

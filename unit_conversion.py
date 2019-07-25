#Made by Akash Patel CS-171-A Lab Section 063
#Prints user interface according to homework insructions
print('Welcome to the Unit Conversion Wizard')
print('This program can convert between any of the following lengths:')
print('inches')
print('feet')
print('yards')
print('miles')
print('leagues')
print('centimeters')
print('decimeters')
print('meters')
print('hectometers')
print('kilometers\n')
#Dictionary / base unit is inches
key = {"inches": 1.0, "feet": 12.0, "yards": 36.0, "miles": 63360, 'leagues': 190080, 'centimeters': 0.393701, 'decimeters': 3.9370,'meters': 39.3701, 'decameters': 393.701, 'hectometers': 3937.01, 'kilometers':39370.1}

#Grabs necessary information for conversion
number = float(input('Enter value:\n'))

#based on user input, collect proper conversion value from dictionary
#newNumber represents the input converted to inches

unitFrom = input('Enter from units:\n')
if unitFrom == 'inches':
  newNumber = number * key['inches']
  
elif unitFrom == 'feet':
  newNumber = number * key['feet']
  
elif unitFrom == 'yards':
  newNumber = number * key['yards']
  
elif unitFrom == 'miles':
  newNumber = number * key['miles']
  
elif unitFrom == 'leagues':
  newNumber = number * key['leagues']
  
elif unitFrom == 'centimeters':
  newNumber = number * key['centimeters']
  
elif unitFrom == 'decimeters':
  newNumber = number * key['decimeters']
  
elif unitFrom == 'meters':
  newNumber = number * key['meters']
  
elif unitFrom == 'decameters':
  newNumber = number * key['decameters']
  
elif unitFrom == 'hectometers':
  newNumber = number * key['hectometers']
  
elif unitFrom == 'kilometers':
  newNumber = number * key['kilometers']
  
#the unit that the user wants to convert to
unitTo = input('Enter to units:\n')

#print original value and its units then the new value and new units rounded to 4 decimal places  
print(number, unitFrom, 'is', round(newNumber / key[unitTo], 4), unitTo)






def greet(name):
    print(f"Hello, {name}.")
    print(f"It's been a while now.")
    print(f"How are you doing, {name}?\n")

greet('Angela')
greet('John')

def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"What is it like in {location}?\n")

# Positional arguments    
greet_with('John', 'Lagos')

# Keyword arguments
greet_with(location = 'Ijebu Ode', name = 'Korede')
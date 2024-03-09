import random

first_names = ['John', 'Emma', 'Michael', 'Sophia', 'James', 'Olivia', 'William', 'Ava', 'Benjamin', 'Isabella']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']

def generate_random_name():
    return random.choice(first_names) + ' ' + random.choice(last_names)

if __name__ == "__main__":
    print("Generated Name:", generate_random_name())
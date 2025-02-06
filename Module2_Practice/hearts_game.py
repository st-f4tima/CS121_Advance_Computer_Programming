#to be solve....
relationship_status = ('Happiness', 'Euphoria', 'Admiration', 'Romance', 'Trust', 'Support')

first_name = set(input('Enter first name: ').replace(" ", "").lower())
second_name = set(input('Enter second name: ').replace(" ", "").lower())

unique_letters = first_name.symmetric_difference(second_name)
num_shared = len(unique_letters)
index = (num_shared - 1) - 6

print(f'Results: {num_shared} - Meaning: {relationship_status[index]}')




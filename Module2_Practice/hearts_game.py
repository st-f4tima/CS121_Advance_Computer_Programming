#to be solve....

meanings = ['Happiness', 'Euphoria', 'Admiration', 'Romance', 'Trust', 'Support']
shared_letters = []

first_name = list(input('Enter first name: ').replace(" ", "").lower())
second_name = list(input('Enter second name: ').replace(" ", "").lower())

for char in first_name:
    if char in second_name:
        shared_letters.append(char)
        second_name.remove(char)

num_shared = len(shared_letters)
print(f'Results: {num_shared} - Meaning: {meanings[num_shared]}')
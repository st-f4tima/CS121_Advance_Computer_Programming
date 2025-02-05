n = int(input('Enter a number: '))
list_nums = []

for i in range(1, n + 1):
    if i % 2 == 0:
        list_nums.append('even')
    else:
        list_nums.append('odd')

print(list_nums)
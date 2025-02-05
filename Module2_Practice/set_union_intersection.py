first_set = set(map(int, input('Enter elements of the first set: ').split()))
second_set = set(map(int, input('Enter elements of the second set:').split()))

union_sets = first_set.union(second_set)
intersection_sets = first_set.intersection(second_set)

print(f'Union: {union_sets}')
print(f'Intersection: {intersection_sets}')
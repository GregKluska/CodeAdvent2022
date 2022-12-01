my_input = [1, 2, 3, 4, 5]

print(f'Current Numbers List {my_input}')

number = int(input("Please enter a number to be added:\n"))

index = int(input(f'Enter the index between 0 and {len(my_input) - 1} to add the given number:\n'))

my_input.insert(index, number)

print(f'Updated List {my_input}')
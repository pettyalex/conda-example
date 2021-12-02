from functions import is_small

def read_in_data():
    with open('random-data.txt') as file:
        lines = []
        
        for line in file:
            lines.append(int(line.strip()))
    
    return lines

def sort(values: list):
    values.sort()
    return values

def do_filter(values: list):
    filtered_items = []
    for i in filter(is_small, values):
        filtered_items.append(i)
    return filtered_items

numbers = read_in_data()
sorted = sort(numbers)
filtered = do_filter(sorted)

print(f"There are {len(filtered)} numbers")

subject = {}
with open('file6.txt') as file:
    for line in file:
        name, hours = line.split(':')
        name_sum = sum(map(int, "".join([i for i in hours if i == ' ' or (i >= '0' and i <= '9')]).split()))
        subject[name] = name_sum
    print(f"{subject}")
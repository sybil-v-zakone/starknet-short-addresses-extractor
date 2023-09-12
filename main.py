finish_addresses = []

with open("start_addresses.txt", 'r', encoding='utf-8-sig') as file:
    start_addresses = [line.strip() for line in file]

for start_address in start_addresses:
    finish_addresses.append(hex(int(start_address, 16)))

with open('finish_addresses.txt', 'w') as file:
    for finish_address in finish_addresses:
        file.write(str(finish_address) + '\n')

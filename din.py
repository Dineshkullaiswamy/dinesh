rows = int(input('enter how many rows:'))
columns = int(input('enter how many columns:'))
symbol = int(input('enter how many symbol:'))

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

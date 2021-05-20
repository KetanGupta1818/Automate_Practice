
print('Welcome')
n = int(input('Enter the number of patterns: '))
for i in range(n):
    sym = input('Enter the symbol: ')
    brd = int(input('Enter the breadth of the box: '))
    hei = int(input('Enter the height of the box: '))
    try:
        box(sym, brd, hei)
    except Exception as err:
        print('An exception happened: ' + 'err')
def box(symbol, b, h):
    if len(symbol) != 1:
        raise Exception('The length of the character must be one')
    if b <= 2:
        raise Exception('The breath must be greater than two')
    if h <= 2:
        raise Exception('The height must be greater than two')
    c = b
    for k in range(b):
        print('Hello')
    for j in range(h - 2):
        print(symbol + (' ' * (b - 2) + symbol)
    for  in range():


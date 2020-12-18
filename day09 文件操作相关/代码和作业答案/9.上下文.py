f = open('info.txt', mode='rb')
data = f.read()
print(data)


with open('info.txt', mode='rb') as f:
    data = f.read()
    print(data)

def chop(c):
    del c[len(c)-1]
    del c[0]
letters = ['a', 'b', 'c', 'd', 'e']
chop(letters)
print(letters)
str = 'X-DSPAM-Confidence:0.8475'
atcolon = str.find(':')
num = float(str[atcolon+1:])
print(num)
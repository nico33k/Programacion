vow = ['a', 'e', 'i', 'o', 'u']
vowup = ['A', 'E', 'I', 'O', 'U']
let = input()
if let.isupper():
    print('uppercase')
if let.islower():
    print('lowercase')
if let in vow or let in vowup:
    print('vowel')
else:
    print('consonant')
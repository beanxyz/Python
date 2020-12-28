
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic= { row.letter:row.code for (index,row) in data.iterrows()}
name = input("Enter your name:\n")
result= [ phonetic[letter] for letter in name if letter in phonetic.keys()]
print(result)


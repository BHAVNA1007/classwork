#06_vowel_cons_special

ch = input("Enter the choice = ")

match ch:
      case 'a'|'e'|'i'|'o'|'u':
          print("Vowel")
      case '#'|'$':
          print("Special Character")
      case _:
           print("Consonant") 

print("out of match case")

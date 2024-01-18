#count vowles

def vowel(args):
   count = 0
   vwl = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
   for i in range(len(args)):
      if args[i] in vwl:
         count+=1
   print(count)
   return count
   
print("Enter word: ")
user_input = str(input(""))      
vowel(user_input) 

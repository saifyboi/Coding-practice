import cmath
#basic list operation
'''
in_string = input("Enter list elements with space: ")
my_list = in_string.split()
print(my_list)
my_list = [str(y) for y in my_list]
print(my_list)
'''

#slightly fancy list
usr_list = []
usr_list = [int(x) for x in input("Enter numbers of your choice: ").split()]
print(usr_list)
print(type(usr_list))
print("would you like to add more elements?")
y = input()
while y=='yes' or 'y' or 'Yes' or 'YES' or 'Y':
   add = [int(x) for x in input("Add new elements:" ).split()]
   usr_list.extend(add)
   print(usr_list)
   cnt = input("Want to continue?")
   if cnt=='no' or 'No' or 'NO' or 'N':
      srt = input("Do you want to sort your list?")
      if srt=='yes' or 'y' or 'Yes' or 'YES' or 'Y':
         print(usr_list.sort())
      else:
         print("bye")      
   break
else:
   print("have a nice day :)")



#fixed above slightly fancy list
'''
usr_list = [int(x) for x in input("Enter numbers of your choice: ").split()]
affirm=["yes", "yeah", "y", "YES", "Yes"]
negate=["no", "nope", "n", "NO", "No"]
# print(usr_list)
# print(type(usr_list))
while True:

    ask1 = input("would you like to add more elements?")
    if ask1 not in affirm:
        break

    add = [int(x) for x in input("Add new elements:").split()]
    usr_list.extend(add)

    cnt = input("Want to continue?")
    if cnt in negate:
        break
    else:
        continue

print("The original list is: ", usr_list)
usr_list.sort()
print("The sorted list is ", usr_list)

print("have a nice day :)")
'''

print("Hello , welcome to NetworkMulk Coffee!!!!!!!!")

name = input ("what's is your name?")

if name == "Ben" or name == "papi" or name == "loki":
   what_are_you = input("are you evil?")
   good_things = int(input("how many good things did you do today?\n"))
   if what_are_you == "yes" and good_things < 4 :
      print("you're not welcame here Evil " + name + ". get out of here!!")
      exit()
   else:
       print("oh, so you're one of those good " + name + ". come on in!!!")
else:
   print("Hello ," + name + " thank you so much for coming in today\n\n\n")

menu = "black coffee,\nEspresso,\nLatte,\n\n\n"

print(name + ", what do you like from out menu today?\n here is what er are serving.?\n" + menu)

order = input()

price = 8

quantity = input("How many coffees do you like?.\n")

total = price * int(quantity)

print("Thank you. your total is: $" + str(total))




print("Sounds good " + name + " we'll have your " + quantity + " " + order + " ready for you in a moment. ")
'''
THIS IS A MAGICIAN GAME WHERE THE USER HAS TO GUESS A SECRET NUMBER TO GET OUT OF THE LOOP


'''
print("Welcome to the magician game!")


# the secret number 
secret_number = 777

# ask the user to enter a guess number
usr_inp = int(input("what's your 3 digits guess number? "))


while usr_inp != secret_number:
   print(" HA HA HA!you're stuck in my loop!")
   usr_inp = int(input("TO GET OUT OGF THIS LOOP ENTER THE SECRET NUMBER! "))
   if usr_inp == secret_number:
        print("CONGRATS! YOU GOT OUT OF THE LOOP!")
        print("THE SECRET NUMBER IS:", secret_number)
        break


secret_name = "wuraola"
name = ""
name_count = 0
name_limit = 3
out_of_names = False
while secret_name != name and not (out_of_names):
    if name_count < name_limit:
        name = input("what is my name ")
        name_count += 1
    else:
        out_of_names = True
if out_of_names:
    print ("Out of Guesses, You Lose!")  
else:
    print("you win!")

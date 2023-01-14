print ("Welcome to computer quiz! ")
playing = input("Do you want 2 play the game? type 'YES'.  ")

if playing.upper() != "YES":
    quit()
    
print("Okay! Lets play :) ")
score=0

answer= input("What does cpu stand for? ")
if answer.upper() ==  "CENTRAL PROCESSING UNIT":
    print("")
    score += 1
else: print("")

answer= input("What does PSU stand for? ")
if answer.upper() ==  "POWER SUPPLY":
    print("")
    score += 1
else: print("")

answer= input("What does BBT stand for? ")
if answer.upper() ==  "BIG BOY TOYS":
    print("")
    score += 1
else: print("")

answer= input("What does RAM stand for? ")
if answer.upper() ==  "RANDOM ACESS MEMORY":
    print("")
    score += 1
else: print("")

answer= input("What does CWH stand for? ")
if answer.upper() ==  "CODE WITH HARRY":
    print("")
    score += 1
else: print("")


print("You got " + str(score) + " Question Correct!")
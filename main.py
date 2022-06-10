import random

print("Enter R for Rock, P for paper, S for Scissors")
possible_options=["R","P","S"]

player_count= 0
cpu_count=0
while True:
    for count in range(1,4):  
        player=input(">").upper()
        cpu=str(random.choice(possible_options))

      
        if player==cpu:
            print("The computer and player pick the same move")
            continue
        elif player=="R" or "P"and cpu=="P" or "R":
            winner="P"
        elif player=="S" or "P"and cpu=="P" or "S":
            winner="S"       
        elif player=="S" or "R"and cpu=="R" or "S":
            winner="R"
        else:
            print("Invalid Input")
            continue
        if player==winner:
                player_count+=1
                print(f"player({player}) : CPU({cpu})\nplayer wins")
        else:
                cpu_count+=1
                print(f"player({player}) : CPU({cpu})\nComputer wins")
        continue
    break


print(f"player({player_count}): computer({cpu_count})")
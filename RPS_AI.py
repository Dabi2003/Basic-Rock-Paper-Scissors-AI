import random


player_points=0
ai_points=0

#train AI to predict next move
def train(arr):
    nums={"R":0,"P":0,"S":0}
    for x in arr:
        if(x=="R"):
         nums[x]+=1
        if(x=="P"):
            nums[x]+=1
        if(x=="S"):
            nums[x]+=1
    training_moves=[]
    big=max(nums,key=nums.get)    #next use the most common move of player to gain AI_points
    if(big=="R"):
        training_moves.append("P")
    if(big=="P"):
         training_moves.append("S")
    if(big=="S"):
        training_moves.append("R")

    #finding patterns
    for i in range(0,len(arr)-1):
        if(i==len(arr)-2):
            break
        temp=arr[i]+arr[i+1]+arr[i+2]
        for x in range(i+3,len(arr)-1):
            if(x==len(arr)-2):
                break 
            pattern=arr[x]+arr[x+1]+arr[x+2]
            if(pattern==temp):
                temp=[arr[i],arr[i+1],arr[i+2]]
                for n in temp:
                    if(n=="R"):
                        training_moves.append("P")
                    else:
                        if(n=="P"):
                            training_moves.append("S")
                        else:
                            if(n=="S"):
                                training_moves.append("R")
    return(training_moves)


   
    
#replaying the game but the AI is using past experiences to predict next move
def play_again():
    temp_moves=train(training_data)
    print(temp_moves)
    training_data.clear()
    for i in range(0,10):
            move=input("Enter a move Type: R(rock) P(paper) S(scisscors) ")
            training_data.append(move)
            ai_move=temp_moves[i]
            print("player: ",move)
            print(" ")
            print("AI_move:", ai_move)
            compare(ai_move,move)
            print("Player_score: ",player_points," AI_score: ",ai_points)
            
        

#compare player and AI move
def compare(ai_move,move):
    global player_points
    global ai_points
    AI_win=0
    if(ai_move=="R" and move=="P"):
        print("Player wins")
        player_points+=1
     
    
    if(ai_move=="P" and move=="R"):
         print("AI wins")
         ai_points+=1
    
    if(ai_move=="R" and move=="S"):
        print("AI wins")
        ai_points+=1
    
    if(ai_move=="S" and move=="R"):
        print("Player wins")
        player_points+=1
    
    if(ai_move=="S" and move=="P"):
        print("AI wins")
        ai_points+=1
    
    if(ai_move=="P" and move=="S"):
        print("Player wins")
        player_points+=1
    return(AI_win)

#First play through where the AI makes a random choice
ai_moves=["R","P","S"]
training_data=[]
training_moves=[]
for i in range(0,10):
    move=input("Enter a move Type: R(rock) P(paper) S(scisscors) ")
    training_data.append(move)
    ai_move=random.choice(ai_moves)
    print("player: ",move)
    print(" ")
    print("AI_move:", ai_move)
    compare(ai_move,move)
    print("Player_score: ",player_points," AI_score: ",ai_points)

while(1):
    again=input("Would you like to play again? 'Y':yes 'N':no ")
    if(again=="Y"):
     play_again()
    if(again=="N"):
        break



#added some pattern recoginition, let's see if we could go deeper next time







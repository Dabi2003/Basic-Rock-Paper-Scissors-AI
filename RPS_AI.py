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
    
    big=max(nums,key=nums.get)    #next use the most common move of player to gain AI_points
    if(big=="R"):
        return("P")
    if(big=="P"):
        return("S")
    if(big=="S"):
        return("R")
    
   
    

  
        
            

    
    
#replaying the game but the AI is using past experiences to predict next move
def play_again():
    for i in range(0,10):
        move=input("Enter a move Type: R(rock) P(paper) S(scisscors) ")
        training_data.append(move)
        temp_move=train(training_data)
        ai_move=temp_move
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

print(train(training_data))
while(1):
    again=input("Would you like to play again? 'Y':yes 'N':no ")
    if(again=="Y"):
     play_again()
    if(again=="N"):
        break









import random

class FruitQuiz:
    
    def __init__(self):
        
        self.fruits= {

'apple':'red',

'orange':'orange',

'watermelon':'green',

'banana':'yellow'

}
    def quiz(self):
        
        while (True):
            fruits, color =  random.choice(list(self.fruits.items())) 
            
            print(f"What is the Colour of {fruits}")      
            user_ans = input()
            
            if user_ans.lower() == color:
                print("Correct Answer")
                
            else:
                print("Wrong Answer")
                
            option = int(input("Enter 0 If You Want to Add Another Flashcard. Otherwise, Enter 1: " ))
            if (option):
                break
print("Welcome to Fruit Quiz")
fq = FruitQuiz()
fq.quiz()
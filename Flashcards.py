class FlashCard:
    
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        
    def __str__(self):
        return self.word + ' ( ' + self.meaning + ' ) '
    
flash = []
print("Welcome to Flashcard Application")

while True:
    word = input("Enter the Name You Want to Add to Flashcard: ")
    meaning = input("Enter the Meaning of the Word: ")
    
    flash.append(FlashCard(word, meaning))
    option = int(input("Enter 0 If You Want to Add Another Flashcard. \nOtherwise, Enter 1: "))
    
    if(option):
        break
    
print("/nYour Flashcards")

for i in flash:
    print(">", i)

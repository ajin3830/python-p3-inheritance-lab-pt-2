class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    def raise_hand(self):
        print("Pick me!")
class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    def raise_hand(self):
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        
# Class Student says a brief greeting. .                                             
# Class Student respectfully tries to get the teacher's attention. .                 
# Class ChattyStudent says a brief greeting, then tries to spoil a TV show. .        
# Class ChattyStudent respectfully tries to get the teacher's attention 10 times.
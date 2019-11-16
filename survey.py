import time
questionNumber = 0
name = str(input("Please Enter your name"))
print()
def questions():
    def questionOne():
        global right, wrong, questionNumber
        print("How Satisfied are you with your visit?")
        print("Are you A:Very Satisfied B:Somewhat Satisfied C:Satisfied or D:Not Satisfied")
        ans = str(input())
        if ans == "A" or ans == "a" or ans == 'Very Satisfied' or ans == 'very sa':
            print("Thank you")
            right = right + 1
        else:
            print("Would you like a manager to contact you about your visit?")
            wrong = wrong+1
        questionNumber = questionNumber + 1
    questionOne()
    time.sleep(2)
    print()
    time.sleep(4)
    def questionTwo():
        global right, wrong, questionNumber
        print("Are you A:Very Satisfied B:Somewhat Satisfied C:Satisfied or D:Not Satisfied")
        print("Are you A:Very Satisfied B:Somewhat Satisfied C:Satisfied or D:Not Satisfied")
        ans = str(input())
        if ans == "C" or ans == "c" or ans == '1642'or ans == '3':
            print("You got it right!")
            right = right + 1
        else:
            print("You got it wrong!")
            wrong = wrong+1
        questionNumber = questionNumber + 1   
    questionTwo()
    time.sleep(2)
    print()
    print("So far ",name,"You have got",right,"Answers right,",wrong,"Answers wrong and you have completed",questionNumber,"Questions")
    print()
    time.sleep(4)
    def questionThree():
        global right, wrong, questionNumber
        print("How satisfied were you with the cleanliness of the restaurant (Approx)")
        print("Is it A:2000 B:600 C:70,000 or D:100000")
        ans = str(input())
        if ans == "D" or ans == "d" or ans == '100000'or ans == '4':
            print("You got it right!")
            right = right + 1
        else:
            print("You got it wrong!")
            wrong = wrong+1
        questionNumber = questionNumber + 1   
    questionThree()
    time.sleep(2)
    print()
    print("So far ",name,"You have got",right,"Answers right,",wrong,"Answers wrong and you have completed",questionNumber,"Questions")
    print()
    time.sleep(4)
    def questionFour():
        global right, wrong, questionNumber
        print("How satisfied were you with the quality of the food")
        print("Is it A:61,000 B:208,000 C:98,000 or D:18,000")
        ans = str(input())
        if ans == "D" or ans == "d" or ans == '100000'or ans == '4':
            print("You got it right!")
            right = right + 1
        else:
            print("You got it wrong!")
            wrong = wrong+1
        questionNumber = questionNumber + 1   
    questionFour()
questions()
#quiz game
#-----------------------------
def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1
    for key in question:
        print("-----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("enter(A,B,C or D):")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses+=check_answer(question.get(key),guess)
        question_num+=1
    display_score(correct_guesses,guesses)
#-----------------------------
def check_answer(answer,guess):
    if answer==guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

#-----------------------------
def display_score(correct_guesses,guesses):
    print("#-----------------------------")
    print("RESULT")
    print("#-----------------------------")
    print("answers:",end=" ")
    for i in question:
        print(question.get(i),end=" ")
    print()
    print("guesses:",end=" ")
    for i in guesses:
        print(i,end="")
    print()
    score=int((correct_guesses/len(question))*100)
    print("your score:"+str(score)+"%")
#-----------------------------
def play_again():
    response=input("do you want to play again:(yes/no):")
    response=response.upper()
    if response=="YES":
        return True
    else:
        return False
#-----------------------------



question={"who created the python?":"A",
          "which year python was created?":"B",
          "python is tributed to which comedy group?":"C",
          "is the earth round?":"A"
          }
options=[["A.guiden van rossum","B.elon musk","C.bill gates","D.mr beem"],
         ["A.1989","B.1991","C.2000","D.2010"],
         ["A.lonely island","B.smosh","C.monty python","D.SNL"],
         ["A.true","B.false","C.sometimes","D.what is earth"]]
new_game()
while play_again():
    new_game()
print("byeeeeee")
right=0
wrong=0
ques=5

q1 = input("Q1. A triangle with no two sides of equal length \n")
if (q1.lower() == "scalene triangle"):
    print("Correct!")
    right+=1
else:
    print("Wrong Answer :(")
    print("") #print correct ans
    wrong+=1
    
perc=(right/ques)*100

print("---------------- RESULT ----------------")
print("Total Score is ", right)
print("Percentage obtained ", perc) #funky alt
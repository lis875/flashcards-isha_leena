right=0
wrong=0
ques=5

# QUESTION
q1 = input("Q. A triangle with no two sides of equal length \n")
if (q1.lower() == "scalene triangle"):
    print("Correct!")
    right+=1
else:
    print("Wrong Answer :(")
    print("The correct answer is Scalene Triange") #print correct ans
    wrong+=1

# QUESTION
q2 = input("Q. Which number is neither prime nor composite? \n")
if (q2 == "1") or (q2.lower() == "one"):
    print("Correct!")
    right+=1
else:
    print("Wrong Answer :(")
    print("The correct answer is 1") #print correct ans
    wrong+=1

q3 = input("Q. Evaporation, Condensation, Precipitation, Run off.. What's next \n")
if (q2.lower() == "evaporation"):
    print("Correct!")
    right+=1
else:
    print("Wrong Answer :(")
    print("The correct answer is Evaporation") #print correct ans
    wrong+=1

# QUESTION
q4 = input("Q. True or False: The foods you eat and the products you buy affect freshwater resources \n")
if (q4.lower() == "True"):
    print("Correct!")
    right+=1
else:
    print("Wrong Answer :(")
    print("The correct answer is True") #print correct ans
    wrong+=1

perc=(right/ques)*100

print("---------------- RESULT ----------------")
print("Total Score is ", right)
print("Percentage obtained ", perc) #funky alt
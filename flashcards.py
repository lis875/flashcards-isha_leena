import random

total_ques = 4
right = 0
wrong = 0

def ques(ques_no):
    global right  # Declare right as a global variable
    global wrong  # Declare wrong as a global variable
    while(True):
        if ques_no == 'q1':
            q1 = input("Q. A triangle with no two sides of equal length\n")
            if q1.lower() == "scalene triangle":
                print("Correct!\n")
                right += 1
                break
            else:
                print("Wrong Answer :(\n")
                #print("The correct answer is Scalene Triangle")  # Print correct ans
                wrong += 1

        elif ques_no == 'q2':
            q2 = input("Q. Which number is neither prime nor composite?\n")
            if q2 == "1" or q2.lower() == "one":
                print("Correct!\n")
                right += 1
                break
            else:
                print("Wrong Answer :(\n")
                #print("The correct answer is 1")  # Print correct ans
                wrong += 1

        elif ques_no == 'q3':
            q3 = input("Q. Evaporation, Condensation, Precipitation, Run off.. What's next\n")
            if q3.lower() == "evaporation":
                print("Correct!\n")
                right += 1
                break
            else:
                print("Wrong Answer :(\n")
                #print("The correct answer is Evaporation")  # Print correct ans
                wrong += 1

        elif ques_no == 'q4':
            q4 = input("Q. True or False: The foods you eat and the products you buy affect freshwater resources\n")
            if q4.lower() == "true":
                print("Correct!\n")
                right += 1
                break
            else:
                print("Wrong Answer :(\n")
                #print("The correct answer is True")  # Print correct ans
                wrong += 1

ques_list = ['q1', 'q2', 'q3', 'q4']
random.shuffle(ques_list)
for i in range(4):
    ques(ques_list[i])

perc = (right / total_ques) * 100

print("---------------- RESULT ----------------")
print("Total Score is ", right)
print("Percentage obtained ", perc)
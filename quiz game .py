print("Welcome to Quiz Game 2022 ")

game = print(input("Are you ready to play game ? "))

if game != "yes":
   print("Lets go..!!")

score = 0

q1 = input("What is full form of jk ? ").lower()

if q1 == ("just kidding"):
    print("Correct")
    score += 1
else:
    print("Oops its wrong....better luck next time")

q2 = input("What is full form of dw ? ").lower()

if q2 == ("dont worry"):
    print("Correct")
    score += 1
else:
    print("Oops its wrong....better luck next time")

q3 = input("What is full form of MMCOE ? ").lower()

if q3 == ("marathwada mitra mandal college of engineering"):
    print("Correct")
    score += 1
else:
    print("Oops its wrong....better luck next time")

q4 = input("What is full form of fb ? ").lower()

if q4 == ("face book"):
    print("Correct")
    score += 1
else:
    print("Oops its wrong....better luck next time")

q5 = input("What is full form of HD ? ").lower()

if q5 == ("Hexadecimal dump"):
    print("Correct")
    score += 1
else:
    print("Oops its wrong....better luck next time")

print("You got " + str(score) + "questions correct" )

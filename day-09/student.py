student = {}
choice = "yes"
while choice == "yes":
    choice = input("Would you like to add studnt(\'yes\' or \'no\'): ")
    if choice == "yes":
        name = input("Enter name of Student: ")
        scores = []
        for i in range(3):
            score = int(input(f'Score {i}: '))
            scores.append(score)
        student[name] = scores

print(student)
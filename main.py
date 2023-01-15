SCORE = 0
QUESTIONS = 3

print("Hi! Welcome to the multiple choice quiz")
print("QUESTION Nu.1:")
requiredAnswer1 = input("which cell phone do I have?\na. Huawei\nb. Samsung\nc. Xiaomi\nd. Iphone\nAnswer:")
if requiredAnswer1 == "C" or requiredAnswer1 == "c" or requiredAnswer1 == "Xiaomi" or requiredAnswer1 == "xiaomi":
    SCORE += 1
    print("Correct!")
    print("You've answered " + str(SCORE) + "/" + str(QUESTIONS) + " correct.\n")
else:
    print("Incorrect! the correct answer was -Xiaomi.\n")


print("QUESTION Nu.2:")
requiredAnswer2 = input("Which computer do I have?\na. Mac\nb. Acer\nc. Samsung\nAnswer:")
if requiredAnswer2 == "B" or requiredAnswer2 == "b" or requiredAnswer2 == "Acer" or requiredAnswer2 == "acer":
    SCORE += 1
    print("Correct!")
    print("You've answered " + str(SCORE) + "/" + str(QUESTIONS) + " correct.\n")
else:
    print("Incorrect!\nThe correct answer was -Acer.\n")


print("QUESTION Nu.3")
requiredAnswer3 = input("Which programming language do I like most?\na. Python\nb. JavaScript\nc. Java\nAnswer:")
if requiredAnswer3 == "A" or requiredAnswer3 == "a" or requiredAnswer3 == "Python" or requiredAnswer3 == "python":
    SCORE += 1
    print("Correct!")
    print("You've answered " + str(SCORE) + "/" + str(QUESTIONS) + " richtig.\n")
else:
    print("Incorrect!\nThe correct answer was -Python.\n")


if SCORE <= 1:
    print(str(SCORE) + "/" + str(QUESTIONS) + "-you suck.")
elif SCORE == 2:
    print(str(SCORE) + "/" + str(QUESTIONS) + " -.You could do better")
else:
    print("Congratulations! You've answered " + str(SCORE) + "/" + str(QUESTIONS) + " correct.")

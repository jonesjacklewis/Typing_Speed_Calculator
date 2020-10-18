from time import time  # Imports the time module

testSentence = "The Quick Brown Fox Jumps Over the Lazy Dog."  # A test sentence
pointsNeeded = len(testSentence)  # The number of points available is equal to the length of the testSentence
weight = 1 / pointsNeeded  # The weight of equal char is equal to the reciprocal of the total points
print("Please type the following sentence as quickly an accurately as possible. For every error your time will be "
      "increased by a calculated percentage ")
print(testSentence)
print("\n")
print("Press a key when ready: ")
input()
print(testSentence)
print("\n")
start = time()  # Starts Timer by saving the current time
user = input()  # When user press Enter
stop = time()  # Ends timer by saving the new time
NumErrors = 0  # Variable for number of errors initially set to zero


# Below fixes length issues
if len(user) > len(testSentence):
    while len(user) != len(testSentence):
        testSentence += "*"

if len(user) < len(testSentence):
    while len(user) != len(testSentence):
        user += "*"


for i in range(pointsNeeded - 1):  # For each character in test string
    if user[i] != testSentence[i]:  # If the character doesn't match what should
        NumErrors += 1  # Increments number of errors
UserWeight = NumErrors * weight  # Works out an adjustment
originalTime = stop - start  # Calculates time without errors
adjustTime = originalTime * (1 + UserWeight)  # Calculates an adjusted time based on errors

originalTime = round(originalTime, 2)  #  rounds
NumErrors = NumErrors
newTime = round(adjustTime, 2)  # rounds

numWords = len(user.replace(".","").split(" ")) # Gets number of words
sToM = round(newTime / 60, 2)  # Converts to minutes and rounds
wpm = round(numWords/sToM, 2)  # Calculates wpm and rounds




print(f"You would have completed the test in {originalTime} seconds but due to {NumErrors} error(s) your adjusted time is {adjustTime} seconds")
print(f"This means your wpm is {wpm}")

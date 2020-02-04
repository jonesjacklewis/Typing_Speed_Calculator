from time import time  # Imports the time module

testSentence = "The Quick Brown Fox Jumps Over the Lazy Dog."  # A test sentence
pointsNeeded = len(testSentence)  # The number of points available is equal to the length of the testSentence
weight = 1 / pointsNeeded  # The weight of equal char is equal to the reciprocal of the total points
print("Please type the following sentence as quickly an accurately as possible. For every error your time will be "
      "increased by a calculated percentage ")
print("\n")
print("Press a key when ready: ")
input()
print(testSentence)
print("\n")
start = time()  # Starts Timer by saving the current time
user = input()  # When user press Enter
stop = time()  # Ends timer by saving the new time
NumErrors = 0  # Variable for number of errors initially set to zero
for i in range(pointsNeeded - 1):  # For each character in test string
    if user[i] != testSentence[i]:  # If the character doesn't match what should
        NumErrors += 1  # Increments number of errors
UserWeight = NumErrors * weight  # Works out an adjustment
originalTime = stop - start  # Calculates time without errors
adjustTime = originalTime * (1 + UserWeight)  # Calculates an adjusted time based on errors

originalTime = str(round(originalTime, 2))  # Converts to string and rounds
NumErrors = str(NumErrors)  # Converts to String
newTime = str(round(adjustTime, 2))  # Converts to string and rounds

print("You would have completed the test in %s seconds but due to %s errors your adjusted time is %s seconds" %
      (originalTime, NumErrors, adjustTime))

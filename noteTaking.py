"""
This is a python script that that creates a simple note-taking program.  When a user starts it up
it will prompt them for a filename.  If they enter a file name that doesn't exist, it will create
it and prompt the user to start entering in the text they want to write to the file.

If they enter a file name that already exists, it will ask the user if they want to:
A) Read the file
B) Delete the file and start over
C) Append the file
D) Replace a single line in the file.

"""

import os

# Function that takes th input from the user and writes the data to a file.
def takeNotes(x, tempValue):
    lines = []
    tempFile = open(inputFile, x)
    print("Please start entering your notes.  To exit the program please hit Enter twice")
    print("\n")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    if tempValue == "C":
        text = "\n".join(lines)
        tempFile.write("\n"+text)
    else:
        text = "\n".join(lines)
        tempFile.write(text)
    tempFile.close()

# Prompting user to enter a file name
inputFile = input("\nPlease enter a file name: ")
print("\n")
tempValueList = ["A", "B", "C", "D"]

# Checking to see if the file name already exist
if os.path.exists(inputFile) == False:
    x = "w"
    dummyValue = ""
    takeNotes(x, dummyValue)
else:
    print("File exist")
    print("What do you wish to do?")
    print("A) Read the file context")
    print("B) Delete the file and start over")
    print("C) Append the file")
    print("D) Replace a single line")
    tempValue = input("Please enter A, B, C, or D: ")
    tempValue = tempValue.upper()

# Verifying that the user enters one of the required values
    while not tempValue in tempValueList:
        tempValue = input("Please enter A, B, C, or D: ")
        tempValue = tempValue.upper()
    
    if tempValue == "A":
        tempFile = open(inputFile, "r")
        print("\n")
        print(tempFile.read())
    
    if tempValue == "B":
        print("\nThe content in",inputFile,"will be deleted\n")
        os.remove(inputFile)
        x = "w"
        takeNotes(x,tempValue)
    
    if tempValue == "C":
        print("\nAdditional content will be added to",inputFile,"\n")
        x = "a"
        takeNotes(x, tempValue)
    
    if tempValue == "D":
        tempFile = open(inputFile, "r")
        print("\nCurrent contents of the notes:\n")
        print(tempFile.read())
        tempFile.close()
        inputList = []
        tempFile = open(inputFile, "r")

        for line in tempFile:
            tempFileLine = line.strip("\n").split()
            inputList.append(tempFileLine)
        
        tempFile.close()
        x = len(inputList)
        i = 1
        print("\n")
        while i <= x:
            print("Which line do you wish to replace",i,inputList[i-1])
            i += 1

# Determining which line needs to be replace alone with the text that will replace it        
        print("\n")
        lineNumUpdate = int(input("Please enter the line number you wish to replace: "))
        textToReplace = input("Please enter the text you wish to update the line with:\n").split()
        lineNumUpdate -= 1
        inputList[lineNumUpdate] = textToReplace

# Writing the new text to the inputFile
        with open(inputFile, 'w') as newNoteFile:
            for item in inputList:
                newNoteFile.write(" ".join(map(str,item)))
                newNoteFile.write("\n")






    
    






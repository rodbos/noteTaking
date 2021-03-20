
import os

def takeNotes(x, tempValue):
    lines = []
    tempFile = open(inputFile, x)
    print("Please start entering your notes.  To exit the program please hit Enter twice")
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

inputFile = input("Please enter a file name: ")
tempValueList = ["A", "B", "C", "D"]

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

    while not tempValue in tempValueList:
        tempValue = input("Please enter A, B, C, or D: ")
        tempValue = tempValue.upper()
    
    if tempValue == "A":
        tempFile = open(inputFile, "r")
        print(tempFile.read())
    
    if tempValue == "B":
        print("The content in",inputFile,"will be deleted")
        os.remove(inputFile)
        x = "w"
        takeNotes(x,tempValue)
    
    if tempValue == "C":
        print("Additional content will be added to",inputFile)
        x = "a"
        takeNotes(x, tempValue)
    
    if tempValue == "D":
        tempFile = open(inputFile, "r")
        print("\n")
        print("Current contents of the notes")
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
        
        print("\n")
        lineNumUpdate = int(input("Please enter the line number you wish to replace: "))
        textToReplace = input("Please enter the text you wish to update the line with:\n").split()
        lineNumUpdate -= 1
        inputList[lineNumUpdate] = textToReplace
        
        with open(inputFile, "w") as newNoteFile:
            newNoteFile.write("\n".join(str(line) for line in inputList))
            # for line in inputList:
            #     newNoteFile.write("%s\n".join(str(line)))


    
    






#Sabrina Turney
#October 15, 2018
#Going Green & File Interaction
#This program takes multiple inputs from the user to calculate their overall
#savings from "going green" using multiple arrays, as well as creating files
#to store these arrays by appending files.

def main():
    #Declare local variables
    endProgram = "no"
    
    notGreenCost = [0] * 12
    goneGreenCost = [0] * 12
    savings = [0] * 12
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    option = 0

    
    while endProgram == "no":
        print("Option 1 will get input for your costs before and after going green")
        print("Option 2 will display this info for you.")
        print("Option 3 will write these values to a txt file for later use.")
        print("And option 4 will read the data you've entered back to you!")

        option = (int(input("Please enter an option 1 through 4 to continue: ")))

    #Function calls and a ton of elif statements!
        if option == 1:
            getNotGreen(notGreenCost, months)
            getGoneGreen(goneGreenCost, months)
            energySaved(notGreenCost, goneGreenCost, savings)
        elif option == 2:
            displayInfo(notGreenCost, goneGreenCost, savings, months)
        elif option == 3:
            writeToFile(months, savings)
        elif option == 4:
            readFromFile(months, savings)

        #Repetition structure here will end or repeat the program:
        endProgram = input("Do you want to end the program? Yes or no: ")

def writeToFile(months, savings):
    savingsFile = open("savings1.txt", "a")
    savingsFile.write("Savings:\n")
    counter = 0
    while counter < 1:
        savingsFile.write((str(months) + "\n"))
        savingsFile.write((str("\n")))
        savingsFile.write((str(savings) + "\n"))
        counter += 1
        
    savingsFile.close()
    print("\n\nWe've written a file of all your months and savings!")
    return

def readFromFile(months, savings):
    inFile = open("savings1.txt", "r")
    str1 = inFile.read()
    print(str1)
    inFile.close
    return
    

#Here's where we get our not green cost array filled up by the user:
def getNotGreen(notGreenCost, months):
    #I just called the "counter" variable index here to keep in line
    #with the list nomenclature!
    index = 0
    while index < len(notGreenCost):
        #To avoid too many args in the input line, I made the months into
        #headers that appear before the user inputs so they know which
        #month they are inputting to.
        print ("\t\t" + (months[index]))
        notGreenCost[index] = int(input("Enter NOT GREEN energy costs for this month: "))
        index += 1
    print("-----------------------------------------------")
    return notGreenCost, months

def getGoneGreen(goneGreenCost, months):
    index = 0
    while index < len(goneGreenCost):
        #Again, I display the months as headers here to avoid having
        #too many arguments in the code input.
        print("\t\t" + months[index])
        goneGreenCost[index] = int(input("Enter GONE GREEN energy costs for this month: "))
        index += 1
    print("-----------------------------------------------")
    return goneGreenCost, months

#Calculation using a bunch of arrays! Cool!
def energySaved(notGreenCost, goneGreenCost, savings):
    index = 0
    while index < len(savings):
        #I picked savings here because all our arrays are 12 elements long anyway.
        savings[index] = notGreenCost[index] - goneGreenCost[index]
        index += 1
    return notGreenCost, goneGreenCost, savings

#Just printing out all the good info for the end user.
def displayInfo(notGreenCost, goneGreenCost, savings, months):
    index = 0
    while index <len(savings):
        #I tried to make it look a little nicer here at the display,
        #but kept in line with the pseudocode.
        #unlike the "your code might look like this!" example.
        print("-----------------------------------------------")
        print("\t\t SAVINGS")
        print("-----------------------------------------------")
        print("Information for: ", months[index])
        print("Savings: $", savings[index])
        print("Not Green Costs: $", notGreenCost[index])
        print("Gone Green Costs: $", goneGreenCost[index])
        #this prevents our savings from running forever
        index += 1

#Call the main function for the user.        
main()

#Sabrina Turney
#October 15, 2018
#Sum of Numbers
#This program takes a file I created, numbers.txt, reads the numbers in the file
#and then calculates and returns their total - Lab specifies integers only.

def main():

    #Nice introduction
    print("Welcome to my file reading program!")
    print("In this exercise, I'll read the integers in your number file,")
    print("And then print out the sum of the numbers in the file!")

    #Declare a variable I'll use later
    total = 0

    #I open the numbers.txt file to read it, I'm not changing the file.
    file = open("numbers.txt", "r")

    #I'll print the contents to show the user what I'm calculating in
    #my For loop.
    print("\nHere's the current contents of your numbers file:")

    #Here's the loop! This changes the string values the numbers in the file
    #curently are into integers that can be added. After that, I use my
    #total variable from earlier to add them as I'm looping.
    for line in file:
        nums = int(line)
        print("\t", nums)
        total += nums

    print("------------------------------------")
    
    #Last thing to do is print the data to the user:
    print("\nThe total value of all the integers in your document is: \n\t", total)
    #Say a little goodbye for the end of the program:
    print("\nThank you for using my program to count your file numbers!")
    #Close the file, very important:

    file.close()
#Call the main function for the user.
main()

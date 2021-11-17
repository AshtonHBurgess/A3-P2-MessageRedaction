import sys;

#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     w0465511
#Student Name:  Ashton Burgess

#Create a program that will remove desired letterfrom a given list or string value
#peramiters will be (Letters to be removed, string value )
#program also needs to beable to tell how many characters have been removed
#also needs option to quit of do the program again



#Method for spliting and joining 
def splitString(phrase, remove):
    phraseList=phrase.split(remove)
    return ("_".join(phraseList))

def main():

    
    while True:
        #Part one of Program: Collect the message and letters to redact and Create the potentail quit froom the program
        #message="here we go ssssaaaammagain my my "
        message=input("Type a phrase (or quit to exit program): ")
        messageLen=len(message)
        if message.lower()=="quit":
            print("quiting program")
            exit()
        
        #redact="a,s,m"
        #Seperate the letters to redact, and count them
        redact=input("Type a comma-seperated list of letters to redact: ")
        numToRedact=len(redact)
        print(numToRedact)
        
        redactList=redact.split(",")
        for i in range(len(redactList)):
            if i ==0:
                newmessage=splitString(message,redactList[i])
            else:
                newmessage=splitString(newmessage,redactList[i])
        # taking out the "_" so i can count the characters in final message and subtract the final characters from the original message length to get letters removed
        checkingFinalLen=newmessage.split("_")
        almostAtFinalLen="".join(checkingFinalLen)
        finalLen=messageLen - (len(almostAtFinalLen))
        print("Number of letters redacted: {0}".format(finalLen))
        print(newmessage)
        print()
main()


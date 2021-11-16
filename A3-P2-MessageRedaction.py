import sys;

#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     w0465511
#Student Name:  Ashton Burgess

#Create a program that will remove desired letterfrom a given list or string value
#peramiters will be (Letters to be removed, string value )




def splitString(phrase, remove):
    phraseList=phrase.split(remove)
    return ("_".join(phraseList))

def main():

    
    while True:
        
            



        #message="here we go ssssaaaammagain my my "
        message=input("Type a phrase (or quit to exit program): ")
        if message.lower()=="quit":
            print("quiting program")
            exit()
        
        #redact="a,s,m"
        redact=input("Type a comma-seperated list of letters to redact: ")
        numToRedact=len(redact)
        print(numToRedact)

        redactList=redact.split(",")
        for i in range(len(redactList)):
            if i ==0:
                newmessage=splitString(message,redactList[i])
            else:
                newmessage=splitString(newmessage,redactList[i])
        print(newmessage)


main()


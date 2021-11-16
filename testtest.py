word="this is a phrase"
letters=[]
for i in word:
    if i.upper()== "S":
        break
        #continue
        
    else: 
        letters.append(i)
print(letters)
print(word)


#while word != 
#split and join
myString =  "This is a phrase of Kings"
myString = myString.split(" ")
print(myString)
print(myString[0][3])

myList = ["Q", "R", "S"]
print("BOO!".join(myList))
    # # while True:
    # #     if i == len(word):
    # #         break
    # #     print(word[i])
    # #     i+=i

for i in range(5):
    print(i +1, "hi")
    for j in range(3):
        print(j +1, "there")
names = ["sfds", "sds", "wsds", "sds"]
#for i in range(len(names)):
#    print(names[i])
for name in names:
    for letter in name:
        print(letter)

            # YOUR CODE STARTS HERE, each line must be indented (one tab)
    letterRemover()
    myList="mama mia here we go again".split(" ")
    print(myList)




#for i in range(len(names)):
#    print(names[i])

    for name in myList:
        for letter in name:
            if letter == "m":
                continue
            else:
                print(letter)

               

    print(myList)

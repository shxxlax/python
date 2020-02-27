a=("hello world")

print (a)

#cute me

#lists

pets=["dog","cat","fish"]
thepets=pets[1]
print(thepets)

#length & types

size=len(pets)

msg="there are " + str(size)+  " pets"

print(msg)

#loops

for x in pets:
    print("I wish I hads a " + x) 

#user input
ans=input("What kind of pet do you have?")

print("you have a " + ans)

#booleans
known = ans in pets
print("it is " +str(known) + " that I have seen a " + ans)

#branching

if known:
    msg="My friend has a " + ans
    
else:
    msg="I don't know anyone with a "+ ans
print(msg)

#dictionary

feels={"cat":"selfish","dog":"loyal","fish":"wet"}

if known:
    pre="e" if ans=="fish" else""
    msg=ans+pre + "s are very " + feels.get(ans)
else:
    msg="I don't know anyone with a "+ ans
print(msg)
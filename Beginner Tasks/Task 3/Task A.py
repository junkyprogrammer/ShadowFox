#You have a list of superheroes representing the Justice League. justice_league = ["Superman" , "Batman" , "Wonder Woman" , "Flash" , "Aquaman" ,"Green Lantern"]

#Creating a List
space = " "
justice_league = ["Superman" , "Batman" , "Wonder Woman" , "Flash" , "Aquaman" ,"Green Lantern"]
print("Meet our Justice League Team!!")
print(justice_league)
#Calculate the number of members in the Justice League.

count = len(justice_league)
#print(count)

#Adding new members into the list
print(space)
print("Batman recruited Batgirl and Nightwing in the team!")
justice_league.extend(['Batgirl', 'Nightwing'])

#Displaying the list after adding new members
print(space)
print(justice_league)

#Leader changed from Superman to Wonder Woman
print(space)
justice_league[0], justice_league[2] = justice_league[2], justice_league[0]
print("List after changing the leader",justice_league)


# remaining from task 4

# Aquaman and Flash are having conflicts, so adding Superman in between them

print(space)

print("List after adding Superman in between the conflict of Aquaman and Flash")
print(space)

justice_league[2], justice_league[3] = justice_league[3], justice_league[2]
print(justice_league)

#The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg","Shazam", "Hawkgirl", "Martian Manhunter" ,"Green Arrow".

print("Superman leaving his previous team")

justice_league.remove('Superman')
print("")
print("Superman Assbembled a new team including these new memebers : ")
print(space)

justice_league1 = ["Cyborg","Shazam", "Hawkgirl", "Martian Manhunter" ,"Green Arrow"]
print(justice_league1)

justice_league1.extend(['Superman'])


justice_league1[0], justice_league1[5] = justice_league1[5], justice_league1[0]
print(justice_league1)
print(space)


#Sorting out the list aplhabetically

print(sorted(justice_league1))
print(space)

print("Our New Leader is : Cyborg ")

## Bonus ques Answer: Our New team leader is Cyborg!

""" Solution for:  https://leetcode.com/problems/strong-password-checker/

A password is considered strong if below conditions are all met:

    It has at least 6 characters and at most 20 characters.
    It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
    It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change."""

def strongPasswordChecker(s):
    length = len(s)
    capitals = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    lowers = [chr(i) for i in range(ord('a'),ord('z')+1)]
    numbers = [chr(i) for i in range(ord('0'),ord('9')+1)]
    repeats = []
    repeats1 = str()
    repeats2 = str()
    repeats3 = str()
    caps = 0
    lows = 0
    digits = 0
    others = 0
    repeated = 0
    must_add_because_missing = 0
    could_change_because_repeats = []

    solution = 0

    for x in s:   #First Count that we have at least one of each required item
        if x in capitals:
            caps +=1
        elif x in lowers:
            lows +=1
        elif x in numbers:
            digits +=1
        else:
            others +=1   #this is an unessecary count
        repeats3 = repeats2
        repeats2 = repeats1   #update pointers to look for repeats
        repeats1 = x
        if repeats1 == repeats2 and repeats1 == repeats3:   #compare for repeats
            repeated+=1
            repeats.append(x)        #put repeats in a list
        else:
            if len(repeats) >0:      #the length of the repeat is the important number
                could_change_because_repeats.append(len(repeats)+2)  #put the length in a list
            repeats = []      #clear the list
    if len(repeats)>0:               #and one more to catch any final repeats
        could_change_because_repeats.append((len(repeats)+2))

    if caps==0:                        #update any number of missing components
        must_add_because_missing+=1
    if lows==0:
        must_add_because_missing+=1
    if digits==0:
        must_add_because_missing+=1

    if length > 20:                     #First deal with too long passwords
        while length > 20:
            while length > 20 and sum(could_change_because_repeats)>0:   #shorten the length and delete ones with repeats first
                for i,x in enumerate(could_change_because_repeats):      #easy pickings to get the 3's,6's,9's, etc
                    if (x//3>0) and (x%3==0) and (length>20):
                        could_change_because_repeats[i]-=1          #have to refer to x by list[i]
                        solution+=1
                        length-=1
                    x = could_change_because_repeats[i]             #update value of x
                    if x < 3:                                       #knock 2's and 1's to 0
                            could_change_because_repeats[i] = 0
                for i,x in enumerate(could_change_because_repeats):
                    if (x//3>0) and (x%3==1) and (length>20):       #Tackle any repeats of 4's,7's, 10's, etc
                        could_change_because_repeats[i]-=1
                        solution+=1
                        length-=1
                    x = could_change_because_repeats[i]            #update x
                    if (x//3>0) and (x%3==0) and (length>20):      #Tackle any repeats of 3's,6's,9's
                        could_change_because_repeats[i]-=1
                        solution+=1
                        length-=1
                    x = could_change_because_repeats[i]             #Tackle 2's and 1's
                    if x < 3:
                            could_change_because_repeats[i] = 0
                for i,x in enumerate(could_change_because_repeats):     #one more time!
                    if (x//3>0) and (x%3==2) and (length>20):       #Tackle any 5's, 8's, 11's, etc
                        could_change_because_repeats[i]-=1
                        solution+=1
                        length-=1
                    x = could_change_because_repeats[i]
                    if (x//3>0) and (x%3==1) and (length>20):       #Tackle any 4's, 7's, 10's
                        could_change_because_repeats[i]-=1
                        solution+=1
                        length-=1
                    x = could_change_because_repeats[i]
                    if (x//3>0) and (x%3==0) and (length>20):          #Tackle any 3's,6's,9's etc
                        could_change_because_repeats[i]-=1
                        solution+=1
                        length-=1
                    x = could_change_because_repeats[i]
                    if x < 3:                                       #Tackle any 1's and 2's
                            could_change_because_repeats[i] = 0
            if length>20:         #If there are no more repeats to deal with, just start deleting
                solution+=1
                length-=1

    elif length < 6: #password too short
        while sum([x//3 for x in could_change_because_repeats]) > 0 & length<6:
            for i,x in enumerate(could_change_because_repeats): #insert function
                if x//3 > 0 :
                    could_change_because_repeats[i]-=2  #drop 2 repeats for every 1 inserted
                    solution +=1
                    length+=1
                    if must_add_because_missing>0:   #if we need to add anyway
                        must_add_because_missing-=1  #then take it from here
                if could_change_because_repeats[i]<3:#change 2's and 1's to 0
                    could_change_because_repeats[i]=0
        while must_add_because_missing > 0 and length<6:  #If there is any elements missing, add them
            must_add_because_missing-=1
            solution+=1
            length+=1
        while length<6:       #If it is still short, add charchters to make it 6 long
            solution+=1
            length+=1

    if length <= 20 and length >= 6:     #for all normal length passwords, we change charcters, not add or delete
        while sum([x//3 for x in could_change_because_repeats])>0:  #First Tackle repeats by changing a character
            for i,x in enumerate(could_change_because_repeats):
                if x//3>0:
                    solution+=1
                    if must_add_because_missing>0:  #if any charachters are still missing,
                        must_add_because_missing-=1    #account for them in what you change
                    could_change_because_repeats[i]-=3 #-3 for changing a charachter
                if could_change_because_repeats[i]<3:   #Change 2's and 1's to 0
                    could_change_because_repeats[i]=0

        while must_add_because_missing > 0:     #if any items aren't acounted for, add them.
            must_add_because_missing-=1
            solution+=1

    return solution


strongPasswordChecker("aaaaabbbb1234567890ABA")
strongPasswordChecker('1111111111')
strongPasswordChecker("hoAISJDBVWD09232UHaaaaJEPODKNLADU1")
strongPasswordChecker("aaaabbaaabbaaa123456A")
strongPasswordChecker("1234567890123456Baaaaa")
strongPasswordChecker('aa123')
strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa")
strongPasswordChecker("ABABABABABABABABABAB1")
strongPasswordChecker('1111111111')

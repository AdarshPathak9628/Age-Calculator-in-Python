##  program to enter a dob and calculate its age.

import datetime
dob=datetime.datetime.now()
cy=dob.year
cm=dob.month
cd=dob.day
DOB=input("Enter your DOB(dd/mm/yyyy)").split("/")
print(dob)
d=int(DOB[0])
m=int(DOB[1])
y=int(DOB[2])
print(type(cd),type(d))
if cd < d:
    if(cm in [1,3,5,7,8,10,12]):
        cd=cd+31
    elif(cm in [4,6,9,11]):
        cd=cd+30
    else:
        cd=cd+28
    cm=cm-1
rd=cd-d
if(cm < m):
    cm=cm+12
    cy=cy-1
rm=cm-m
ry=cy-y
print(ry,"years",rm,"Mounth",rd,"days") 

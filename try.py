Result={}
name=[]
maths=[]
science=[]
english=[]
computer=[]
sanskrit=[]
for i in range(0,5):
    print()
    n=input("Enter student's name-> ")
    name.append(n)
    m=int(input("enter maths marks-> "))
    maths.append(m)
    s=int(input("enter science marks -> "))
    science.append(s)
    e=int(input("enter english marks -> "))
    english.append(e)
    c=int(input("enter computer marks -> "))
    computer.append(c)
    sa=int(input("enter sanskrit marks -> "))
    sanskrit.append(sa)
    Result[n]=[m,s,e,c,sa]


print("Result of students are as follows",Result)
for i in range(0,5):
    if maths[i]>maths[i-1]:
        mh=maths[i]
        nmh=name[i]
    if science[i]>science[i-1]:
        sh=science[i]
        nsh=name[i]
    if english[i]>english[i-1]:
        eh=english[i]
        neh=name[i]
    if computer[i]>computer[i-1]:
        ch=computer[i]
        nch=name[i]
    if sanskrit[i]>sanskrit[i-1]:
        sah=sanskrit[i]
        nsah=name[i]

Highest=[mh,sh,eh,ch,sah]
sub=["Maths","Science","English","Computer","Sanskrit"]
print("List of highest marks is->",Highest)
for i in range(0,5):
    print("Highest marks in",sub[i],"is",Highest[i])
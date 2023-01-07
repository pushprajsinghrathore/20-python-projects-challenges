email=input("enter your email")
if len(email)>=6:
    print("correct")
else:
    print("wrong")
if email[0].isalpha():
    if("@" in email) and ("@"==1):
        if(email[-4]==".") ^(email[-3]=="."):
            for i in email:
                if i==i.isspace():
                    k=1
                if i==i.upper():
                    j=1
                if i.isdigit():
                    continue
                elif i=="_"or i=="."or i=="@":
                    continue
                else:
                    d=1
            if k==1 or d==1 or j==1:
                print("wrong")
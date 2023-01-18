from time import * # with help this cod we import time and with
# * (star) we use all funcation of  time
def  mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:

                error=error+1
                
        except:
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay= time_e-time_s
    time_r=round(time_delay,2)
    speed=len(userinput)/time_r
    return round(speed)




import random as r # so with help of this random we have to genrate random  string
test=["In this typing speed test game using Python tutorial, you will learn how to check the speed.",
      "If you know the basics of Python and the pygame library, you can easily calculate the speed.",
      " Make the best out of this tutorial and learn from our trainer, who will give proper examples related to the speed."]
test1=r.choice(test)
print("*************typing speed **************")
print(test1)  
print()
print()
time_1=time()
# take input from users
testinput=input("Enter:  ")
time_2=time()
print('speed:',speed_time(time_s,time_e,testinput),"w/sec")
print("error:",mistake(test1,testinput))


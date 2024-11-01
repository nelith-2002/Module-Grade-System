# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

#Student ID:20230664
#Date:2023/12/04

from graphics import*
f=open("text.txt","a")
f.write("part3\n")
def file(ans_p,ans_d,ans_f,x):  #print file     
    d=x+"-"+str(ans_p)+","+str(ans_d)+","+str(ans_f)+"\n"
    f.write(d)


def check_p():     #check progress marks
    while True:
         p=input("Please enter your credits at pass: ")
         
         if p.isdigit()==True:
             if p=="0" or p=="20" or p=="40" or p=="60" or p=="80" or p=="100" or p=="120":
                   return int(p)
                   break
                   
             else:
                    print("Out Of range")
                    continue
         else:
                print("Integer required")
                continue

def check_d():     #check defer marks
    while True:
        d=input("Please enter your credit at defer: ")

        if d.isdigit()==True:
            if d=="0" or d=="20" or d=="40" or d=="60" or d=="80" or d=="100" or d=="120":
                
                   return int(d)
                   break
            else:
                      print("Out of range")
                      continue
        else:
            
                print("Integer required")
                continue
            
def check_f():     #check fail marks
    while True:
        f=input("Please enter your credit at fail: ")

        if f.isdigit()==True:
            if f=="0" or f=="20" or f=="40" or f=="60" or f=="80" or f=="100" or f=="120":
                return int(f)
                break
            
            else:
                print("Out of range")
                continue
        else:
            print("Integer required")
            continue
list_p=[]
list_pm=[]
list_dm=[]
list_e=[]

count1=0
count2=0
count3=0
count4=0
e_list=[]

while True:
    ans_p=check_p()
    ans_d=check_d()
    ans_f=check_f()
    if ans_p+ans_d+ans_f!=120:
        print("Total Incorrect")
        continue
    else:
         if ans_p==120 and ans_d==0 and ans_f==0:
             x="Progress"
             print(x)
             count1+=1
             e_list.append(count1)
             list_p.append(ans_p),list_p.append(ans_d),list_p.append(ans_f)
         elif ans_p==100 and (ans_d==0 or ans_d==20) and (ans_f==0 or ans_f==20):
             x="Progress (module trailer)"
             print(x)
             count2+=1
             e_list.append(count2)
             list_pm.append(ans_p),list_pm.append(ans_d),list_pm.append(ans_f)
         elif (ans_p==0 or ans_p==20 or ans_p==40 or ans_p==60 or ans_p==80) and (ans_d==0 or ans_d==20 or ans_d==40 or ans_d==60 or ans_d==80 or ans_d==100 or ans_d==120) and (ans_f==0 or ans_f==20 or ans_f==40 or ans_f==60):
             x="Do not Progress – module retriever"
             print(x)
             count3+=1
             e_list.append(count3)
             list_dm.append(ans_p),list_dm.append(ans_d),list_dm.append(ans_f)
         elif (ans_p==0 or ans_p==20 or ans_p==40) and (ans_d==0 or ans_d==20 or ans_d==40) and (ans_f==80 or ans_f==100 or ans_f==120):
             x="Exclude"
             print(x)
             count4+=1
             e_list.append(count4)
             list_e.append(ans_p),list_e.append(ans_d),list_e.append(ans_f)
                     
         else:
             x="Invalid"
             print(x)
         file(ans_p,ans_d,ans_f,x)
        
         while True:
             print( )
             print("Would you like to enter another set of data?")
             input_1=input("Enter 'y' for yes or 'q' to quit and view results: ")
             if input_1 in ["q","Q","Y","y"]:
                 break
         if input_1=="q" or input_1=="Q":
             break

totcount=count1+count2+count3+count4
maximum_num=max(e_list)

f.close()
win=GraphWin("Histogram",750,750)    #start graphics code
win.setBackground("#EDF2EC")

Topic=Text(Point(200,50),"Histogram Results")
Topic.setTextColor("Black")
Topic.setSize(30)
Topic.setStyle("bold")
Topic.draw(win)

subtopic_1=Text(Point(200,610),"Progress")
subtopic_1.setTextColor("Black")
subtopic_1.setSize(12)
subtopic_1.setStyle("bold")
subtopic_1.draw(win)

subtopic_2=Text(Point(310,610),"Trailer")
subtopic_2.setTextColor("Black")
subtopic_2.setSize(12)
subtopic_2.setStyle("bold") 
subtopic_2.draw(win)

subtopic_3=Text(Point(420,610),"Retriever")
subtopic_3.setTextColor("Black")
subtopic_3.setSize(12)
subtopic_3.setStyle("bold")
subtopic_3.draw(win)

subtopic_4=Text(Point(530,610),"Excluded")
subtopic_4.setTextColor("Black")
subtopic_4.setSize(12)
subtopic_4.setStyle("bold")
subtopic_4.draw(win)

r1=Rectangle(Point(150,600),Point(250,600-(520/maximum_num)*count1))
r1.setFill("#7B8997")
r1.draw(win)

r2=Rectangle(Point(260,600),Point(360,600-(520/maximum_num)*count2))
r2.setFill("#A0C689")
r2.draw(win)

r3=Rectangle(Point(370,600),Point(470,600-(520/maximum_num)*count3))
r3.setFill("dark green")
r3.draw(win)

r4=Rectangle(Point(480,600),Point(580,600-(520/maximum_num)*count4))
r4.setFill("dark red")
r4.draw(win)

num1=Text(Point(200,595-(520/maximum_num)*count1),count1)
num1.setTextColor("black")
num1.setSize(12)
num1.setStyle("bold")
num1.draw(win)

num2=Text(Point(305,595-(520/maximum_num)*count2),count2)
num2.setTextColor("black")
num2.setSize(12)
num2.setStyle("bold")
num2.draw(win)

num3=Text(Point(418,595-(520/maximum_num)*count3),count3)
num3.setTextColor("black")
num3.setSize(12)
num3.setStyle("bold")
num3.draw(win)

num4=Text(Point(528,595-(520/maximum_num)*count4),count4)
num4.setTextColor("black")
num4.setSize(12)
num4.setStyle("bold")
num4.draw(win)

totcount=Text(Point(110,710),totcount)
totcount.setTextColor("black")
totcount.setSize(15)
totcount.setStyle("bold")
totcount.draw(win)

v=Text(Point(210,710),"Outcomes in Total")
v.setTextColor("black")
v.setSize(15)
v.setStyle("bold")
v.draw(win)

print( )
output_1=0                 
while output_1<=len(list_p)-1:
 t=0
 while 3*t+2<=len(list_p)-1:
    print("Progress- ",list_p[3*t],",",list_p[3*t+1],",",list_p[3*t+2])
    t=t+1
 break

output_2=0
while output_2<=len(list_pm)-1:
    t=0
    while 3*t+2<=len(list_pm)-1:
        print("Progress(module trailer)- ",list_pm[3*t],",",list_pm[3*t+1],",",list_pm[3*t+2])
        t=t+1
    break
 
output_3=0
while output_3<=len(list_dm)-1:
    t=0
    while 3*t+2<=len(list_dm)-1:
        print("Module retriever- ",list_dm[3*t],",",list_dm[3*t+1],",",list_dm[3*t+2])
        t=t+1
    break
      
output_4=0
while output_4<=len(list_e)-1:
    t=0
    while 3*t+2<=len(list_e)-1:
        print("Exclude- ",list_e[3*t],",",list_e[3*t+1],",",list_e[3*t+2])
        t=t+1
    break
    
        
            
         
          


 
            

   

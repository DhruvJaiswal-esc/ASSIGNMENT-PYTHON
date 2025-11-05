#DHRUV JAISWAL OF SECTION F,ROLL NO-250170364
#Date-28/09/2025
#Daily Calorie Tracker CLI
import sys

print("Welcome\nThis tool is called a DAILY CALORIE TRACKER CLI\nIts function is to take your every meal's report and give you your average calorie intake\n It also checks if it is under your Basic Metabolic Rate(BMR)\n you are requested to enter your meal in characters only,your calories in numbers\nAnd the time it was taken at in format of 24 hour clock\n example: Breakfast 200  23:00")
#Welcoming the user to the tracker and explaining how it works 
meal=[]
calorie=[]
timestamp=[]

n=int(input("please enter the number of meals you are going to input currently:"))
for i in range(n): #taking input(meal,calorie,time) from the user in lists using for loop
    temp=input(f"Meal Number {i+1}:")
    meal.append(temp)
    caltemp=int(input("and its calories:"))
    calorie.append(caltemp)
    timetemp=(input("Meal was taken at:"))
    timestamp.append(timetemp)
intcalorie=[int(j) for j in calorie]#converting calorie list data into int type for smooth summation
total_calorie=sum(intcalorie)#actual summation
cal_limit=int(input("Enter your BMR Please="))
print("""\t Meal Name\t\t\tCalories\t\tMeal Taken At
------------------------------------------------------------------------------""")#printing the table in a neat manner
for i in range(n):
    print(f"\t{i+1}.{meal[i] :<12}\t\t\t{intcalorie[i]:<4}\t\t\t{timestamp[i]:<10}")#printing its contents
print("Your total calorie intake:",total_calorie)
avg_intake=float(total_calorie/n)#calculating and printing the avg calories
print(f"AVG Intake:{avg_intake:.2f}")
if(cal_limit<total_calorie):#checking if the user has gone over their recommended calories or not
    print("Warning: you have exceeded your daily calorie intake")
else:
    print("Congrats on controlling your Daily Calorie Intake,keep up the good work")
bonus=input("do you want to save this report?Answer in yes or no only")#bonus task,asking for report and making the file 
if(bonus=="yes"):
    with open("calorie_log.txt","wt") as f:#opening the file and printing all the contents in it
        print("""\t Meal Name\t\t\tCalories\t\tMeal Taken At\n------------------------------------------------------------------------------""", file=f)
        for i in range(n):
            print(f"\t{i+1}.{meal[i] :<12}\t\t\t{intcalorie[i]:<4}\t\t\t{timestamp[i]:<10}",file=f)
        print("Your total calorie intake:",total_calorie,file=f)    
        print(f"AVG Intake:{avg_intake:.2f}",file=f)
        print("Your BMR:",cal_limit,file=f)
        if(cal_limit<total_calorie):
            print("Warning: you have exceeded your daily calorie intake",file=f)
        else:
            print("Congrats on controlling your Daily Calorie Intake,keep up the good work",file=f)    
elif(bonus=="no"):
    print("program complete")
else:#making sure the user does not answer anything they should not
    print("ANSWER IN YES OR NO")
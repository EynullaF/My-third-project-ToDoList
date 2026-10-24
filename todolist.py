print("Today's goals")
goals = []
a=0

while True:
    n = input("\033[33mWrite your goal (or press ENTER to finish adding): \033[0m")
    if n != "":
        goals.append(n)
    else:
        break 

def comp(goals):
    for i in goals:
        global a
        a=a+1
        print(f'{a}.{i}')

comp(goals)
def re(goals):
    if all(word.startswith("☑") for word in goals):
        print("\033[32mYou have completed all the goals\033[0m")
        return False
    else:
        b = input("\033[31mWrite the number of the goal you completed or SPACE+ENTER to complete...\033[0m")
        try:
            if b!=" ":
                b=int(b)
                if 0<b<=len(goals):
                    b=b-1
                    goals[b] = "☑ " + goals[b]
                    comp(goals)
                else:
                    print("Try again")
            else:
                print("\033[32mYou have completed all the goals\033[0m")
                return False
        except ValueError:
            print("Try again")
                
while True:
    if re(goals) is False:
        break
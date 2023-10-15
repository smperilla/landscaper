money = 0
tools = []
win_scenario = 1000

def status():
    print(f"You have ${money}.")
    print(f"Your tools: {', '.join(tools)}")

while True:
    status()

    if money >= win_scenario and 'team' in tools:
        print("You've won the game.")
        break

    print("Make a choice:")
    print("1. Cut grass with teeth")
    print("2. Buy scissors")


    choice = input()

    if choice == "1":
        money += 1
        print("You've cut grass with your teeth.")
    
    elif choice == '2':
        if money >= 5:
            money -= 5
            tools.append('rusty scissors')
            print("You've bought rusty scissors.")
        else:
            print("You don't have enough money!")

    elif choice == '3':
        if money >= 25:
            money -= 25
            tools.append('old-timey push lawnmower')
            print("You've bought an old-timey push lawnmower.")


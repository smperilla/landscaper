money = 1000

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
    print("3. Cut grass with scissors")
    print("4. Buy old-timey push lawnmower")  
    print("5. Cut grass with old-timey push lawnmower")  
    print("6. Buy fancy battery-powered lawnmower")
    print("7. Cut grass with fancy battery-powered lawnmower")
    print("8. Hire a team of starving students")
    print("9. Cut grass with a team of starving students")



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
    
    elif  choice == '3':
        money += 5
        print("You've cut grass with rusty scissors.")

    elif choice == '4':
        if money >= 25:
            money -= 25
            tools.append('old-timey push lawnmower')
            print("You've bought an old-timey push lawnmower.")
    
    elif choice == '5':
        money += 50
        print("You've cut rass with an old-timey push lawnmower.")

    elif choice == '6':
        if money >= 250:
            money -= 250
            tools.append('fancy battery-powered lawnmower')
            print("You've bought a fancy battery-powered lawnmower.")

    elif choice == '7':
        money += 100
        print("You've cut rass with a fancy battery-powered lawnmower.")

    elif choice == '8':
        if money >= 500:
            money -= 500
            tools.append('team')
            print("You've bought a team of starving students.")
    
    elif choice == '9':
        money += 250
        print("You've cut rass with a team of starving students.")

  

    
 
    





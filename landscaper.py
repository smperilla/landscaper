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

    choice = input()

    if choice == "1":
        money += 1
        print("You've cut grass with your teeth.")


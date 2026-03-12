planetList = []
missionOver = False

while missionOver == False:
    planet = input("Enter planet name: ")
    planetList.append(planet)

    question = input("Is the mission over? (y/n): ")
    if question == "y" or question == "Y":
        missionOver = True

neighbor = input("Which planet do you want the neighbors for?: ")

print("Planets neighboring " + neighbor + ": ")

for i in range(len(planetList)):
    if planetList[i] == neighbor:
        if i - 1 >= 0:
            print("     " + planetList[i - 1])
        if i + 1 <= len(planetList) - 1:
            print("     " + planetList[i + 1])

print("Program ending...")
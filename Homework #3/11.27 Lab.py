#Rayyan Rahman ID: 1893113
def getJerseyNumber():
    # prompt for jersey number
    jerseyNumber = int(input("Enter new player's jersey number:"))  # get input
    # if jersey number is invalid
    while (jerseyNumber < 0 or jerseyNumber > 99):
        jerseyNumber = int(input("Error! Enter new player's jersey number:"))  # get input till number not valid
    return jerseyNumber


# function prompt for rating 1-9 and return its value
def getRating():
    rating = int(input("Enter player's rating:"))
    while (rating < 1 or rating > 9):
        rating = int(input("Error! Enter player's rating:"))
    return rating


# function print menu option for user and return its choice

def menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")
    choice = input("Choose an option:\n")  # get input from user
    return choice[0]  # return a char


# print roster in ascending order
# takes a dictionary as argument to print in sorted order
def printRoster(player):
    print("ROSTER")  # print roster string
    for jersey in sorted(player):  # sort by key
        # print jersey number and key
        print("Jersey number: {}, Rating: {}".format(jersey, player[jersey]))
    print("")



# function add new player to dictionary
# takes argument a dictionary which holds a jersey number and rating

def addPlayer(player):
    jerseyNumber = getJerseyNumber()  # get jersey number from function
    rating = getRating()  # get rating
    player[jerseyNumber] = rating  # add rating and jersey number


# deleteplayer function remove player input jersey number from user
# takes a argument dictionary
def deletePlayer(player):
    jerseyNumber = getJerseyNumber()
    if jerseyNumber in player:  # jersey number in player dictionary
        player.pop(jerseyNumber)  # remove that key and value from dictionary
    else:  # else print error message
        print("Jersey number not found.")


# update player function takes dictionary argument

def updatePlayer(player):
    jerseyNumber = getJerseyNumber()  # get jersey number
    if jerseyNumber in player:  # if jersey number exits in dictionary
        rating = getRating()  # get rating
        player[jerseyNumber] = rating  # and update rating
    else:  # else jersey number not found print error message
        print("Jersey number not found.")


def outputRatingPlayer(player):
    rating = getRating()  # get rating
    print('ABOVE', rating)
    for jersey in sorted(player):  # dictionary in sorted order
        if (player[jersey] > rating):  # if rating is above user input rating
            print("Jersey number: {}, Rating: {}".format(jersey, player[jersey]))
    print("")

  # print


def getPlayerInput(player):
    i = 0  # loop index i=0
    while i < 5:  # run loop from 0-5
        # prompt for jersey number
        print("Enter player {}'s jersey number:".format(i + 1),end='\n')
        jerseyNumber = int(input())
        # prompt for jersey number till did not get valid number
        while (jerseyNumber < 0 or jerseyNumber > 99):
            print("Error! Enter player {}'s jersey number:".format(i + 1),end='\n')
            jerseyNumber = int(input())
        print("Enter player {}'s rating:".format(i + 1), end='\n')
        print('')
        rating = int(input())
        while (rating < 1 or rating > 9):
            print("Error! Enter player {}'s rating:".format(i + 1), end='\n')
            rating = int(input())
        player[jerseyNumber] = rating  # add jersey number and rating to dictionary
        i += 1  # increment loop index


# main code starts from here
if __name__ == "__main__":
    player = {}  # create a empty dictionary
    getPlayerInput(player)  # add 5 player data to dictionary
    printRoster(player)  # print roster in sorted order
    while True:  # infinite loop
        choice = menu()  # get choice from user
        if choice == 'a':  # if choice is a
            addPlayer(player)  # add player data to dict
        elif choice == 'd':  # delete player
            deletePlayer(player)
        elif choice == 'u':  # update player rating
            updatePlayer(player)
        elif choice == 'r':  # print roster above rating
            outputRatingPlayer(player)
        elif choice == 'o':  # output roster in sorted
            printRoster(player)
        elif choice == 'q':  # quit program
            break
        else:
            print("Invalid choice.")
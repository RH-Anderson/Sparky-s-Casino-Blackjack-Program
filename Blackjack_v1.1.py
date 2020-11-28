### Blackjack program ###

### Author: Robert Anderson ###
### Version: 1.1
### Date: 11/28/2020

### Conventions
# Ace = 1
# Number cards = 2 through 10
# Jack = 11
# Queen = 12
# King = 13

### Rules

# Face cards are worth 10 points
# Ace can be 1 or 11
# Draw two cards. You may draw a third card and a fourth card if you wish.
# If total value of cards exceeds 21, you lose
# The dealer also draws two cards. The dealer will continue drawing if they
        # have a total value less than 17
# You win if you have a higher point value than the dealer or the dealer busts
# The dealer wins if they have a higher point value or you bust
# Ties go the dealer


### Import modules
import random, pprint


### Define continue playing variables
continueplaying = "Yes"
yeslist = ('Yes','yes','Y','y') #This tuple is also used for checking if the player wants to continue playing


### Define scorekeeping global variables and functions
wincount = 0
losecount = 0
def addwin():
    global wincount
    wincount = wincount + 1
def addloss():
    global losecount
    losecount = losecount + 1


## Define Sparky's commentary

chatlist = {    #A dictionary of different chat lists for different occasions
    'chitchat': [        #General chatting    
        "Some of the penitentaries are nicer than others",
        "Don't call me shorty",
        "Ask me about my nicknames",
        "They'll never take me alive",
        "I have friends in all kinds of places",
        "Let me tell you where I got my tattoos",
        "Don't mistake me for just a cute teddy bear",
        "I had a difficult youth",
        "I fought with the muhajideen",
        "I know what happened to Jimmy Hoffa",
        "It's a rookie mistake to leave a serial number on a gun",
        "I'm quite the ladies' bear",
        "I broke out of Alcatraz three times",
        "No one can prove I had anything to do with the Watergate break-in",
        "When they say ten years to life they usually don't mean it",
        "Raising bail is easier than you think",
        "I helped Johnny Cash write the Fulsom Prison Blues",
        "I'm a bear of international intrigue"
        ],

    'threats': [ #Threats which are interspersed with chatting and used more frequently as the player is winning
        "I have cameras watching your every move",
        "What's that you got up your sleeve",
        "Let me tell you why they call me Sparky the Knife'",
        "I may look cute, but don't cross me"
        ],

    'losing_threats': [ #Threats only used when the player is losing
        "Pay up or you'll be swimming with the fishies",
        "We find the most effective tool of coercion is warm cookies",
        "Remember you have to pay, or I'll send the boys around to break thumbs",
        "Do not accuse me of cheating"

        ]
    }


## Define chat functions

def sparkychat(wincount,losecount,likelihood, threatonly):
    #likelihood is the percent likelihood (out of 100) that the function will fire. 100 is guaranteed and 0 is impossible.
    #if True is passed to the threatonly argument, then the function simply returns a threat based on the win percentage


    def chatprint(chat_type):       #This function actually prints the chat text. The argument determines which type of chat will be printed
        selection = random.randint(0,len(chatlist[chat_type])-1)    #This line selects the index number for the chat string which will be printed, given the chat type
        print('———Sparky: ' + '"' + chatlist[chat_type][selection] + '"')


    def select_chat(p_chitchat, p_threats, p_losing_threats):    #This function selects the type of chat to print. The arguments give the likelihood with which each type of chat is selected
        i = random.randint(1,100)

        if i <= p_chitchat:
            chatprint('chitchat')
        elif i <= p_chitchat + p_threats:
            chatprint('threats')
        elif i <= p_chitchat + p_threats + p_losing_threats:
            chatprint('losing_threats')      

    if likelihood >= random.randint(1,100) and threatonly != True:
        games_played = wincount + losecount
        if games_played <= 3:   #Chat block for start of game
            select_chat(100,0,0)
        else:
            if wincount/games_played >= .6:  #Chat block for when the player is winning
                select_chat(50,50,0)
            elif wincount/games_played <= .4:  #Chat block when the player is losing
                select_chat(50,0,50)
            else:                           #Chat block for a relatively even game
                select_chat(80,20,0)               

    if threatonly == True:
        if wincount >= losecount:
            chatprint('threats')
        elif wincount < losecount:
            chatprint('losing_threats') 



### Opening Dialogue
print("Welcome to Sparky's Casino. You are playing blackjack.")
print("Please draw two cards")


### Game function (one round of blackjack)

def game():

    while True:     # This WHILE loop while be broken when the player busts, the dealer busts, or after points are compared

        
        # Defining functions
        
        def draw():         #Draws the card
            drawresult = random.randint(1,13)
            return drawresult

        def cardvalue(drawnumber):  #Assigns the value of the card
            if drawnumber >= 11:
                return 10
            else:
                return drawnumber
           

        def cardname(card):   #Assigns the name of the card
            if card == 11:
                card = "Jack"
            elif card == 12:
                card = "Queen"
            elif card == 13:
                card = "King"
            elif card == 1:
                card = "Ace"
            return str(card)


        def points(card1, card2, card3, card4):
            if card1 == 1 or card2 == 1 or card3 == 1 or card4 == 1:
                if bustcheck(card1 + card2 + card3 + card4 + 10) == True:
                    return card1 + card2 + card3 + card4
                else:
                    return card1 + card2 + card3 + card4 + 10
            else:
                return card1 + card2 + card3 + card4


        def bustcheck(pointsinput): # Checks if points exceed bust threshold
            if pointsinput > 21:
                return True
            else:
                return False


        def evaluatewinner(playercard1value, playercard2value, playercard3value, playercard4value, dealercard1value, dealercard2value, dealercard3value, dealercard4value):
            global wincount
            global losecount

            if points(playercard1value, playercard2value, playercard3value, playercard4value) > points(dealercard1value, dealercard2value, dealercard3value, dealercard4value):

                print("You have more points (" + \
                      str(points(playercard1value, playercard2value, playercard3value, playercard4value)) \
                    + " to " + \
                    str(points(dealercard1value, dealercard2value, dealercard3value, dealercard4value)) \
                    + "). You win!")
                addwin()
                print()
                sparkychat(wincount,losecount,33,False)
                
            elif points(playercard1value, playercard2value, playercard3value, playercard4value) < points(dealercard1value, dealercard2value, dealercard3value, dealercard4value):

                print("The dealer has more points (" + \
                      str(points(playercard1value, playercard2value, playercard3value, playercard4value)) \
                    + " to " + \
                    str(points(dealercard1value, dealercard2value, dealercard3value, dealercard4value)) \
                    + "). You lose.")
                addloss()
                print()
                sparkychat(wincount,losecount,33,False)

            elif points(playercard1value, playercard2value, playercard3value, playercard4value) == points(dealercard1value, dealercard2value, dealercard3value, dealercard4value):

                print("You have equal points (" + \
                      str(points(playercard1value, playercard2value, playercard3value, playercard4value)) \
                    + "). Ties go to the dealer.")
                addloss()
                print()
                sparkychat(wincount,losecount,33,False)

        
        #Drawing cards
        playercard1 = draw()
        playercard2 = draw()
        playercard3 = draw()
        playercard4 = draw()
        
        dealercard1 = draw()
        dealercard2 = draw()
        dealercard3 = draw()
        dealercard4 = draw()

        #Valuing cards
        playercard1value = cardvalue(playercard1)
        playercard2value = cardvalue(playercard2)
        playercard3value = cardvalue(playercard3)
        playercard4value = cardvalue(playercard4)

        dealercard1value = cardvalue(dealercard1)
        dealercard2value = cardvalue(dealercard2)
        dealercard3value = cardvalue(dealercard3)
        dealercard4value = cardvalue(dealercard4)

        #Naming cards
        playercard1name = cardname(playercard1)
        playercard2name = cardname(playercard2)
        playercard3name = cardname(playercard3)
        playercard4name = cardname(playercard4)

        dealercard1name = cardname(dealercard1)
        dealercard2name = cardname(dealercard2)
        dealercard3name = cardname(dealercard3)
        dealercard4name = cardname(dealercard4)       


        #Player draw option #1
        playercardsdrawn = 2
        print("You drew:")
        print(playercard1name)
        print(playercard2name)
        print("The value of your cards is " + \
              str(points(playercard1value, playercard2value, 0, 0)))
        print("")
        sparkychat(wincount,losecount,33,False)
        print("")
        print("Would you like to draw again?")
        drawdecision1 = str(input()).lower()

        if drawdecision1 in yeslist:
#        if drawdecision1 == "Yes" or drawdecision1 == "yes" or drawdecision1 == "Y" or drawdecision1 == "y":
            playercardsdrawn = 3
            print(" ")
            print("Your third card is a " + playercard3name)
            print("The total value of your hand is now " + \
                  str(points(playercard1value, playercard2value, playercard3value, 0)))

            if bustcheck(points(playercard1value, playercard2value, playercard3value, 0)) == True:
                print("You have busted!")
                print(" ")
                addloss()
                sparkychat(wincount,losecount,33,False)
                break

            #Player draw option #2
            print("")
            sparkychat(wincount,losecount,33,False)
            print("")
            print("Would you like to draw again?")
            drawdecision2 = str(input()).lower()

            if drawdecision2 in yeslist:
                playercardsdrawn = 4
                print(" ")
                print("Your fourth card is a " + playercard4name)
                print("The total value of your hand is now " + \
                      str(points(playercard1value, playercard2value, playercard3value, playercard4value)))

                if bustcheck(points(playercard1value, playercard2value, playercard3value, playercard4)) == True:
                    print("You have busted!")
                    print(" ")
                    addloss()
                    sparkychat(wincount,losecount,33,False)
                    break


        #Dealer
        dealercardsdrawn = 2
        print(" ")
        print("The dealer has drawn:")
        print(dealercard1name)
        print(dealercard2name)
#        print("The dealer has a score of " + \                     # I think I don't need these lines, they clutter up the interface for little benefit
#              str(points(dealercard1value, dealercard2value, 0, 0)))

        #Dealer draw option #1
        if points(dealercard1value, dealercard2value, 0, 0) <17:
            dealercardsdrawn = 3
            print("The dealer draws a third card: " + dealercard3name)
            if bustcheck(points(dealercard1value, dealercard2value, dealercard3value, 0)) == True:
                print("The dealer busts. You win!")
                addwin()
                print()
                sparkychat(wincount,losecount,33,False)
                break

            #Dealer draw option #2
            if points(dealercard1value, dealercard2value, dealercard3value, 0) <17:
                dealercardsdrawn = 4
                print("The dealer draws a fourth card: " + dealercard4name)
                if bustcheck(points(dealercard1value, dealercard2value, dealercard3value, dealercard4value)) == True:
                    print("The dealer busts. You win!")
                    addwin()
                    print()
                    sparkychat(wincount,losecount,33,False)
                    break



###       Check to make sure that the variables are acting correctly. This should be commented out in production.
##        print("You have drawn " + str(playercardsdrawn) + " cards")
##        print("The dealer has drawn " + str(dealercardsdrawn) + " cards")



         #Check how many cards the player and dealer have drawn and evaluate winner
        if playercardsdrawn == 2 and dealercardsdrawn == 2:
             evaluatewinner(playercard1value, playercard2value, 0, 0, dealercard1value, dealercard2value, 0, 0)            

        elif playercardsdrawn == 2 and dealercardsdrawn == 3:
             evaluatewinner(playercard1value, playercard2value, 0, 0, dealercard1value, dealercard2value, dealercard3value, 0)

        elif playercardsdrawn == 2 and dealercardsdrawn == 4:
             evaluatewinner(playercard1value, playercard2value, 0, 0, dealercard1value, dealercard2value, dealercard3value, dealercard4value)

        elif playercardsdrawn == 3 and dealercardsdrawn == 2:
             evaluatewinner(playercard1value, playercard2value, playercard3value, 0, dealercard1value, dealercard2value, 0, 0)

        elif playercardsdrawn == 3 and dealercardsdrawn == 3:
             evaluatewinner(playercard1value, playercard2value, playercard3value, 0, dealercard1value, dealercard2value, dealercard3value, 0)

        elif playercardsdrawn == 3 and dealercardsdrawn == 4:
             evaluatewinner(playercard1value, playercard2value, playercard3value, 0, dealercard1value, dealercard2value, dealercard3value, dealercard4value)

        elif playercardsdrawn == 4 and dealercardsdrawn == 2:
             evaluatewinner(playercard1value, playercard2value, playercard3value, playercard4value, dealercard1value, dealercard2value, 0, 0)

        elif playercardsdrawn == 4 and dealercardsdrawn == 3:
             evaluatewinner(playercard1value, playercard2value, playercard3value, playercard4value, dealercard1value, dealercard2value, dealercard3value, 0)

        elif playercardsdrawn == 4 and dealercardsdrawn == 4:
             evaluatewinner(playercard1value, playercard2value, playercard3value, playercard4value, dealercard1value, dealercard2value, dealercard3value, dealercard4value)



        break   #End of while loop. This is just for development, it should not
                #be reached when the program is complete

                
            

### Activating game function + replay loop

while continueplaying in yeslist:
    game()

    print("")
    print("Win count is " + str(wincount))
    print("Lose count is " + str(losecount))
    
    ### Ending Dialogue
    print("")
    print("______________________________________")
    print("")
    sparkychat(wincount,losecount,33,False)
    print("")
    print("Would you like to play again?")
    continueplaying = input().lower()
    print(" ")

winpercent = round(wincount/(losecount + wincount)*100,1)
print("You won " + str(wincount) + " times and lost " + str(losecount) + " times (" + str(winpercent) + "%)")
print("")
sparkychat(wincount,losecount,100, True)
print("")
print("Thank you for playing! Please visit again soon.")
print(" ")
print("Please press enter to exit")
input() #This should terminate the program since it doesn't do anything and there is nothing after it

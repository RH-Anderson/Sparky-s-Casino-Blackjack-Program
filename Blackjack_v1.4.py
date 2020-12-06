### Blackjack program ###

### Author: Robert Anderson ###
### Version: 1.4
### Date: 12/6/2020

### Current status: Blackjack with replacement is complete
### Future goals: Blackjack without replacement, Texas hold'em


### Conventions used in code

# Ace = 1
# Number cards = 2 through 10
# Jack = 11
# Queen = 12
# King = 13



### Blackjack rules

# Face cards are worth 10 points
# Ace can be worth 1 or 11 points
# Draw two cards. You may draw a third card and a fourth card if you wish.
# If total value of cards exceeds 21, you lose
# The dealer also draws two cards. The dealer will continue drawing if they
#       have a total value less than 17
# You win if you have a higher point value than the dealer or the dealer busts
# The dealer wins if they have a higher point value or you bust
# Ties go the dealer



### Import modules
import random, pprint


### Define variables for player interaction
continueplaying = "Yes"
yeslist = ('Yes','yes','Y','y') #This tuple is used when the player is asked if they would like to draw again or if they would like to continue playing



### Define scorekeeping global variables and functions
wincount = 0
losecount = 0
def addwin():
    global wincount
    wincount = wincount + 1
def addloss():
    global losecount
    losecount = losecount + 1



### Define Sparky's commentary

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
        "I'm a bear of international intrigue",
        "I'm wanted in 36 states"
        ],

    'threats': [ #Threats which are interspersed with chatting and used more frequently as the player is winning
        "I have cameras watching your every move",
        "What's that you got up your sleeve",
        "Let me tell you why they call me Sparky the Knife'",
        "Just remember who's casino you're in",
        "I may look cute, but don't cross me",
        "We don't like people with cards up their sleeves"
        ],

    'losing_threats': [ #Threats only used when the player is losing
        "Pay up or you'll be swimming with the fishies",
        "We find the most effective tool of coercion is warm cookies",
        "Remember you have to pay, or I'll send the boys around to break thumbs",
        "Do not accuse me of cheating"

        ]
    }


### Define chat functions

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



### Define universal game functions

def draw(game, cardlist, cardvaluelist, cardnamelist):         #Draws a card and adds it to a list, names the card, and assigns a point value based on the game
    cardlist.append(random.randint(1,13))               #Draw a card

    drawncard = cardlist[len(cardlist)-1]               #Identifies which card was drawn
    cardvaluelist.append(assignvalue(game, drawncard))  #Assigns value to card based on the game
    cardnamelist.append(assignname(game, drawncard))    #Assigns name to card based on the game

def assignvalue(game, drawncard):  #Assigns the value of the card
    if game == "blackjack":
        if drawncard >= 11:
            return 10
        else:
            return drawncard
           

def assignname(game, drawncard):   #Assigns the name of the card
    if game == "blackjack" or game == "holdem":
        if drawncard == 11:
            return("Jack")
        elif drawncard == 12:
            return("Queen")
        elif drawncard == 13:
            return("King")
        elif drawncard == 1:
            return("Ace")
        else:
            return(str(drawncard))


def points(game, cardvaluelist):
    if game == "blackjack":
        if 1 in cardvaluelist:      #This block for blackjack allows one Ace to be treated as 11 if that wouldn't result in a bust and treated as 1 otherwise
            if bustcheck(sum(cardvaluelist) + 10) == True:
                return sum(cardvaluelist)
            else:
                return sum(cardvaluelist) + 10
        else:
            return sum(cardvaluelist)



### Define game-specific functions
        #(Note: these functions have to be defined at this level instead of within the game functions since they are used in the scoring function points() )


#Blackjack:

def bustcheck(points): # Checks if points exceed bust threshold
    if points > 21:
        return True
    else:
        return False




### Opening Dialogue
print('''Welcome to Sparky's Casino. You are playing blackjack.
Please draw two cards
''')




### Game functions (one round)

def blackjack():

    while True:     # This WHILE loop while be broken when the player busts, the dealer busts, or after points are compared

        #Reset lists representing player's and dealer's hands to empty
        player_cards = []           #cards contains values from 1 through 13, representing the cards drawn
        player_card_values = []     #values contains the game-specific point value
        player_card_names = []      #names contains the names of the cards

        dealer_cards = []
        dealer_card_values = []
        dealer_card_names = []
   


        #Drawing initial cards
        draw("blackjack",player_cards,player_card_values,player_card_names)
        draw("blackjack",player_cards,player_card_values,player_card_names)

        #Player draw option #1
        print("You drew:")
        print(player_card_names[0])
        print(player_card_names[1])
        print( "The value of your cards is " + \
              str( points("blackjack",player_card_values) )  )
        print()
        sparkychat(wincount,losecount,33,False)
        print()
        print("Would you like to draw again?")
        drawdecision1 = str(input()).lower()

        if drawdecision1 in yeslist:
            draw("blackjack",player_cards,player_card_values,player_card_names)
            print()
            print("Your third card is a " + str(player_card_names[2]))
            print("The total value of your hand is now " + \
                  str( points("blackjack",player_card_values) )  )

            if bustcheck(points("blackjack",player_card_values)) == True:
                print("You have busted!")
                print(" ")
                addloss()
                sparkychat(wincount,losecount,33,False)
                break

            #Player draw option #2
            print()
            sparkychat(wincount,losecount,33,False)
            print()
            print("Would you like to draw again?")
            drawdecision2 = str(input()).lower()

            if drawdecision2 in yeslist:
                draw("blackjack",player_cards,player_card_values,player_card_names)
                print()
                print("Your fourth card is a " + str(player_card_names[3]))
                print("The total value of your hand is now " + \
                      str( points("blackjack",player_card_values) )  )

                if bustcheck(points("blackjack",player_card_values)) == True:
                    print("You have busted!")
                    print()
                    addloss()
                    sparkychat(wincount,losecount,33,False)
                    break


        #Dealer
        draw("blackjack",dealer_cards,dealer_card_values,dealer_card_names)
        draw("blackjack",dealer_cards,dealer_card_values,dealer_card_names)
        print()
        print("The dealer has drawn:")
        print(dealer_card_names[0])
        print(dealer_card_names[1])

        #Dealer draw option #1
        if points("blackjack",dealer_card_values) <17:
            draw("blackjack",dealer_cards,dealer_card_values,dealer_card_names)
            print("The dealer draws a third card: " + dealer_card_names[2])
            if bustcheck(points("blackjack",dealer_card_values)) == True:
                print("The dealer busts. You win!")
                addwin()
                print()
                sparkychat(wincount,losecount,33,False)
                break

            #Dealer draw option #2
            if points("blackjack",dealer_card_values) <17:
                draw("blackjack",dealer_cards,dealer_card_values,dealer_card_names)
                print("The dealer draws a fourth card: " + dealer_card_names[3])
                if bustcheck(points("blackjack",dealer_card_values)) == True:
                    print("The dealer busts. You win!")
                    addwin()
                    print()
                    sparkychat(wincount,losecount,33,False)
                    break


        #Evaluate winner

        def evaluatewinner(player_card_values, dealer_card_values):
            if points("blackjack",player_card_values) > points("blackjack",player_card_values):     #Player has more points
                print("You have more points (" + \
                    str( points("blackjack",player_card_values) ) \
                    + " to " + \
                    str( points("blackjack",dealer_card_values) ) \
                    + "). You win!")
                addwin()
                print()
                sparkychat(wincount,losecount,33,False)
                
            elif points("blackjack",player_card_values) < points("blackjack",player_card_values):   #Dealer has more points
                print("The dealer has more points (" + \
                    str( points("blackjack",player_card_values) ) \
                    + " to " + \
                    str( points("blackjack",dealer_card_values) ) \
                    + "). You lose.")
                addloss()
                print()
                sparkychat(wincount,losecount,33,False)
            elif points("blackjack",player_card_values) == points("blackjack",player_card_values):   #Tie goes to the dealer
                print("You have equal points (" + \
                      str( points("blackjack",player_card_values) ) \
                    + "). Ties go to the dealer.")
                addloss()
                print()
                sparkychat(wincount,losecount,33,False)


        evaluatewinner(player_card_values, dealer_card_values)
        


        break   #End of while loop. This is just for development, it should never
                #be reached when the program is complete

                
            

### Activating game function + replay loop

while continueplaying in yeslist:
    blackjack()

    print()
    print("Win count is " + str(wincount))
    print("Lose count is " + str(losecount))
    
    ### Ending Dialogue
    print()
    print("______________________________________")
    print()
    sparkychat(wincount,losecount,33,False)
    print()
    print("Would you like to play again?")
    continueplaying = input().lower()
    print()

winpercent = round(wincount/(losecount + wincount)*100,1)
print("You won " + str(wincount) + " times and lost " + str(losecount) + " times (" + str(winpercent) + "%)")
print()
sparkychat(wincount,losecount,100, True)
print("""
Thank you for playing! Please visit again soon.

Please press enter to exit""")
input() #This line terminates the program since the player's input isn't used for anything and there is nothing after it

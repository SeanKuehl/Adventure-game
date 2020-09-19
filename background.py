import random
import pygame
import sys
pygame.init()
#make the game print what event it does. Add the rest of the item effects

eventList = [['eminem', 'eminem challenges you to a rap battle', 'accept', 'try to roast him', 'decline', '3', 4], ['trump', 'you come across Donald Trump', 'insult him', 'walk by him', 'fight him', '2', 2], ['trump', 'trump appears and without warning calls you "fake news"', 'ignore him', 'tell him you are not', 'tell him to square up', '1', 2], ['deadpool', 'deadpool offers you a chimichanga', 'insult it', 'refuse it', 'take it', '3', 3], ['deadpool', 'deadpool approaches with swords out', 'fight him', 'tell him he will not', 'tell him he is strong', '3', 3], ['shrek', 'shrek tells you to leave his swamp', 'leave his swamp', 'tell him to make you', 'say nothing', '1', 6], ['shrek', 'shrek asks you what you think of donkey', 'fat', 'loud', 'funny', '3', 6], ['world', 'a sentient globe asks you what the capital of south africa is', 'portsmouth', 'cape town', 'glapton', '2', 7], ['world', 'a sentient globe asks you what the capital of egypt is', 'alexandria', 'giza city', 'cairo', '3', 7], ['world', 'a sentient globe asks you where the white house is located', 'washington state', 'washington D.C.', 'washington capitol hill', '2', 7], ['history', 'a sentient statue asks you who killed ceaser', 'pompeo', 'brutus', 'octavian', '2', 8], ['history', 'a sentient statue asks you who the first fascist was', 'benito mussolini', 'adolf hitler', 'pinochet', '1', 8], ['history', 'a sentient statue asks you who won the miracle of the marne', 'russia', 'germany', 'france', '3', 8], ['micheal bay', 'micheal bay asks you what the best part of a movie is', 'explosions', 'plot', 'characters', '1', 5], ['micheal bay', 'micheal bay asks you how much art matters in a film', 'a lot', 'it is everything', 'it does not matter', '3', 5], ['gru', 'gru appears and asks you what you think of his latest movies', 'great', 'perfect', 'evil', '3', 10], ['gru', 'gru appears and asks you how many minions he has', 'too many', 'too few', 'just enough', '1', 10], ['sonic', 'sonic appears and asks you how fast he can run', 'light speed', 'speed of sound', 'sonic speed', '2', 11], ['sonic', 'sonic appears and asks you who his nemesis is', 'Dr. Wily', 'Shadow', 'Dr. Eggman', '3', 11]]


itemList = [['dank memes', 'you find a living pile of dank memes, are they dank enough? do you take them?', 12], ['basketball', 'you find a basketball, can you pull it in his eye? can you pull it on the fly? do you want to take it?', 13], ['exam', 'you find this years upcoming exam with answers, do you take it?', 14], ['souja boy', 'you find a souja boy mixtape, could it be fire? do you take it?', 15], ['ugg boots', 'you find a pair of ugg boots, do you take them? they could come in handy.', 16], ['gum', 'you find a stick of delicious juicy fruit gum, do you take it?', 17], ['beverly wood', 'you find the principal, do you dare take her with you on your journey?', 18], ['your mother', 'you find your mother, do you dare take her with you on your journey?', 19], ['your father', 'you find your father, do you dare take him with you on your journey?', 20], ['lonzo ball', 'you come across lonzo ball, do you want him to companion you on your journey?', 21], ['selena gomez', 'you come across selena gomez, do you want her to companion you on your journey?', 22], ['kendrick lemar', 'you come across kendrick lemar, do you want him to companion you on your journey?', 23], ['potted plant', 'you come across a potted plant, do you want to take it?', 24], ['phone', 'you find a phone on the floor, do you take it?', 25], ['jordans', 'you find a pair of jordans, do you cop them?', 26], ['chromebook', 'you find a chromebook, do you take it?', 27], ['snickers bar', 'you find a snickers, do you feel like yourself? do you want to take it?', 28], ['jason mask', 'you find a jason mask, do you dare touch it?', 29], ['chucky doll', 'you find a chucky doll, do you dare take it?', 30], ['chuck norris', 'you find chuck norris, do you want his conpanionship on your journey?', 31]]

cave1MainPath = ['5']
cave1Left1Path = ['5']
cave1Left2Path = ['5']
cave1Right1Path = ['5']
cave1Right2Path = ['5']
cave2MainPath = ['5']
cave2Left1Path = ['5']
cave2Left2Path = ['5']
cave2Right1Path = ['5']
cave2Right2Path = ['5']
cave3MainPath = ['5']
cave3Left1Path = ['5']
cave3Left2Path = ['5']
cave3Right1Path = ['5']
cave3Right2Path = ['5']

currentCave = []
currentCaveSpot = []
itemEffectList = ['end game', 'move ahead 3', 'move ahead 2', 'move ahead 1', 'win game', 'change main cave', 'four events', 'three turns', 'two items', 'funny image', 'marks', 'jake']
temporaryList = []
caveSelection = 00000.0
startUp = True
screenWidth = 800
screenHeight = 400
picPosW = screenWidth / 2
picPosH = screenHeight / 2

# 0 is event, 5 is intro message, 1 is left turn 2 is right, 4 is item, 3 is left or right, 6 is loss, 7 is victory
displaySurface = pygame.display.set_mode((screenWidth, screenHeight))

#myImage = pygame.image.load('background.bmp')
#myImageRect = myImage.get_rect()
#displaySurface.blit(myImage, (picPosW - myImageRect.center[0], picPosH - myImageRect.center[1]))

#do same for all three caves
def assignVictory():
    randNum = random.randint(1,5)
    if randNum == 1:
        cave1MainPath.append(7)
        cave1Left1Path.append(6)
        cave1Left2Path.append(6)
        cave1Right1Path.append(6)
        cave1Right2Path.append(6)
        #below is cave 2
        cave2MainPath.append(7)
        cave2Left1Path.append(6)
        cave2Left2Path.append(6)
        cave2Right1Path.append(6)
        cave2Right2Path.append(6)
        #below is cave 3
        cave3MainPath.append(7)
        cave3Left1Path.append(6)
        cave3Left2Path.append(6)
        cave3Right1Path.append(6)
        cave3Right2Path.append(6)

    if randNum == 2:
        cave1MainPath.append(6)
        cave1Left1Path.append(7)
        cave1Left2Path.append(6)
        cave1Right1Path.append(6)
        cave1Right2Path.append(6)
        #below is cave 2
        cave2MainPath.append(6)
        cave2Left1Path.append(7)
        cave2Left2Path.append(6)
        cave2Right1Path.append(6)
        cave2Right2Path.append(6)
        #below is cave 3
        cave3MainPath.append(6)
        cave3Left1Path.append(7)
        cave3Left2Path.append(6)
        cave3Right1Path.append(6)
        cave3Right2Path.append(6)
    if randNum == 3:
        cave1MainPath.append(6)
        cave1Left1Path.append(6)
        cave1Left2Path.append(7)
        cave1Right1Path.append(6)
        cave1Right2Path.append(6)
        # below is cave 2
        cave2MainPath.append(6)
        cave2Left1Path.append(6)
        cave2Left2Path.append(7)
        cave2Right1Path.append(6)
        cave2Right2Path.append(6)
        # below is cave 3
        cave3MainPath.append(6)
        cave3Left1Path.append(6)
        cave3Left2Path.append(7)
        cave3Right1Path.append(6)
        cave3Right2Path.append(6)
    if randNum == 4:
        cave1MainPath.append(6)
        cave1Left1Path.append(6)
        cave1Left2Path.append(6)
        cave1Right1Path.append(7)
        cave1Right2Path.append(6)
        # below is cave 2
        cave2MainPath.append(6)
        cave2Left1Path.append(6)
        cave2Left2Path.append(6)
        cave2Right1Path.append(7)
        cave2Right2Path.append(6)
        # below is cave 3
        cave3MainPath.append(6)
        cave3Left1Path.append(6)
        cave3Left2Path.append(6)
        cave3Right1Path.append(7)
        cave3Right2Path.append(6)
    if randNum == 5:
        cave1MainPath.append(6)
        cave1Left1Path.append(6)
        cave1Left2Path.append(6)
        cave1Right1Path.append(6)
        cave1Right2Path.append(7)
        # below is cave 2
        cave2MainPath.append(6)
        cave2Left1Path.append(6)
        cave2Left2Path.append(6)
        cave2Right1Path.append(6)
        cave2Right2Path.append(7)
        # below is cave 3
        cave3MainPath.append(6)
        cave3Left1Path.append(6)
        cave3Left2Path.append(6)
        cave3Right1Path.append(6)
        cave3Right2Path.append(7)

def assignCaves(caveOn, inLoop, lastDone):
    while inLoop == True:
        caveLenRand = random.randint(13, 20)
        caveOn += 1
        if caveOn == 16:
            lastDone = False
        while caveLenRand > 0:
            caveSpotRand = random.randint(0, 100)
            if caveSpotRand >= 28 and caveSpotRand <= 100:
                caveSpotRand = '0'
            elif caveSpotRand >= 8 and caveSpotRand <= 27:
                x = ['1', '2', '3']
                caveSpotRand = random.choice(x)
            elif caveSpotRand >= 0 and caveSpotRand <= 7:
                caveSpotRand = '4'
            if caveOn == 1:
                cave1MainPath.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 2:
                cave1Right1Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 3:
                cave1Right2Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 4:
                cave1Left1Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 5:
                cave1Left2Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 6:
                cave2MainPath.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 7:
                cave2Right1Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 8:
                cave2Right2Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 9:
                cave2Left1Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 10:
                cave2Left2Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 11:
                cave3MainPath.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 12:
                cave3Right1Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 13:
                cave3Right2Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 14:
                cave3Left1Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            if caveOn == 15:
                cave3Left2Path.append(caveSpotRand)
                caveLenRand -= 1
                lastDone = True
            #caveLenRand is not decreasing, there is something wrong in the logic
            if lastDone == False:
                caveLenRand = 0
                inLoop = False



def endGame():
    caveSelection = 0.0
    open = False
    pygame.quit()
    sys.exit()


def effectCheck(caveSelection,currentCave):
    pygame.event.wait()
    effect = 0
    randomNumber = random.randint(1, 3)
    if randomNumber != 1:
        effect = itemEffectList[randomNumber]
    if effect == 'end game':
        print("this item's mystical powers have ended your life on contact. Both your adventure and your life are over")
        endGame()
    if effect == 'move ahead 3':
        if len(currentCave) > 4:
            currentCave.pop(0)
            currentCave.pop(0)
            currentCave.pop(0)
    if effect == 'move ahead 2':
        if len(currentCave) > 3:
            currentCave.pop(0)
            currentCave.pop(0)
    if effect == 'move ahead 1':
        if len(currentCave) > 2:
            currentCave.pop(0)
    if effect == 'win game':
        print("the item transports you to where you entered one of the three caves. Money surrounds you in a pile. The item is gone. This adventure has been a successful one.")
        endGame()
    if effect == 'change main cave':
        if caveSelection > 29999.0:
            caveSelection -= 1
        else: caveSelection += 1

    if effect == 'four events':
        currentCave.insert(1, 0)
        currentCave.insert(1, 0)
        currentCave.insert(1, 0)
        currentCave.insert(1, 0)

    if effect == 'three turns':
        currentCave.insert(1, 3)
        currentCave.insert(1, 2)
        currentCave.insert(1, 1)
    if effect == 'two items':
        currentCave.insert(1, 4)
        currentCave.insert(1, 4)
    if effect == 'funny image':
        picToScreen(9, True)
        userInput = input("tell me when you're done")
        picToScreen(0, False)
    if effect == 'marks':
        userInput1 = input("enter your mark from your first class last semester")
        userInput2 = input("enter your mark from your second class last semester")
        userInput3 = input("enter your mark from your third class last semester")
        userInput4 = input("enter your mark from your fourth class last semester")
        average = round(((int(userInput1) + int(userInput2) + int(userInput3) + int(userInput4)) / 4.0) * 100.0) / 100.0
        if average >= 75.0:
            print("good job, your marks are decent I guess")
        else:
            print("you realize you arn't good enough and end your own journey")
            endGame()

        if effect == 'jake':
            userInput = input("do you subscribe to jake paul")
            if userInput == "yes":
                endGame()
            else: pass


def picToScreen(image, to):
    pygame.event.wait()
    imglist = ['background.bmp', 'dean.bmp', 'trump.bmp', 'deadpool.bmp', 'eminem.bmp', 'micheal.bmp', 'shrek.bmp', 'world.bmp', 'history.bmp', 'fun.bmp', 'gru.bmp', 'sonic.bmp', 'memes.bmp', 'basketball.bmp', 'exam.bmp', 'souja.bmp', 'ugg.bmp', 'juicy.bmp', 'principal.bmp', 'mom.bmp', 'dad.bmp', 'lonzo.bmp', 'selena.bmp', 'kend.bmp', 'plant.bmp', 'phone.bmp', 'jordans.bmp', 'chrome.bmp', 'bar.bmp', 'jason.bmp', 'chucky.bmp', 'chuck.bmp']
    if to == True:
        img = imglist[image]
        myImage = pygame.image.load(img)
        myImageRect = myImage.get_rect()
        displaySurface.fill((0, 0, 0))
        displaySurface.blit(myImage, (picPosW - myImageRect.center[0], picPosH - myImageRect.center[1]))
        pygame.display.update()
        pygame.event.wait()


    if to == False:
        myImage = pygame.image.load('background.bmp')
        myImageRect = myImage.get_rect()
        displaySurface.fill((0, 0, 0))

        displaySurface.blit(myImage, (picPosW - myImageRect.center[0], picPosH - myImageRect.center[1]))
        pygame.display.update()
        pygame.event.wait()

class Event:
    def __init__(self, name, message, option1, option2, option3, correctAnswer, image, currentCave, caveSelection):
        self.name = name

        self.message = message
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.correctAnswer = correctAnswer
        self.image = image
        self.currentCave = currentCave
        self.caveSelection = caveSelection

    def loadEvent(self, name, message, option1, option2, option3, correctAnswer, image, currentCave, caveSelection):

        answer = 0
        to = True
        picToScreen(image, to)
        pygame.event.wait()
        userInput = input(message+"    "+option1+"    "+option2+"    "+option3)

        if userInput == option1:
            answer = 1
        if userInput == option2:
            answer = 2
        if userInput == option3:
            answer = 3



        if answer == correctAnswer:
            print("congratulations, you made it past "+name+" and may now continue on your path")
            image = 0
            to = False
            picToScreen(image, to)
            pygame.event.wait()
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)


        else: print(name+" has ended your journey and your life. You must restart from the begginning"), endGame()


    def loadItem(self, message, name, image, currentCave, caveSelection):

        answer = 0
        to = True
        picToScreen(image, to)
        pygame.event.wait()
        userInput = input(message+" do you want to pick it up or not pick up?")

        if userInput == "pick up":

            effectCheck(caveSelection, currentCave)



            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)
    #effect check will check for the effect of the item

        if userInput == "not pick up":
            print("you choose not to pick up the "+name+", hopefully this was a wise choice.")
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)


def caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot):
    #below is so the window does not stop responding after a few seconds
    pygame.event.wait()


    if caveSelection == 10000.0:
        currentCave = cave1MainPath

    if caveSelection == 20000.0:
        currentCave = cave2MainPath

    if caveSelection == 30000.0:
        currentCave = cave3MainPath

    #below is for first left cave of each

    if caveSelection == 10100.0:
        currentCave = cave1Left1Path

    if caveSelection == 20100.0:
        currentCave = cave2Left1Path





    if caveSelection == 30100.0:
        currentCave = cave3Left1Path

    #below is for second left cave of each
    if caveSelection == 10200.0:
        currentCave = cave1Left2Path

    if caveSelection == 20200.0:
        currentCave = cave2Left2Path

    if caveSelection == 30200.0:
        currentCave = cave3Left2Path

    #below is for first right cave of each


    if caveSelection == 12000.0:
        currentCave = cave1Right1Path

    if caveSelection == 22000.0:
        currentCave = cave2Right1Path

    if caveSelection == 32000.0:
        currentCave = cave3Right1Path

    #below is for second right cave of each

    if caveSelection == 14000.0:
        currentCave = cave1Right2Path

    if caveSelection == 24000.0:
        currentCave = cave2Right2Path

    if caveSelection == 34000.0:
        currentCave = cave3Right2Path



    #below is for combinations for cave1

    if caveSelection == 12100.0:
        currentCave = cave1MainPath

    if caveSelection == 14100.0:
        currentCave = cave1Right1Path

    if caveSelection == 12200.0:
        currentCave = cave1Left1Path

    #below is for combinations for cave2

    if caveSelection == 22100.0:
        currentCave = cave1MainPath

    if caveSelection == 24100.0:
        currentCave = cave1Right1Path

    if caveSelection == 22200.0:
        currentCave = cave1Left1Path

    #below is for combinations for cave3


    if caveSelection == 32100.0:
        currentCave = cave1MainPath

    if caveSelection == 34100.0:
        currentCave = cave1Right1Path

    if caveSelection == 32200.0:
        currentCave = cave1Left1Path

    #below are overflow combinations for cave1


    if caveSelection == 16000.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    if caveSelection == 10300.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    if caveSelection == 14200.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    #below are the overflow combinations for cave2


    if caveSelection == 26000.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    if caveSelection == 20300.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    if caveSelection == 24200.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    #below are the overflow combinations for cave3

    if caveSelection == 36000.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    if caveSelection == 30300.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    if caveSelection == 34200.0:
        print("you have taken too long and attracted too much attention. You do not live to see the other side of the corner.")

    #when both are maxed out it is impossible/gamebreaking

    #anymore than three turns is counted as out of the cave system
    #below is for turns that would go out of a cave system ( use a around the world system )


    #above is for main caves while below is for first right off shoots
    #first below is to pop cavespot from list and second is chance of event



    if len(currentCave) < 1:
        print("you have reached the end of the cave")
    else: currentCaveSpot = int(currentCave.pop(0))

    if currentCaveSpot == 0:
        randomNumber = random.randint(1,2)
        if randomNumber != 1:

            userInput = input("you move forth but nothing happens, do you wish to 'press on'?")
            if userInput == "press on":
                caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)
        if randomNumber == 1:
            randomNumber = random.randint(0,18)
            temporaryList = eventList[randomNumber]
            Event.loadEvent(Event, name = str(temporaryList[0]), message = str(temporaryList[1]), option1 = str(temporaryList[2]), option2 = str(temporaryList[3]), option3 = str(temporaryList[4]), correctAnswer = int(temporaryList[5]),  image = temporaryList[6], currentCave = currentCave, caveSelection = caveSelection)



    if currentCaveSpot == 5:
        userInput = input("you enter the cave, hopefully it will lead to riches and not lead to your demise. Do you want to 'go forward' just tell me")
        caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)



    # 0 is event, 1 is possible left turn, 2 is possible right turn, 3 is possible left or right, 4 is item, 5 is empty(text producing only
    if currentCaveSpot == 2:
        userInput = input("you notice that there's a way to go right here, but should you take it? Do you want to 'go forward' or 'turn right'?")
        if userInput == "go forward":
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)
        elif userInput == "turn right":
            caveSelection += 2000.0
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)



    if currentCaveSpot == 1:
        userInput = input("you notice that there's a way to go left here, but should you take it? do you want to 'go forward' or 'turn left'?")
        if userInput == "go forward":
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)
        elif userInput == "turn left":
            caveSelection += 100.0
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)



    if currentCaveSpot == 3:
        userInput = input("you notice that there's a way to go both left and right, but should you go either instead of continueing forward? Do you want to 'go forward', 'turn left', or 'turn right'?")
        if userInput == "go forward":
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)
        elif userInput == "go left":
            caveSelection += 100.0
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)
        elif userInput == "go right":
            caveSelection += 2000.0
            caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)




    if currentCaveSpot == 4:
        randomNumber = random.randint(1,4)
        temporaryList = itemList[randomNumber]
        Event.loadItem(Event, name = str(temporaryList[0]), message=str(temporaryList[1]), image = temporaryList[2], currentCave = currentCave, caveSelection = caveSelection)
#option1 will actuall be effect
    if currentCaveSpot == 6:
        print("after all you have been through, it was in vain. You reach a dead end and all the creatures you have previously encountered decend on you and end both your journey and your life")
        #picToScreen() show defeat image
        endGame()



    if currentCaveSpot == 7:
        print("after all you have been through, all the trials and findings and dark corners turned and walked past in hope, something happened. You reach a pool of riches and a torch lit way out of the cave. You did it, you won, congratulations.")

def start(caveSelection, startUp, image, currentCaveSpot):

    if startUp == True:
        to = True
        assignCaves(0, True, False)
        picToScreen(image, to)
        assignVictory()

        userInput = input("You journey out from your quiet village to go on an adventure. You come accross three caves, which one do you want to enter? Cave1, cave2, or cave3?")
        if userInput == "cave1" or userInput == "cave2" or userInput == "cave3":


            if userInput == "cave1":
                caveSelection += 10000.0


            elif userInput == "cave2":
                caveSelection += 20000.0


            elif userInput == "cave3":
                caveSelection += 30000.0


            else: print("sorry, that was not an adventure worthy responce")

    startUp = False

    caveMove(caveSelection, currentCave, temporaryList, userInput, currentCaveSpot)
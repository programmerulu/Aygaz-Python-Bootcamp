import random
from art import *
import os
import configure as conf
import sys


totalComputerScore=0;
totalPlayerScore=0;
WhoWon=None; #True=PlayerWon, False=ComputerWon

def clear_screen():
    if os.name == 'nt':  # if operating system is Windows.. 
        os.system('cls')
    else:  # For another operating systems....
        os.system('clear')

options = conf.AllOptions["Default"]


def MainMenu():
    global options,totalComputerScore,totalPlayerScore,WhoWon
    print(text2art("Rock Paper Scissors"))
    while True:
        if(totalComputerScore!=0 or totalPlayerScore!=0):
            print(f"Scores =>  {playerName}:{totalPlayerScore} | {totalComputerScore}:{conf.computerName}")
        print(f"The morale of {conf.computerName} playing a game = {conf.computerProbability*100:.2f}%")
        print(f"""
        Hello, I'm {conf.computerName}. I hope we are going to have an enjoyable time with each other.
        
        [1] Let's start
        [2] About the game
        [3] Customize the game
        [4] Exit
        """)
        print(text2art("By Emrecan Ulu"))

        choice = input("Enter a option: ").strip()

        if choice == '1':
            StartGame()
        elif choice == '2':
            AboutGame()
        elif choice == '3':
            CustomizeGame()
        elif choice == '4':
            print("Exiting....")
            sys.exit()
        else:
            clear_screen()
            print("Invalid Number")
    

def StartGame():
    global options, totalComputerScore, totalPlayerScore, WhoWon
    if not (conf.computerProbability < 0.35):
        clear_screen()
        print(text2art("Game is starting :)"))
        PlayerScore = 0
        ComputerScore = 0

        if WhoWon is not None:
            if WhoWon:
                print(f"{conf.computerName}: {conf.PlayerWonLastimeSentences[random.randint(0, len(conf.PlayerWonLastimeSentences) - 1)]}")
            else:
                print(f"{conf.computerName}: {conf.ComputerWonLastTimeSentences[random.randint(0, len(conf.ComputerWonLastTimeSentences) - 1)]}")

        print(f"These are the options you can choose.\nIf you don't know what these mean, I suggest you read the 'About the game' section.\n {options}\n")
        print("Remember, whoever gets 3 wins. I will make you regret it :)\n")
        while PlayerScore < 3 and ComputerScore < 3:
            MyChoice = ' '.join(input("Choose= ").strip().lower().title().split())
            if MyChoice != "":
                if MyChoice in options:
                    chooseOfComputer = options[random.randint(0, len(options) - 1)]
                    if MyChoice == chooseOfComputer:
                        print("--------------------------------------")
                        print(f"{playerName} => {PlayerScore} | {ComputerScore} <= {conf.computerName}\n")
                        print(f"{playerName} => {MyChoice} | {chooseOfComputer} <= {conf.computerName}")
                        print(conf.DrawSentences[random.randint(0, len(conf.DrawSentences) - 1)])
                        print("--------------------------------------")
                    elif (MyChoice == options[0] and chooseOfComputer == options[1]) or \
                         (MyChoice == options[1] and chooseOfComputer == options[2]) or \
                         (MyChoice == options[2] and chooseOfComputer == options[0]):
                        PlayerScore += 1
                        print("--------------------------------------")
                        print(f"{playerName} => {PlayerScore} | {ComputerScore} <= {conf.computerName}\n")
                        print(f"{playerName} => {MyChoice} | {chooseOfComputer} <= {conf.computerName}")
                        print(conf.LoseSentences[random.randint(0, len(conf.LoseSentences) - 1)])
                        print("--------------------------------------")
                    else:
                        ComputerScore += 1
                        print("--------------------------------------")
                        print(f"{playerName} => {PlayerScore} | {ComputerScore} <= {conf.computerName}\n")
                        print(f"{playerName} => {MyChoice} | {chooseOfComputer} <= {conf.computerName}")
                        print(conf.WinSentences[random.randint(0, len(conf.WinSentences) - 1)])
                        print("--------------------------------------")

                    if ComputerScore == 3:
                        totalComputerScore += 1
                        WhoWon = False
                        print(f"*****DEFEAT*****\n{conf.computerName} won!")
                        print(f"Total =>  {playerName}:{totalPlayerScore} | {totalComputerScore}:{conf.computerName}")
                        conf.computerProbability = min(conf.computerProbability + random.uniform(0.1, 0.2), 1.0)
                        print(f"{conf.computerName}'s spirits lifted.")
                        print(f"Possibility of current play = {conf.computerProbability*100:.2f}%\n")
                        print(f"{conf.VictorySentences[random.randint(0, len(conf.VictorySentences) - 1)]}")
                        while True:
                            choiceAgain = input("How about playing again? Y/N => ").strip()
                            if choiceAgain in ["N", "n", "No", "no"]:
                                clear_screen()
                                print("See you next time")
                                MainMenu()  
                                return
                            elif choiceAgain in ["Y", "y", "Yes", "yes"]:
                                if random.random() > conf.computerProbability:
                                    clear_screen()
                                    print(f"{conf.computerName} = {conf.LeavingTheGameSentences[random.randint(0, len(conf.LeavingTheGameSentences) - 1)]}")
                                    MainMenu() 
                                    return
                                StartGame()
                                break
                            else:
                                print("Hey Dude! Are you kidding with me? You must enter Y (Yes) or N (No)")
                    elif PlayerScore == 3:
                        totalPlayerScore += 1
                        WhoWon = True
                        print(f"*****VICTORY*****\n{playerName} won!")
                        print(f"Total =>  {playerName}:{totalPlayerScore} | {totalComputerScore}:{conf.computerName}")
                        conf.computerProbability = max(conf.computerProbability - random.uniform(0.1, 0.2), 0.1)
                        print(f"{conf.computerName} is upset.")
                        print(f"Possibility of current play = {conf.computerProbability*100:.2f}%\n")
                        print(f"{conf.DefeatedSentences[random.randint(0, len(conf.DefeatedSentences) - 1)]}")
                        while True:
                            choiceAgain = input("Do you want to play again? Y/N => ").strip()
                            if choiceAgain in ["N", "n", "No", "no"]:
                                clear_screen()
                                print("See you next time")
                                MainMenu()  
                                return
                            elif choiceAgain in ["Y", "y", "Yes", "yes"]:
                                if random.random() > conf.computerProbability:
                                    clear_screen()
                                    print(f"{conf.computerName} = {conf.LeavingTheGameSentences[random.randint(0, len(conf.LeavingTheGameSentences) - 1)]}")
                                    MainMenu()  
                                    return
                                StartGame()
                                break
                            else:
                                print("Hey Dude! Are you kidding with me? You must enter Y (Yes) or N (No)")
                else:
                    print("Invalid value")
    else:
        clear_screen()
        print(f"{conf.computerName} = {conf.DemoralizationSentences[random.randint(0, len(conf.DemoralizationSentences) - 1)]}")

def AboutGame():
    clear_screen()
    print(text2art("About the game"))
    print(f"""
    Hello my gamer friend, I'm {conf.computerName}. 
    I am very assertive in the game of {options[0]} {options[1]} {options[2]} and I believe I can beat you. 
    If you do not know the game, you can read the instructions below and learn the rules of the game. 
    You can even change the values ​​in the rock-paper-scissors game as you wish from the "Customize the game" tab. 
    Now that you know the rules of the game, how about playing a game with me, my friend :)
    
    *The one who scores 3 wins the game
    
    *My morale is very important, sometimes I may refuse to play with you, 
    especially when my morale percentage is low, the possibility of me refusing to play with you will increase. 
    If I have less than 35% morale, you won't be able to play another game with me. 
    I admit I have a bit of a whiny personality :)

    *The superiority of each element over each other is as follows:
    
    {options[0]} > {options[1]} 
    {options[0]} < {options[2]}
    {options[1]} > {options[2]}
    """)

    while True:
        print("""
        [1] Let's start
        [2] Back""")

        choice = input("Choose= ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                clear_screen()
                StartGame()
                break
            elif choice == 2:
                clear_screen()
                MainMenu()  
                break
            else:
                print("Invalid number")
        else:
            print("You mustn't enter string or null value")

def CustomizeGame():
    clear_screen()
    print(text2art("Customize the game"))
    global options 
    while True: 
        print(f"""
        [1] Elements library
        [2] Change {conf.computerName}'s name
        [3] Change {conf.computerName}'s morale
        [4] Back
        """)

        while True:
            choice = input("Choose= ")
            if choice.isdigit() and choice != "":
                if choice == "1":
                    clear_screen()
                    print(text2art("Element Library"))
                    print("""
                    Welcome to the element library, my friend. If you're bored with the default elements, don't worry. 
                    I prepared beautiful elements for you. Let's choose one :)
                    """)

                    

                    for i, (key, values) in enumerate(conf.AllOptions.items()):
                        print(f"[{i + 1}] {key}: {', '.join(values)}")

                    while True:
                        choiceElement_input = input("SET A LIBRARY= ")
                        if choiceElement_input.isdigit() and choiceElement_input != "":
                            choiceElement = int(choiceElement_input)
                            choiceElement -= 1
                            if 0 <= choiceElement < len(conf.AllOptions):
                                selected_key = list(conf.AllOptions.keys())[choiceElement]
                                options = conf.AllOptions[selected_key]
                                clear_screen()
                                print(f"{selected_key}: {', '.join(options)} was successfully set")
                                MainMenu()
                                break
                            else:
                                print("Please choose a valid number.")
                        else:
                            print("You mustn't enter a string or null value")
                elif choice == "2":
                    clear_screen()
                    print(text2art(":("))
                    print(f"""
                    Are you really going to change my name? However, I loved you as {conf.computerName}, 
                    but that doesn't really matter. It would be a pleasure to compete with you under a different name, 
                    my beautiful friend :(
                    """)

                    while True:
                        newName = input("Set a new name= ")
                        if newName != "":
                            conf.computerName = newName.capitalize()
                            clear_screen()
                            print(f"New name was set as {newName}")
                            MainMenu()
                            break 
                        else:
                            print("You must enter a new name")
       
                elif choice == "3":
                    clear_screen()
                    print(text2art(f"{conf.computerProbability*100:.1f}%"))
                    print("""
                            Changing my morale? Why is there such a feature? I think the software developer 
                            who made this was angry because he couldn't lower my morale :)
                            """)
                    while True:
                        newProbability_input = input("Set= %").strip()
                        # if newProbability_input.isdigit() and newProbability_input != "":
                        try:
                            newProbability = float(newProbability_input)
                            if 0 <= newProbability <= 100:
                                conf.computerProbability = newProbability / 100
                                clear_screen()
                                print(f"New morale was set as {newProbability}")
                                MainMenu()
                                break
                            else:
                                print("You must enter morale between 0 and 100")
                        except ValueError:
                            print("You mustn't enter a string or null value")
             
                elif choice=="4":
                    clear_screen()
                    MainMenu();
                    break
                else:
                    print("Invalid number")
            else:
                print("You mustn't enter a string or null value")



def tas_kagit_makas_EMRECAN_ULU():
    global playerName
    while True:
        playerName = input("Enter your name= ")
        if playerName !="":
            MainMenu();
        else:
            print("Enter your name please")



if(__name__=="__main__"):
    tas_kagit_makas_EMRECAN_ULU();


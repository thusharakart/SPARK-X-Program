from Models.team import Team
from abc import ABC, abstractmethod
from typing import Final
import random


'''
Abastract Base Class 
- controlls the match
'''

class MatchController(ABC):

    @abstractmethod
    def createTeams(self, teams):
        pass

    @abstractmethod
    def bat(self, battingTeam, targetScore):
        pass

    # get the team who won the toss with a random boolean
    def __tossCoin(self, teams):

        tossWonTeam = teams[0] if random.getrandbits(1) else teams[1]
        tossWonTeam.setHasWonToss(True)

        tossLossTeam = teams[1] if teams[0].getHasWonToss() else teams[0]

        # considering the team who won the toss will bat first
        print("\nTeam " + tossWonTeam.getName() + " won the toss.")

        return [tossWonTeam, tossLossTeam]

    def __announceWinner(self, targetScore, secondScore, tossWonTeam, tossLossTeam):

        # winner anounce at the end of the game
        print("*" * 8 + " Game Over !!! " + "*" * 8 + '\n')

        # Check for the winning team
        if (targetScore > secondScore):
            print("Team " + tossWonTeam.getName() + " has won the match by " +
                    str(targetScore - secondScore) + " runs.")
        elif (targetScore < secondScore):
            print("Team " + tossLossTeam.getName() + " has won the match by " +
                    str(secondScore - targetScore) + " runs.")
        else:
            print("Match is drawn")
        
        print('\n' + "*" * 31 + '\n')


    def getUserInput(self):

        print("Press key 'P'/'p' to play!:" , end = " ")
        usr_input = input().strip()

        # consider the user input untill valid input comes
        while((not usr_input) or (usr_input != 'p' and usr_input != 'P')):
            print("Invalid input. Please try again.")
            usr_input = input().strip()

    def play(self):

        try:
            teams = []

            self.createTeams(teams)

            tossWonTeam, tossLossTeam = self.__tossCoin(teams)
            
            targetScore = self.bat(tossWonTeam, -1)

            secondScore = self.bat(tossLossTeam, targetScore)

            self.__announceWinner(targetScore, secondScore, tossWonTeam, tossLossTeam)

        except Exception as e:
            print("Oops! Error Occured.", e)



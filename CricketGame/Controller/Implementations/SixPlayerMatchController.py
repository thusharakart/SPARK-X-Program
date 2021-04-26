'''
    Derived Child Class from the MatchController Class
    - controlls a six player match between two teams
'''
from typing import Final
from Controller.matchController import MatchController
from Models.team import Team

class SixPlayerMatchController(MatchController):

    NO_OF_TEAMS: Final[int] = 2
    NO_OF_PLAYERS: Final[int] = 6
    NO_OF_OVERS: Final[int] = 5
    NO_OF_BALLS: Final[int] = 3
    OUT: Final[str] = "OUT"
    BOWLED_OUT: Final[str] = "BOWLED_OUT"
    CAUGHT_OUT: Final[str] = "CAUGHT_OUT"
    
    def createTeams(self, teams):
        for i in range(self.NO_OF_TEAMS):
            print("Enter team " + str(i + 1) + " name : ")

            usr_input = input().strip()

            while((not usr_input) or usr_input in [team.getName() for team in teams]):

                if usr_input:
                    print("Team name should be unique")

                print("Enter a valid name : ")
                usr_input = input().strip()

            team = Team(usr_input, self.NO_OF_PLAYERS)
            teams.append(team)
        
    def __displayScoreBoard(self, ball, battingTeam):

        overs = "(overs/balls): ({0}/{1})".format((ball+1) //
                                                    self.NO_OF_BALLS, (ball+1) % self.NO_OF_BALLS)
        teamSummery = battingTeam.getSummery()

        # print the score board
        print("Score Board : " + str(overs) + " " + teamSummery)

        if ((ball+1) % self.NO_OF_BALLS == 0 and ball != 0):
            print("End Of The Over!")

        print()

    def bat(self, battingTeam, targetScore):

        print("Team " + battingTeam.getName() + " is batting now.\n")

        totNoOfBalls = self.NO_OF_OVERS * self.NO_OF_BALLS

        player = battingTeam.getNextPlayer()

        for ball in range(totNoOfBalls):

            super().getUserInput()
            result = player.bat()

            print()
            # If the result was 5 that considered as a BOWLED_OUT
            # If the result was 7 that considered as a CAUGHT_OUT
            if result == 5 or result == 7:
                player.setStatus(self.OUT)
                player.setWicketTakenBy(
                    self.BOWLED_OUT if result == 5 else self.CAUGHT_OUT)
                print("Player " + player.getName() + " is out!",
                      "Umpire : " + player.getWicketTakenBy())

                player = battingTeam.getNextPlayer()

                if not player:
                    print("All out for team " + battingTeam.getName())
                    break
                # initialize the result with 0
                result = 0
            else:
                # check for the dot ball(zero runs)
                print("Dot Ball" if result == 0 else (str(result) +
                                                      " runs were scored by the player " + player.getName()))
                player.updateScore(result)

            battingTeam.updateScore(result)

            self.__displayScoreBoard(ball, battingTeam)

            if (targetScore > -1 and battingTeam.getTotalScore() > targetScore):
                break

        return battingTeam.getTotalScore()
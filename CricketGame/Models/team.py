
from Models.player import Player
from typing import Final

class Team:

    BATTING: Final[str] = "BATTING"
    _players = []

    def __setPlayers(self, noOfPlayers):
        self._players = []
        for i in range(noOfPlayers):
            player = Player(str(i+1))
            self._players.append(player)

    def __init__(self, name, noOfPlayers):
        self._name = name
        self._totalScore = 0
        self._totalWickets = -1
        self._currentBatman = -1
        self._hasWonToss = False
        self.__setPlayers(noOfPlayers)
    
    
    def getName(self):
        return self._name
    
    def getTotalScore(self):
        return self._totalScore
    
    def getTotalWickets(self):
        return self._totalWickets
    
    def getHasWonToss(self):
        return self._hasWonToss
    
    def setHasWonToss(self, hasWonToss):
        self._hasWonToss = hasWonToss

    def getNextPlayer(self):
        self._currentBatman+=1
        self._totalWickets+=1
        if self._currentBatman >= len(self._players):
            return None
        nextPlayer = self._players[self._currentBatman]
        nextPlayer.setStatus(self.BATTING)
        return nextPlayer

    def updateScore(self, result):
        self._totalScore += result

    def getSummery(self):
        return "(score/wickets): " + str(self._totalScore) + "/" + str(self._totalWickets)
        
        
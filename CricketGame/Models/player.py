
import random


class Player:

    def __init__(self, name):
        self._name = name
        self._score = 0
        self._wicketType = ""
        self._status = ""

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setScore(self, score):
        self._score = score

    def getScore(self):
        return self._score

    def setWicketTakenBy(self, wicketTakenBy):
        self._wicketTakenBy = wicketTakenBy

    def getWicketTakenBy(self):
        return self._wicketTakenBy

    def setWicketType(self, wicketType):
        self._wicketType = wicketType

    def getWicketType(self):
        return self._wicketType

    def setStatus(self, status):
        self._status = status

    def getStatus(self):
        return self._status

    def updateScore(self, result):
        self._score += result

    def bat(self):
        return random.randint(0, 7)

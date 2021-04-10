import sys
sys.path.append("..")
from CricketGame.Controller.matchController import SixPlayerMatchController


if __name__ == "__main__":
    controller = SixPlayerMatchController()
    controller.play()

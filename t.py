from AndroidBase import AndroidBase
from Screen import Screen
import time

android = AndroidBase()
android.PullScreenShot()

screen = Screen()
r = screen.findFavoriteText()
screen.click()
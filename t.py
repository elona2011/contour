from AndroidBase import AndroidBase
from Screen import Screen
import time

android = AndroidBase()
android.getDeviceIds()
android.PullScreenShot()

screen = Screen()
r = screen.findPng('./wechat/1080/longTxt.png')
# r = screen.findFavoriteText()
screen.click()
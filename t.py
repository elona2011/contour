from AndroidBase import AndroidBase
from Screen import Screen
import time

# android = AndroidBase()
# android.getDeviceIds()
# android.PullScreenShot()

screen = Screen('8GH0220409022730')
r = screen.findRedPoint()
# r = screen.findFavoriteText()
screen.click()
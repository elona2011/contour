from Screen import Screen
from AndroidBase import AndroidBase
import time

screen = Screen()
android = AndroidBase()

def thumb():
    time.sleep(5)
    r = screen.findRedPoint()
    if r == True:
        screen.click()

        time.sleep(3)

        r = screen.findVideoBlock()
        if r:
            screen.click()
            time.sleep(10)
            android.RollingUpLittle()

            r = screen.findPng('./wechat/1080/thumbIcon.png')
            if r:
                # 点击thumb
                screen.click()
                time.sleep(2)
                r = screen.findPng('./wechat/1080/commentIcon.png')
                if r:
                    # 点击comment
                    screen.click()
                    time.sleep(3)
                    screen.thumbComment()
                    time.sleep(2)
                    r = screen.findPng('./wechat/1080/replyButton.png')
                    if r:
                        # 发送评论
                        screen.click()
                        time.sleep(3)
                        screen.return2()
                        r = screen.matchUserIcon()
                        if r:
                            # 长按头像
                            screen.clickLong()
                            time.sleep(3)
                            screen.sendReply()
                            time.sleep(3)
                            r = screen.findPng('./wechat/1080/sendButton.png')
                            if r:
                                # 发送回复
                                screen.click()
                                time.sleep(3)
                                screen.return1()
                    else:
                        screen.return4()
                else:
                    screen.return2()
            else:
                # 没找到，返回
                screen.return2()
        else:
            screen.return1()

while True:
    thumb()
    thumb()
    thumb()
    time.sleep(30)
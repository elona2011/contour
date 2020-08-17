from Screen import Screen
from AndroidBase import AndroidBase
import time

screen = Screen()
android = AndroidBase()
width = android.width


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

            r = screen.findPng('./wechat/'+str(width)+'/thumbIcon.png')
            if r:
                print('点击thumb')
                screen.click()
                time.sleep(2)
                r = screen.findPng('./wechat/'+str(width)+'/commentIcon.png')
                if r:
                    print('点击comment')
                    screen.click()
                    time.sleep(3)
                    screen.thumbComment()
                    time.sleep(2)
                    r = screen.findPng('./wechat/'+str(width)+'/replyButton.png')
                    if r:
                        print('发送评论')
                        screen.click()
                        time.sleep(3)
                        screen.return2()
                        r = screen.matchUserIcon()
                        if r:
                            print('长按头像')
                            screen.clickLong()
                            time.sleep(3)
                            screen.sendReply()
                            time.sleep(3)
                            r = screen.findPng('./wechat/'+str(width)+'/sendButton.png')
                            if r:
                                print('发送回复')
                                screen.click()
                                time.sleep(3)
                                screen.return2()
                    else:
                        screen.return4()
                else:
                    screen.return2()
            else:
                print('没找到thumb，返回')
                screen.return2()
        else:
            screen.return1()

if width != 1080 and width != 720:
    print('分辨率'+str(width)+'，不支持，联系开发')
else:
    while True:
        thumb()
        thumb()
        thumb()
        thumb()
        thumb()
        thumb()
        thumb()
        thumb()

        m=300
        print('休息'+str(m)+'秒')
        time.sleep(m)
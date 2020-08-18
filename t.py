from AndroidBase import AndroidBase
from Screen import Screen
import time

android = AndroidBase()
android.PullScreenShot()

screen = Screen()
r = screen.findVideoBlock()
if r:
    screen.click()
    time.sleep(10)
    android.RollingUpLittle()

    r = screen.findPng('./wechat/'+str(android.width)+'/thumbIcon.png')
    if r:
        print('点击thumb')
        screen.click()
        time.sleep(2)
        r = screen.findPng('./wechat/'+str(android.width)+'/commentIcon.png')
        if r:
            print('点击comment')
            screen.click()
            time.sleep(3)
            screen.thumbComment()
            time.sleep(2)
            r = screen.findPng('./wechat/'+str(android.width)+'/replyButton.png')
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
                    r = screen.findPng('./wechat/'+str(android.width)+'/sendButton.png')
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
# r = screen.findPng('./wechat/'+str(android.width)+'/thumbIcon.png')
# screen.click()
# screen.findVideoBlock()
# screen.matchUserIcon()
# screen.clickLong()
# screen.clickLong()
# r = screen.findComment()
# if r:
#     # 点击comment
#     screen.click()
#     time.sleep(3)
#     screen.thumbComment()
#     time.sleep(2)
#     r = screen.findReplyButton()
#     if r:
#         screen.click()
#     else:
#         screen.return4()
# else:
#     screen.return2()

# r = screen.findReplyButton()
from Screen import Screen
from AndroidBase import AndroidBase
import time

screen = Screen()
android = screen.AndroidBase
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
            time.sleep(10) # 看视频
            android.RollingUpLittle()

            r = screen.findPng('./wechat/'+str(width)+'/thumbIcon.png')
            if r:
                print('点击thumb')
                screen.click()
                r = screen.findPng('./wechat/'+str(width)+'/commentIcon.png')
                if r:
                    print('点击comment')
                    screen.click()
                    screen.thumbComment()
                    time.sleep(2)
                    r = screen.findPng('./wechat/'+str(width)+'/replyButton.png')
                    if r:
                        print('发送评论')
                        screen.click()
                        screen.return2()
                        r = screen.findPng('./wechat/'+str(width)+'/plusButton.png')
                        if r:
                            print('点击plus')
                            screen.click()
                            r = screen.findPng('./wechat/'+str(width)+'/favoriteButton.png')
                            if r:
                                print('点击favorite')
                                screen.click()
                                r=screen.findFavoriteText()



                            else:
                                print('未找到favorite')
                                screen.return1()
                        else:
                            print('未找到plus')
                            screen.return1()




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
                                print('未找到回复按钮')
                                screen.return1()
                        else:
                            print('未找到用户头像')
                            screen.return1()
                    else:
                        print('没找到replyButton，返回')
                        screen.return4()
                else:
                    print('没找到comment，返回')
                    screen.return2()
            else:
                print('没找到thumb，返回')
                screen.return2()
        else:
            print('没找到视频号')
            screen.return1()
    else:
        print('没找到红点')

if width != 1080 and width != 720:
    print('分辨率'+str(width)+'，不支持，联系开发')
else:
    while True:
        try:
            thumb()
            time.sleep(10)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print('出异常了，重启中。。。')
            print(e)
            time.sleep(5)
            android.ClickReturn()
            time.sleep(5)
            android.ClickReturn()
            time.sleep(5)
            android.ClickReturn()
            time.sleep(5)
            android.ClickReturn()
            time.sleep(5)
            android.ClickReturn()
            time.sleep(5)
            android.WX()
            time.sleep(10)
        
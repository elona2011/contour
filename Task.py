from Screen import Screen
from AndroidBase import AndroidBase
import time


class Task():
    def __init__(self, id):
        self.screen = Screen(id)
        self.android = self.screen.AndroidBase
        self.width = self.android.width

    def clickFavorite(self, name):
        r = self.screen.findPng(
            './wechat/'+str(self.width)+'/favoriteButton.png')
        if r:
            print('点击favorite')
            self.screen.click()
            r = self.screen.findPng('./wechat/'+str(self.width)+'/'+name)
            if r:
                print('点击'+name)
                self.screen.click()
                r = self.screen.findPng(
                    './wechat/'+str(self.width)+'/favoriteSend.png')
                if r:
                    print('点击favorite发送')
                    self.screen.click()
                    time.sleep(3)
                    return True
                else:
                    print('未找到favorite发送')
            else:
                print('未找到'+name)
        else:
            print('未找到favorite')
        return False

    def thumb(self):
        time.sleep(5)
        r = self.screen.findRedPoint()
        if r == True:
            self.screen.click()

            time.sleep(3)

            r = self.screen.findVideoBlock()
            if r:
                self.screen.click()
                time.sleep(10)  # 看视频
                self.android.RollingUpLittle()

                r = self.screen.findPng(
                    './wechat/'+str(self.width)+'/thumbIcon.png')
                if r:
                    print('点击thumb')
                    self.screen.click()
                    r = self.screen.findPng(
                        './wechat/'+str(self.width)+'/commentIcon.png')
                    if r:
                        print('点击comment')
                        self.screen.click()
                        self.screen.thumbComment()
                        time.sleep(2)
                        r = self.screen.findPng(
                            './wechat/'+str(self.width)+'/replyButton.png')
                        if r:
                            print('发送评论')
                            self.screen.click()
                            self.screen.return2()
                            r = self.screen.findPng(
                                './wechat/'+str(self.width)+'/plusButton.png')
                            if r:
                                print('点击plus')
                                self.screen.click()
                                r = self.clickFavorite('longTxt.png')
                                if r:
                                    r = self.clickFavorite('favoriteVideoText.png')
                                    if r:
                                        self.android.OneClick(
                                            2, self.screen.height/4)
                                        r = self.screen.matchUserIcon()
                                        if r:
                                            print('长按头像')
                                            self.screen.clickLong()
                                            time.sleep(3)
                                            r = self.screen.findPng(
                                                './wechat/'+str(self.width)+'/sendButton.png')
                                            if r:
                                                print('发送回复')
                                                self.screen.click()
                                                time.sleep(3)
                                                self.screen.return2()
                                            else:
                                                print('未找到回复按钮')
                                                self.screen.return1()
                                        else:
                                            print('未找到用户头像')
                                            self.screen.return1()
                                    else:
                                        self.screen.return3()
                                else:
                                    self.screen.return3()
                            else:
                                print('未找到plus')
                                self.screen.return1()

                        else:
                            print('没找到replyButton，返回')
                            self.screen.return4()
                    else:
                        print('没找到comment，返回')
                        self.screen.return2()
                else:
                    print('没找到thumb，返回')
                    self.screen.return2()
            else:
                print('没找到视频号')
                self.screen.return1()
        else:
            print('没找到红点')


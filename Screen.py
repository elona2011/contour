import cv2
import numpy as np
from AndroidBase import AndroidBase
import time
from random import randrange


class Screen():
    def __init__(self,id):
        self.img = './Tmp01.png'
        self.img_rgb = cv2.imread(self.img)
        self.img2 = cv2.imread(self.img)
        self.AndroidBase = AndroidBase(id)
        self.width = self.AndroidBase.width
        self.height = self.AndroidBase.height
        self.threshold = 0.7
        self.point = [0, 0]

    def thumbComment(self):
        comments = ('66666', '/:strong/:strong/:strong', '666/:strong/:strong/:strong',
                    'good/:strong/:strong/:strong', '/:sun/:sun/:sun', '[KeepFighting]')
        self.AndroidBase.Text(comments[randrange(len(comments))])

    # def sendReply(self):
        # replys = ('已完播点赞三连，请回我朋友圈第一条视频号', '已人工完播点赞评论，请回我朋友圈第一条视频', '已点赞评论三连，请回我朋友圈第一个视频')
        # self.AndroidBase.Text(replys[randrange(len(replys))])

    def findPng(self, png):
        self.getImg()
        yes, loc = self.AndroidBase.MatchImg(png)
        self.point = loc
        # self.addRect(loc, './wechat/1080/replyButton.png')
        return yes

    def findVideoBlock(self):
        self.getImg()
        yes, loc = self.AndroidBase.MatchImg(
            './wechat/'+str(self.width)+'/videoText.png')

        if yes:
            print('找到视频号', loc)
            if loc[1] < self.AndroidBase.height/2:
                self.AndroidBase.Rolling(
                    loc[0], loc[1], loc[0], self.AndroidBase.height*4/5)
                self.getImg()
                yes, loc = self.AndroidBase.MatchImg(
                    './wechat/'+str(self.width)+'/videoText.png')

            self.point = loc
            self.findUserIcon()
        return yes

    # 平移累加
    def findUserIcon(self):
        preNum = 0
        x0, y0, x1, y1 = 0, 0, 0, 0
        for i in range(self.point[1], 0, -1):
            line = self.img_rgb[i]
            num = 0
            for ii in range(self.point[0]):
                n = line[ii]
                if n[0] != 237 or n[1] != 237 or n[2] != 237:
                    num = num+1
            if preNum == 0:
                preNum = num
            elif num > preNum+30:
                y1 = i
                preNum = num
            elif num < 20:
                y0 = i
                break
        img = self.img_rgb[y0:y1, 0:self.AndroidBase.width]
        img = cv2.transpose(img)
        preNum = 0
        for i in range(0, self.point[0]):
            line = img[i]
            num = 0
            for ii in range(len(line)):
                n = line[ii]
                # print(n)
                if n[0] != 237 or n[1] != 237 or n[2] != 237:
                    num = num+1
            if num > preNum+30:
                x0 = i
                preNum = num
            elif num < preNum - 30:
                x1 = i
                break
        self.PointUserIcon = [(x0+x1)/2, (y0+y1)/2]
        self.userIcon = self.img_rgb[y0:y1, x0:x1]
        cv2.imwrite("TmpUserIcon.png", self.userIcon)

        print(self.PointUserIcon)

    def matchUserIcon(self):
        self.getImg()
        yes, loc = self.AndroidBase.MatchImg2(self.userIcon)
        print(yes,loc)
        if yes == False:
            self.AndroidBase.Rolling(2, self.height/5, 2, self.height*4/5)
            self.getImg()
            yes, loc = self.AndroidBase.MatchImg2(self.userIcon)
        if yes == True:
            self.point = loc
        # self.addRect(loc, './wechat/1080/replyButton.png')
        return yes

    def findRedPoint(self):
        self.getImg()
        hsv = cv2.cvtColor(self.img_rgb, cv2.COLOR_BGR2HSV)

        lower_red0 = np.array([0, 160, 240])
        upper_red0 = np.array([0, 175, 255])
        lower_red1 = np.array([0, 160, 240])
        upper_red1 = np.array([0, 175, 255])

        mask0 = cv2.inRange(hsv, lower_red0, upper_red0)
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        res = cv2.bitwise_and(self.img_rgb, self.img_rgb, mask=mask0 | mask1)
        imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        # self.showImg(imgray)
        contours, hierarchy = cv2.findContours(
            imgray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = [a for a in contours if a.size > 40]
        self.contours = contours
        if len(contours) > 0:
            print("找到新消息群", contours[-1][0][0])
            self.point = contours[-1][0][0]
            if self.point[1] > self.height * 7 / 8:
                return False
            else:
                return True
        else:
            return False
        # print('contours',(contours))
        # imgContour = cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
        # self.showImg(imgContour)

    def findFavoriteText(self):
        self.getImg()
        p = []
        pre = 0
        for i in range(self.height):
            line = self.img_rgb[i]
            num = 0
            for n in line:
                if n[0] == 237 and n[1] == 237 and n[2] == 237:
                    num = num+1
            if num < 100 and num < pre - 500:
                p.append(i)
            pre = num
            if len(p) > 4:
                break
        self.point = (500, p[1]+10)
        return True

    def return1(self):
        self.AndroidBase.ClickReturn()
        time.sleep(4)

    def return2(self):
        self.AndroidBase.ClickReturn()
        time.sleep(4)
        self.AndroidBase.ClickReturn()
        time.sleep(4)

    def return3(self):
        self.AndroidBase.ClickReturn()
        time.sleep(3.5)
        self.AndroidBase.ClickReturn()
        time.sleep(4)
        self.AndroidBase.ClickReturn()
        time.sleep(4)

    def return4(self):
        self.AndroidBase.ClickReturn()
        time.sleep(4)
        self.AndroidBase.ClickReturn()
        time.sleep(3.7)
        self.AndroidBase.ClickReturn()
        time.sleep(3.1)
        self.AndroidBase.ClickReturn()
        time.sleep(4)

    def click(self):
        self.AndroidBase.OneClick(self.point[0]+8, self.point[1]+8)
        cv2.rectangle(self.img2, (self.point[0], self.point[1]),
                      (self.point[0] + 20, self.point[1] + 20), (7, 249, 151), 2)
        cv2.imwrite("Tmp02.png", self.img2)
        time.sleep(3)

    def clickLong(self):
        print('long',self.point)
        self.AndroidBase.LongClick(self.point[0]+28, self.point[1]+28)

    def getImg(self):
        self.AndroidBase.PullScreenShot()
        self.img_rgb = cv2.imread(self.img)
        self.img2 = cv2.imread(self.img)

    def addRect(self, loc, path):
        template = cv2.imread(path, 0)
        w, h = template.shape[::-1]
        cv2.rectangle(
            self.img_rgb, loc, (loc[0] + w, loc[1] + h), (7, 249, 151), 2)
        self.showImg(self.img_rgb)

    def showImg(self, img):
        cv2.namedWindow("output", cv2.WINDOW_NORMAL)
        cv2.imshow('output', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
import datetime
import os
import time
import numpy as np
import cv2
import subprocess
from threading import Thread
from multiprocessing import Process
from AndroidBase import AndroidBase

# 分辨率
resolution = "1080"  # 1080 or 720
# 图标存放目标
dir_root = "wechat"
# 图标名
main_tongxunlu = 'main_tongxunlu.png' # 主菜单，通信录
main_faxian    = 'main_faxian.png'    # 主菜单，发现
main_me        = 'main_me.png'        # 主菜单，我
zan_rukou      = 'zan_rukou.png'      # 点赞，入口
zan_icon       = 'zan_icon.png'       # 点赞，图标
zan_text       = 'zan_text.png'       # 点赞，文字
zan_quxiao     = 'zan_quxiao.png'     # 点赞，取消
zan_pinglun    = 'zan_pinglun.png'    # 点赞，评论
zan_fasong     = 'zan_fasong.png'     # 点赞，发送
pyq_fanhui     = 'pyq_fanhui.png'     # 朋友圈，返回键图标
pyq_text       = 'pyq_text.png'       # 朋友圈，文字
pyq_xiangji    = 'pyq_xiangji.png'    # 朋友圈，相机图标

class WeChatBase():

    # 启动初始化
    def __init__(self):
        self.FaildCnt = 0
        self.myClient = AndroidBase()
        self.myClient.dir_root = dir_root + "/" + resolution # 指定图标存放目录

    # 启动微信
    def LaunchWeChat(self):
        cmd = 'adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI'
        self.myClient.SendCommand(cmd)

    # 点击“发现” -> "朋友圈"
    def EnterMoment(self):
        self.myClient.OneClick(int(self.myClient.width*5/8), int(self.myClient.height*19/20))
        self.myClient.Sleep(1)
        self.myClient.OneClick(int(self.myClient.width*5/8), int(self.myClient.height*1/5))

    # 重启微信
    def ReLaunchWechat(self):
        self.LaunchWeChat()
        self.Sleep(1)
        self.ClickReturn()
        self.Sleep(1)
        self.ClickReturn()
        self.Sleep(1)
        self.ClickReturn()
        self.LaunchWeChat()

    # 检查是否在主菜单下
    def CheckIsMain(self):
        result = self.myClient.CompareThree(main_tongxunlu, main_faxian, main_me)
        return result

    # 检查是否在朋友圈状态下
    def CheckIsMoment(self):
        result = self.myClient.CompareTwo(pyq_text, pyq_xiangji)
        return result

    # 检查是否黑屏
    def CheckIsLocked(self):
        # TODO
        return False

    # 点赞
    def ClickLike(self):

        # 截图
        self.myClient.PullScreenShot()

        # 查找待点赞的朋友圈
        yes1, max_loc1 = self.myClient.MatchImg(zan_rukou)

        if yes1:
            print(u"找到朋友圈消息，坐标" + str(max_loc1))
            # 点开赞框
            print(u"查看是否赞过")
            self.myClient.OneClick(max_loc1[0], max_loc1[1])
            self.myClient.Sleep(0.5)
            self.myClient.PullScreenShot()
            yes2, max_loc2 = self.myClient.MatchImg(zan_text)
            yes3, max_loc3 = self.myClient.MatchImg(zan_quxiao)

            # 查看是否赞过
            if yes2 :
                print(u"未赞过，准备点赞")
                self.myClient.OneClick(max_loc2[0], max_loc2[1])
                print(u"点赞成功")
            #取消赞操作
            # elif yes3:
            #     LogPrint(u"已经赞过，取消")
            #     self.OneClick(max_loc2[0]+10, max_loc2[1]+10)
            # 忽略
            else :
                print(u"已经赞过，忽略")
                self.myClient.OneClick(max_loc1[0], max_loc1[1])
        else:
            print(u"未发现最新朋友圈消息")

        return True
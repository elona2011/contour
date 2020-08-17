class Img():
     # 找匹配图标
    def MatchImg(self, Target):
        # 原始图片
        img_rgb = cv2.imread(ScreenShotFileName)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        # 比对模板图片
        temp_url = self.dir_root + "/" + Target
        #print(temp_url)
        template = cv2.imread(temp_url, 0)
        # 获取模板图片尺寸
        w, h = template.shape[::-1]
        # 比对操作
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        # 比对结果坐标
        loc = np.where( res >= self.threshold)
        #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) # 找到最大值和最小值
        #print(cv2.minMaxLoc(res))
        #print(loc)

        # 描绘出外框
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
        # 保存识别目标后的图
        cv2.imwrite(ScreenShotDetected, img_rgb)

        # 检查比对结果
        for pp in loc:
            # 如果不为空，说明有比对成果的内容
            if len(pp) :
                #print ("Yes")
                #print(pp)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) # 找到最大值和最小值
                #print (max_loc)
                return True, max_loc
            else:
                #print ("Empty")
                return False, []
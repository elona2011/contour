from Screen import Screen
from AndroidBase import AndroidBase
from Task import Task
import time
import subprocess
import threading
import traceback

cmd = 'adb devices'
pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
r = pi.stdout.read().decode('utf-8').split('\n')
r = r[1:-2]
rr = []
for n in r:
    rr.append(n.split('\t')[0])
print(rr)


class myThread (threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        print("Starting " + self.id)
        newtask(self.id)


def newtask(id):
    task = Task(id)

    if task.width != 1080 and task.width != 720:
        print('分辨率'+str(task.width)+'，不支持，联系开发')
    else:
        while True:
            try:
                task.thumb()
                time.sleep(10)
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print('出异常了，重启中。。。')
                print(e)
                traceback.print_exc()
                time.sleep(5)
                task.android.ClickReturn()
                time.sleep(5)
                task.android.ClickReturn()
                time.sleep(5)
                task.android.ClickReturn()
                time.sleep(5)
                task.android.ClickReturn()
                time.sleep(5)
                task.android.ClickReturn()
                time.sleep(5)
                task.android.WX()
                time.sleep(10)


for n in rr:
    try:
        thread = myThread(n)
        thread.start()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)
        traceback.print_exc()


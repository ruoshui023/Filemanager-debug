import sys
import time

import uiautomator2 as u2

# avd_serial: emulator-5554

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)



    d.app_start("com.amaze.filemanager.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.amaze.filemanager.debug":
            break
        time.sleep(2)
    wait()


    #点击召唤侧边栏，然后点击settings
    out = d(description="Navigate up").click()
    if not out:
        print("Success: 召唤侧边栏")
    wait()

    out = d(resourceId="com.amaze.filemanager.debug:id/design_menu_item_text", text="Settings").click()
    if not out:
        print("Success: 点击settings")
    wait()

    #进入security

    out = d.xpath(
        '//*[@resource-id="com.amaze.filemanager.debug:id/recycler_view"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 点击security")
    wait()

    # 点击password

    out = d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/recycler_view"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 点击password")
    wait()

    out = d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_5"]/android.widget.TextView[1]').click()
    if not out:
        print("Success: 键盘输入")
    wait()

    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击ok")
    wait()

    #点击按钮返回
    out = d(description="Navigate up").click()
    if not out:
        print("Success: 返回")
    wait()
    out = d(description="Navigate up").click()
    if not out:
        print("Success: 返回")
    wait()
    #进入文件夹中的文件

    out =  d.xpath(
        '//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 点击先创建的文件")
    wait()


    out =  d(resourceId="com.amaze.filemanager.debug:id/properties").click()
    if not out:
        print("Success: 点击三个点")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[6]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 点击加密")
    wait()

    #打勾然后点击ok
    out = d(resourceId="com.amaze.filemanager.debug:id/checkbox_use_aze").click()
    if not out:
        print("Success: 打勾")
    wait()

    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: ok")
    wait()
   #点击新创建的加密文件，然后crash
    out =   d.xpath(
        '//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()

    if not out:
        print("Success: crash")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
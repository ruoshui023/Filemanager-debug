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

    #点击+新建文件夹
    out = d(resourceId="com.amaze.filemanager.debug:id/sd_main_fab").click()
    if not out:
        print("Success: 点击‘+’新建")
    wait()

    #点击folder
    out = d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/menu_new_folder"]/android.widget.ImageButton[1]').click()
    if not out:
        print("Success: 点击folder")
    wait()

    #点击键盘输入  键盘输入的脚本不确定对不对，这里仿照网上例子输入y
    out = d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_5"]/android.widget.TextView[1]').click()
    if not out:
        print("Success: 点击y键盘输入")
    wait()

    #点击创建create
    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击create")
    wait()

    #进入新建文件夹
    out = d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 进入新建文件夹")
    wait()
    #新建文件，命名同样为y
    out = d(resourceId="com.amaze.filemanager.debug:id/sd_main_fab").click()
    if not out:
        print("Success: 点击‘+’新建")
    wait()

    out = d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/menu_new_file"]/android.widget.ImageButton[1]').click()
    if not out:
        print("Success: 选择file类型")
    wait()

    out = d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_5"]/android.widget.TextView[1]').click()
    if not out:
        print("Success: 点击y键盘输入")
    wait()

    #点击创建create
    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击create")
    wait()


    #点击召唤侧边栏，然后点击recent
    out = d(description="Navigate up").click()
    if not out:
        print("Success: 召唤侧边栏")
    wait()

    out = d(resourceId="com.amaze.filemanager.debug:id/design_menu_item_text", text="Recent files").click()
    if not out:
        print("Success: 点击recent")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
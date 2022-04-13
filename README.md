Pytest+Appium+AndroidStudio
==

**Test Mobile Apps.**\
**Installing the appium on Windows.**

In this case written  how to install Appium on **Windows 10** and how to run a simple python test.
I describe here all my steps, step by step, to successfully install all programs and libraries and create a simple
example of testing a mobile app.
The general principles of using **Appium** are the same as in **Selenium**.

_Prerequisites: **Python3** is already installed._

###Steps for installing and using Appium.

In this video shown the basic installation steps:\
**_https://youtu.be/5rUIT9KxheE_**

Step 1.
- Download **JDK** version 8 from official website:\
_https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html_ \
- Install the **JDK 8**(_in my case, the **JDK 8** version is jdk-8u202-windows-x64_).

Step 2.
- Download **Android SDK** from official website:
_https://developer.android.com/studio_
- Create the 'androidSDK' folder on the C disk(_C:\androidSDK_).
- Install the **Android SDK**.\
_The path to install the program C:\androidSDK.
(for more information about the installation steps, see the YouTube video above.)_

Step 3.

**Need to configurate environment variables:**
- Click 'Start'
- Enter 'Advanced system settings'(_or right click by 'This PC' and choice 'Advanced system settings_')
- In the advanced tab, click on 'Environment Variables'
- In the system variables form, check `JAVA_HOME` variable name. If it doesn't exist, create new way(_click 'NEW'_),
In the 'Variable name' enter: `JAVA_HOME`,
In the 'Variable value' enter the way to your installed jdk folder, in my case: _C:\Program Files\Java\jre1.8.0_202_.
If `JAVA_HOME` already created, check the way(_need path to version JDK8_).
- Create new way(click 'NEW'), 'Variable name' enter: `ANDROID_HOME`, 'Variable value' enter the way to your
installed AndroidSDK folder (_the path: C:\androidSDK_)
- Choice `Path`(in the system variables)
  - Click 'Edit'
  - Add 5 new values:
      - %JAVA_HOME%\bin
      - %ANDROID_HOME%
      - %ANDROID_HOME%\tools
      - %ANDROID_HOME%\platform-tools
      - %ANDROID_HOME%\build-tools
  - Click 'OK'
- Click 'OK'

Step 4.
- Download **Appium** from official website:
_http://appium.io_
- Install **Appium**.

Step 5.
- Create python project (_for example in PyCharm_).
- Create the virtual environment:\
    `py -m venv venv`
- Run the virtual environment:\
    `.\venv\Scripts\activate`
- Install library:\
    `pip install Appium-Python-Client`

Step 6.
- Download wikipedia app for android from internet(_*.apk format_). 

Step 7.
- Run **Android Studio**(_Android SDK_).
- Click 'Tools' in the menu bar, click a 'Device Manager'.
- Click 'Create device'.\
You can to choice any mobile option. (_My options: Pixel 2 Api, Android 9.0)._
- Run virtual mobile (_Launch this AVD in the emulator_).

Step 8.
- Create in the python project a folder. The name folder is 'app', but can choose another name.
- Paste wikipedia.apk file there.
- Install wikipedia on virtual mobile: just drag and drop *.apk file to the screen virtual mobile.

Step 9.
- Run **Appium Server GUI**.
- Click 'start server'.

Step 10.
- Create python file, for example: test_appium_wiki_app.py
- Enter the code there (_code look in the test_appium_wiki_app.py_).
- Perform the test.

###Addition.
For searching/using in Appium the locators like in the selenium need to use UI Automator.
Look this program in: _C:\androidSDK\tools\bin\uiautomatorviewer.bat_
When open the page in virtual mobile, in 'uiautomatorviewer' click 'Device Screenshot'.\
After that you'll be able to parse this page-screenshot.

Sources which I used:\
_https://youtu.be/5rUIT9KxheE_
_https://www.youtube.com/playlist?list=PLWIBmxdTr81dDEZRiNxoy55dIDWtMyOoc_
_https://programmersought.com/article/90436050032/_
_https://pypi.org/project/Appium-Python-Client/_
_https://appium.io/docs/en/about-appium/intro/#introduction-to-appium_


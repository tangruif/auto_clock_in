# auto_clock_in
## requirements
  * python3
    * package selenium
  * chromium-browser
  * chromium-chromedriver
## quick start
  * install chrome
    ``` bash
    sudo apt-get install  chromium-browser chromium-chromedriver
    ```
  * install python package selenium
    *assume that python3 and related pip3 are available
    ``` bash
    pip3 install selenium
    ```
  * edit password.conf
    ``` bash
    line 1: write down your student ID
    line 2: write down your password
    ```
  * edit email_msg.conf
    ``` bash
    line 1: your qq email address
    line 2: the authrization code of your qq email
    line 3: the reciever of the warning email's address
    ```
  * python3 autoClockIn.py
    * check whether the auto clock in succeed
  * add python3 autoClockIn.py to crontab

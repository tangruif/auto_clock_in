# auto_clock_in
#### requirements
  * python3
    * package selenium
  * chromium-browser
  * chromium-chromedriver
#### quick start
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
    First line: write down your student ID
    Second line: write down your password
  * python3 autoClockIn.py
    * check whether the auto clock in succeed
  * add python3 autoClockIn.py to crontab

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time
import os

# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式
opt.set_headless()
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-gpu')
opt.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面


#指定chrom的驱动
#执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
driver = webdriver.Chrome('/usr/bin/chromedriver', options = opt)

#get 方法 打开指定网址
driver.get('https://app.bupt.edu.cn/ncov/wap/default/index')

try:
    id = ""
    passwd = ""
    with open(os.path.dirname(__file__) + "/password.conf") as f:
        id = f.readline()
        passwd = f.readline()
    # 登录
    userId = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input')
    userId.send_keys(id)
    
    password = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input');
    password.send_keys(passwd)
    
    # 点击登录按钮
    log_in_button = driver.find_element_by_xpath('//*[@id="app"]/div[3]');
    ActionChains(driver).click(log_in_button).perform()
    
    time.sleep(2);
    
    # 获取所在地址
    area = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/input')
    ActionChains(driver).click(area).perform()
    time.sleep(2)
    print(area.get_attribute('value'))
    
    # 点击提交
    submit = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a')
    ActionChains(driver).click(submit).perform()
    
    time.sleep(2)
    
    alert = driver.find_element_by_xpath('//*[@id="wapcf"]/div/div[1]')
    print(alert.text)
    print(driver.find_element_by_xpath('//*[@id="wapcf"]').get_attribute('style'))
    
    # 确认提交
    confirm = driver.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]')
    ActionChains(driver).click(confirm).perform()
    
    time.sleep(2)
    
    #print(driver.find_element_by_xpath('//*[@id="wapcf"]').get_attribute('style'))
    print('success')
except Exception as e:
    print("error")
    import myemail
    myemail.sendWarning(str(e))

#最后退出浏览器
driver.quit()

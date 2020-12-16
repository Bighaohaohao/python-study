'''
Author: your name
Date: 2020-11-12 16:51:39
LastEditTime: 2020-11-13 10:46:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudent\Python_Test\Taobaogo.py
'''
# !/usr/bin/env python
# coding=utf-8
# 淘宝秒杀脚本，密码登录版
from selenium import webdriver
from selenium.webdriver import  ActionChains
from selenium.webdriver.chrome.options import Options
import datetime,time

def auto_buy(params):
    print('.........................start.........................')
    chrome_options = Options()
    #打开注释就可以开启无头模式
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options, executable_path=r''+params['driverpath'] )
    driver = webdriver.Chrome(options=chrome_options, executable_path=r''+params['driverpath'] )
    driver.get("https://login.taobao.com/member/login.jhtml")
    driver.implicitly_wait(5)
    driver.find_element_by_id('fm-login-id').send_keys(params['mobile'])
    driver.find_element_by_id('fm-login-password').send_keys(params['passward'])
    time.sleep(1)
    driver.maximize_window()
    draggable = driver.find_element_by_id('nc_1_n1z')
    # #利用js将定位到的元素拖动到可见区域
    driver.execute_script("arguments[0].scrollIntoView();", draggable)
    ActionChains(driver).click_and_hold(draggable).perform()
    # 拖动
    ActionChains(driver).move_by_offset(xoffset=300, yoffset=0).perform()
    ActionChains(driver).release().perform()
    driver.find_element_by_css_selector('#login-form > div.fm-btn > button').click()
    driver.find_element_by_css_selector('#mc-menu-hd').click()

    if not driver.find_element_by_css_selector('#J_SelectAll1').is_selected():
        driver.find_element_by_css_selector('#J_SelectAll1').click()
    print('....................确认购物车商品，等待下单...........................')
    while True:
        now = datetime.datetime.now()
        if now > datetime.datetime.strptime(params['order_time'],'%Y-%m-%d %H:%M:%S'):
            btn=driver.find_element_by_id('J_Go')
            for i in range(1,20):
                try:
                    #淘宝每隔一段时间结算按钮点击次数都会不同，可能也是为防止程序操作设置的
                    driver.find_element_by_css_selector('#submitOrderPC_1 > div.wrapper > a.go-btn').click()
                    print('第'+str(i)+'次点击')
                    break
                except:
                    btn.click()
            driver.quit()
            input('抢单成功，尽快付款，按任意键退出：')
            break
if __name__ == "__main__":
    params={'mobile':'','passward':'','order_time':'','driverpath':''}
    params['driverpath'] = input("请输入chromedriver.exe绝对路径:")
    params['mobile'] = input("请输入淘宝手机号:")
    params['passward'] = input("请输入淘宝账号密码:")
    params['order_time'] =input("请输入抢购时间，格式如(2020-11-12 18:00:00):")
    try:
        auto_buy(params)
    except:
        input('抢单失败，确认下输入是否错误，按任意键退出：')

    print('.........................end.........................')

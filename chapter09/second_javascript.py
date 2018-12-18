# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/16  17:03
# @Author : Noob
# @File   : second_javascript.py

from selenium import webdriver
import unittest
import time

class JavaScriptTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def testJavaScript(self):
        driver = self.driver
        driver.get('https://www.baidu.com/')
        #
        driver.execute_script('alert(1);')
        alert = driver.switch_to.alert
        # 弹窗内文本
        print(alert.text)
        # 右上角x按钮或取消按钮
        # alert.dismiss()
        # 确认按钮
        alert.accept()
        time.sleep(3)
        #
        driver.execute_script('confirm("who are you?");')
        confirm = driver.switch_to.alert
        print(confirm.text)
        # confirm.dismiss()
        confirm.accept()
        time.sleep(3)
        #
        driver.execute_script('var name = prompt("who are you:"); document.write(name)')
        prompt = driver.switch_to.alert
        print(prompt.text)
        prompt.send_keys('noobzeng')
        prompt.accept()
        # prompt.dismiss()
        time.sleep(3)

        el = driver.find_element_by_id('kw')
        el.send_keys('大角虫 Lily')
        el.submit()
        el_next = driver.find_element_by_xpath('//a[contains(text(), "下一页")]')
        #print(el_next.text)
        #el_next.click()
        # driver.find_element_by_xpath('//*[@id="con-ar"]/div[2]/div/div/div[2]/a').click()
        time.sleep(3)

        #
        # 拖到底部
        driver.execute_script("var q=document.documentElement.scrollTop=10000")
        time.sleep(3)
        # 拖到顶部
        driver.execute_script('var q=document.documentElement.scrollTop=0')
        time.sleep(3)
        #
        driver.execute_script('var q=document.documentElement.scrollTop=300')
        time.sleep(3)

        #
        # 拖到指定元素处
        driver.execute_script('arguments[0].scrollIntoView();', el_next)
        time.sleep(3)

    def test_send(self):
        driver = self.driver
        driver.get('http://music.taihe.com/')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/span').click()
        driver.find_element_by_id('ww').click()
        content = '秋酿'
        # 向文本框输入值
        js = 'document.getElementById("ww").value="%s"' % content
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="search_form"]/div[1]/span[2]').click()
        time.sleep(3)

    def test_removeAttribute(self):
        driver = self.driver
        driver.get('https://www.12306.cn/')
        time.sleep(5)
        # 去掉某个属性
        driver.execute_script('document.getElementById("train_date").removeAttribute("readonly")')
        js = 'document.getElementById("train_date").value="%s"' % '2018-12-30'
        driver.execute_script(js)
        driver.find_element_by_id('search_one').click()
        time.sleep(3)

    def test_modifyAttribute(self):
        driver = self.driver
        driver.get('https://www.12306.cn/')
        time.sleep(5)
        js = 'document.getElementById("g-service-lg-list").getElementsByTagName("li")[1].firstChild.target="_self";'
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="g-service-lg-list"]/li[1]/a').click()
        driver.find_element_by_id('search-input').send_keys('广州')
        time.sleep(3)

    def test_display(self):
        driver = self.driver
        driver.get('http://music.taihe.com/')
        time.sleep(3)
        # 处理自定义弹窗
        js = 'document.querySelector("img.tipToTaihe-content").style.display="none"'
        driver.execute_script(js)
        driver.find_element_by_tag_name('body').click()
        js = 'document.querySelector("#ww").value="秋酿"'
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="search_form"]/div[1]/span[2]').click()
        time.sleep(3)

    def test_el(self):
        driver = self.driver
        driver.get('http://music.taihe.com/')
        time.sleep(3)
        try:
            el = driver.find_element_by_id('qwa')
            self.assertEqual('error', el.text)
        except Exception:
            print('元素不存在')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

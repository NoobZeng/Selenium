#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/22  15:35
# @Author : Noob
# @File   : testselect.py

from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select

class SelectTest(unittest.TestCase):

    def login(self, user, password):
        print(self.driver.title)
        user_field = self.driver.find_element_by_xpath('//*[@id="loginname"]')

        # 清除文本框或者文本域的内容：element.clear()
        user_field.clear()

        # 模拟输入文本：element.send_keys(*value)
        user_field.send_keys(user)

        password_field = self.driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
        password_field.clear()
        password_field.send_keys(password)

        # 单击元素：element. click()
        self.driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()

    def setUp(self):
        self.driver = webdriver.Chrome('E:\\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://account.weibo.com/set/iframe?skin=skin048')

    def tearDown(self):
        self.driver.quit()

    def test_select(self):
        self.login('xxx', 'xxx')
        modify_button = self.driver.find_element_by_xpath('//*[@id="pl_content_account"]/div[1]/form/fieldset/div')
        modify_button.click()

        pro = self.driver.find_element_by_id('province')

        # 查看下拉选择是否展开
        pro.click()

        select_pro = Select(pro)

        # 验证下拉选项数量是否正确
        self.assertEqual(36, len(select_pro.options))

        # 验证下拉选项的当前选项
        self.assertTrue('天津' in select_pro.first_selected_option.text)

        # 期望下拉选项
        pros = ['安徽', '北京', '重庆', '福建', '甘肃', '广东', '广西', '贵州', '海南', '河北', '黑龙江', '河南',
                '湖北', '湖南', '内蒙古', '江苏', '江西', '吉林', '辽宁', '宁夏', '青海', '山西', '山东', '上海',
                '四川', '天津', '西藏', '新疆', '云南', '浙江', '陕西', '台湾', '香港', '澳门', '海外', '其他']

        # 实际下拉选项
        select_pro_options = []
        for option in select_pro.options:
            select_pro_options.append(option.text)

        # 验证下拉选项值是否与预期一致
        self.assertEqual(pros, select_pro_options)

        # 选择某个选项
        select_pro.select_by_visible_text('海南')

        # 获取关联的下拉选择框
        city = self.driver.find_element_by_id('city')

        select_city = Select(city)

        # 期望上，海南拥有的城市
        hainan_options = ['海口', '三亚', '其他']

        fujian_options = ['福州', '厦门', '莆田', '三明', '泉州', '漳州', '南平', '龙岩', '宁德']

        # 实际上，海南拥有的城市
        select_hainan_options = []

        select_fujian_options = []

        # 遍历选中省份对应城市的下拉选项
        for option in select_pro.options:
            select_pro.select_by_visible_text(option.text)
            if select_pro.first_selected_option.text == '海南':
                # 调用related()
                self.related(select_city.options, select_hainan_options, hainan_options)
            elif select_pro.first_selected_option.text == '福建':
                self.related(select_city.options, select_fujian_options, fujian_options)

    # 判断期望城市与实际城市是否一致的方法
    def related(self, select_cityoptions, selectjutioptions, jutioptions):
        for city_option in select_cityoptions:
            selectjutioptions.append(city_option.text)
        print(selectjutioptions)
        self.assertEqual(jutioptions, selectjutioptions)

if __name__ == '__main__':
    unittest.main(verbosity=2)
#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/19  23:29
# @Author : Noob
# @File   : webelement_modify_weibo.py

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from selenium import webdriver
import unittest

class ModifyWeibo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('E:\\program\Python37\Scripts\chromedriver-2.43.exe')
        cls.driver.get('https://weibo.com')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        print(cls.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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

    def test_modify(self):
        u'修改微博个人信息'
        self.login('xxx', 'xxx')
        self.driver.find_element_by_xpath('//*[@id="plc_top"]/div/div/div[3]/div[1]/ul/li[5]').click()
        self.driver.find_element_by_xpath('//*[@id="Pl_Core_UserInfo__6"]/div[2]/div[1]/div/a').click()

        # 切换到iframe中才能定位到其下的元素
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//div[@class='WB_cardwrap S_bg2']/iframe"))
        modify_button = self.driver.find_element_by_xpath('//*[@id="pl_content_account"]/div[1]/form/fieldset/div/a')

        # 检查元素对用户是否可见：element.is_displayed()
        # 检查元素是否可用：element.is_enabled()
        self.assertTrue(modify_button.is_displayed() and modify_button.is_enabled())

        # 检查是否进入编辑状态（通过按钮的text来判断）：由于未进入编辑状态所以这里用assertFalse断言
        # self.assertFalse('保存', modify_button.text)

        modify_button.click()

        # 再次检查是否进入编辑状态，点击该按钮后，进入编辑状态，这里用assertTrue断言
        self.assertTrue('保存', modify_button.text)

        # 获取所有必填选项和一个非必填选项的元素
        # 必填项
        nickname = self.driver.find_element_by_xpath('//*[@id="pl_content_account"]/div[1]/div[2]/div/div[2]/div[2]/input')
        province = self.driver.find_element_by_xpath('//*[@id="province"]')
        city = self.driver.find_element_by_xpath('//*[@id="city"]')
        sexs_boy = self.driver.find_element_by_xpath('//*[@id="man_radio"]')
        sexs_girl = self.driver.find_element_by_xpath('//*[@id="woman_radio"]')
        # 非必填项
        gay = self.driver.find_element_by_xpath('//*[@id="man"]')
        lesbian = self.driver.find_element_by_xpath('//*[@id="woman"]')

        # 判断昵称的文本框字符限制
        # 获取元素的属性值：element.get_attribute('name')
        self.assertEqual('text=请输入昵称', nickname.get_attribute('action-data'))

        # 判断文本框的宽度及高度一致

        self.assertEqual(
            self.driver.find_element_by_xpath(
                '//*[@id="pl_content_account"]/div[1]/div[2]/div/div[4]/div[3]/input').size['width'],
            nickname.size['width']
        )

        # 确保所有的字段对于用户都是可见和可用的
        self.assertTrue(nickname.is_displayed() and nickname.is_enabled()
                         and province.is_displayed() and province.is_enabled()
                         and city.is_displayed() and city.is_enabled()
                         and sexs_boy.is_displayed() and sexs_boy.is_enabled()
                         and sexs_girl.is_displayed() and sexs_girl.is_enabled()
                         and gay.is_displayed() and gay.is_enabled()
                         and lesbian.is_displayed() and lesbian.is_enabled() and '保存' == modify_button.text)

        # 初始状态为性别：女，性取向：双性恋
        # 修改性别和性取向,性别：男，性取向：男
        sexs_boy.click()
        lesbian.click()
        modify_button.click()

        # 由于定位不到几秒就消失的弹窗，最终校验修改性别和性取向检查信息是否修改成功

        # 多余步骤
        # self.driver.get('https://account.weibo.com/set/iframe?skin=skin048')

        # 该方法捕捉到的元素不可见，自动化速度较快，页面未加载完全的原因。（元素找不到有时候也是由于这个原因导致的）
        # boy_lable = self.driver.find_element_by_xpath('//*[@id="pl_content_account"]/div[1]/div[1]/div[5]/div[2]')
        # homosexuality_lable = self.driver.find_element_by_xpath('//*[@id="pl_content_account"]/div[1]/div[1]/div[6]/div[2]')

        # WebDriverWait 和 ExpectedCondition 组合使用；
        boy_xpath = '//*[@id="pl_content_account"]/div[1]/div[1]/div[5]/div[2]'
        boy_lable = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, boy_xpath)))
        homo_xpath = '//*[@id="pl_content_account"]/div[1]/div[1]/div[6]/div[2]'
        homosexuality_lable = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, homo_xpath)))
        self.assertEqual('男', boy_lable.text)
        self.assertEqual('同性恋', homosexuality_lable.text)

    def test_select(self):
        u'Select类的测试'
        self.driver.get('https://account.weibo.com/set/iframe?skin=skin048')
        modify_button = self.driver.find_element_by_xpath('//*[@id="pl_content_account"]/div[1]/form/fieldset/div')
        modify_button.click()

        # 期望省份
        pros = ['安徽', '北京', '重庆', '福建', '甘肃', '广东', '广西', '贵州', '海南', '河北', '黑龙江', '河南',
                '湖北', '湖南', '内蒙古', '江苏', '江西', '吉林', '辽宁', '宁夏', '青海', '山西', '山东', '上海',
                '四川', '天津', '西藏', '新疆', '云南', '浙江', '陕西', '台湾', '香港', '澳门', '海外', '其他']
        # 实际获取的省份
        # 将获取到的元素变成Select实例：Select(select标签元素)
        select_pros = Select(self.driver.find_element_by_id('province'))

        # 判断实际选项的个数是否和预期结果一致
        # 获取下拉菜单和列表的所有选项：selec_element.options
        self.assertEqual(len(pros), len(select_pros.options))

        # 实际省份的值放到list中
        select_pro_options = []
        for option in select_pros.options:
            select_pro_options.append(option.text)

        print(select_pro_options)

        # 排序
        # pros.sort()
        # select_pro_options.sort()

        # 判断每个选项的文本与预期的选项列表是否一致（这里做了排序）
        self.assertEqual(pros, select_pro_options)

        # 判断当前的实际选项是否与预期结果一致（初始值设置为广东）
        # 获取下拉菜单和列表的第一个选项/当前选项：select_element.first_selected_option
        self.assertEqual('广东', select_pros.first_selected_option.text)

        # 选择一个选项

        # 根据目标选项的文本值选中选项：select_element.select_by_visible_text('text')
        # select_pros.select_by_visible_text('天津')

        # 根据目标选项的索引选中选项：select_element.select_by_index(index)
        # 获取list中特定元素的方式：list.index(元素名)
        # 索引获取时应当在排序之前
        # print(select_pro_options.index('天津'))
        # select_pros.select_by_index(select_pro_options.index('天津'))

        # 根据目标选项的value属性值选中选项：select_element.select_by_value('value属性值')
        select_pros.select_by_value('12')

        # 判断当前选项值是否与选择后的预期结果一致
        self.assertEqual('天津', select_pros.first_selected_option.text)

        modify_button.click()

        pro_xpath = '//*[@id="pl_content_account"]/div[1]/div[1]/div[4]/div[2]'
        pro_lable = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, pro_xpath)))

        self.assertTrue('天津' in pro_lable.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
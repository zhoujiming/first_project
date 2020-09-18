# -*- coding: utf-8 -*-
# Date: 2020/9/19
import pytest
import allure


class Test_all():
    @allure.step(title="allure通过注解方式完成内容的展示，setp表示测试步骤1...")
    def test_setup(self):
        print("我就是打酱油的setup")

    @allure.step(title="run就是一个正常的方法.")
    def test_run(self):
        allure.attach("自定义描述1", "描述内容，自定义")
        print("我要运行")
        assert True

    def test_skip(self):
        print("我要跳过")

    @allure.severity(allure.severity_level.BLOCKER)  # 严重级别
    @allure.testcase("http://www.baidu.com/", "测试用例的地址")
    @allure.issue("http://music.migu.cn/v3/music/player/audio", "点击可跳转到bug地址")
    def test_error(self):
        with allure.attach("自定义描述1", "我需要让他进行错误"):
            print("我错误了")
            assert False

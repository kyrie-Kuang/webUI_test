# -*- coding: utf-8 -*-
import unittest
import time
import HTMLTestRunner


class RunCase:
    # 测试用例目录
    all_case_list = "E:\\kyl\\web_test\\test_case"

    # discover方法定义
    discover = unittest.defaultTestLoader.discover(
        all_case_list,
        pattern="mzmy_*.py",
        top_level_dir=None)

    # 获取时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S")

    # 定义报告存放路径
    filename = "E:\\kyl\\web_test\\report\\" + now + "result.html"

    fn = open(filename, "wb")

    # 执行测试套件
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fn,
        title=u"美自美业BOOS端测试报告",
        description=u"用例执行情况"
    )

    runner.run(discover)


if __name__ == '__main__':
    RunCase()

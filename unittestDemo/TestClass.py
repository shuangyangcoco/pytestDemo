import unittest
import os, time
from func import *
from parameterized import parameterized
from HTMLTestRunner import HTMLTestRunner


class TestClass(unittest.TestCase):

    @parameterized.expand([
        (1, 2, 'add', 3),
        (2, 1, 'min', 4),
        (7, 4, 'mul', 28),
        (8, 2, 'div', 4)
    ])
    def test_calcultor(self, a, b, opertor, excepted):
        self.assertEqual(calculate(a, b, opertor), excepted)

    @unittest.skip('除0的选择跳过')
    def test_calcu_zero(self):
        result = calculate(20, 0, 'div')
        self.assertEqual(result, '除数不能为0')

    @parameterized.expand([
        ('ad', 'upper', 'AD'),
        ('ac', 'upper', 'DF'),
        ('AB', 'lower', 'ab'),
        ('DF', 'lower', 'ee')
    ])
    def test_transfer_strings(self, strings, type, excepted):
        self.assertEqual(transfer_strings(strings, type), excepted)

    def test_random_string(self):
        self.assertEqual(random_string(), 'asdf')

if __name__ == '__main__':
    # 设置报告的路径
    report_path = os.path.join(os.path.dirname(__file__), 'report')
    # 通过当前时间命名报告
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = report_path + "/" + now + "_result.html"
    # 建立一个套件-就是可以装多个用例
    suite = unittest.TestSuite()
    # 在这个套件中添加测试用例（可能通过类名,模块名等加载，这次用类名）
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestClass))
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='测试用例')
        runner.run(suite)


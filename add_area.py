''' Test Cases '''

from robot.api import TestSuite
from robot.api import ResultWriter
from robot.model import Keyword


# 慧猿CRM登录新增区域测试
class CRM_add_areaTest:

    def __init__(self, name, librarys=["SeleniumLibrary"]):
        # 创建测试套件
        self.suite = TestSuite(name)
        # 导入SeleniumLibrary
        for lib in librarys:
            self.suite.resource.imports.library(lib)

    # 定义变量
    def create_variables(self):
        variables = {
            "${CRM}": "https://crm.kemai.com.cn",
            "${browser}": "Chrome",
            "${login1_input}": "name=user_name",
            "${login2_input}": "name=password",
            "${login_btn}": "class=loginBut",
            "${ziliao_element}": "xpath=//*[.='资料']",
            "${area_element}":"xpath=//*[.='区域信息']",
            "${area_add_btn}":"id=area_add",
            "${area_name_input}":"xpath=//div[@class='form-body']/div[2]/div/input",
            "${area_save_btn}":"xpath=//*[.='保存']",
            "${area_add_result}":"class=km-modal-dialog-msg"

        }
        for k, v in variables.items():
            self.suite.resource.variables.create(k, v)

    # 测试用例：启动浏览器
    def open_browsers(self):
        test_01 = self.suite.tests.create("启动浏览器")
        test_01.keywords.create("Open Browser",
            args=["${CRM}", "${browser}"])
        test_01.keywords.create("Title Should Be",
            args=["科脉慧猿CRM"])

    # 测试用例：慧猿CRM登录
    def login(self):
        test_02 = self.suite.tests.create("慧猿CRM登录测试")
        test_02.keywords.create("Input Text",
            args=["${login1_input}", "769316"])
        test_02.keywords.create("Input Text",
            args=["${login2_input}", "crm666"])
        test_02.keywords.create("Click Button",
            args=["${login_btn}"])
        test_02.keywords.create("Sleep", args=["3s"])

    # 测试用例：断言验证搜索结果标题
    def assert_title(self):
        test_03 = self.suite.tests.create("断言验证登录结果标题")
        test_03.keywords.create("Title Should Be",
            args=["科脉慧猿CRM-首页"])

    # 测试用例：新增区域
    def add_area(self):
        test_04 = self.suite.tests.create("新增区域")
        test_04.keywords.create("Sleep", args=["5s"])
        test_04.keywords.create("Click element",
            args=["${ziliao_element}"])
        test_04.keywords.create("Sleep", args=["3s"])
        test_04.keywords.create("Click element",
            args=["${area_element}"])
        test_04.keywords.create("Sleep", args=["3s"])
        test_04.keywords.create("Click Button",
            args=["${area_add_btn}"])
        test_04.keywords.create("Sleep", args=["3s"])
        test_04.keywords.create("Input Text",
            args=["${area_name_input}", "测试robot"])
        test_04.keywords.create("Click Button",
            args=["${area_save_btn}"])
        test_04.keywords.create("Sleep", args=["3s"])

    # 测试用例：断言验证新增区域结果
    def assert_result(self):
        test_05 = self.suite.tests.create("断言验证新增区域结果")
        test_05.keywords.create("Page Should Contain Button",
            args=["确定"])

    # 测试用例：关闭测试用例
    def close_browsers(self):
        test_06 = self.suite.tests.create("关闭浏览器")
        test_06.keywords.create("Close All Browsers")

    # 运行
    def run(self):
        self.create_variables()
        self.open_browsers()
        self.login()
        self.assert_title()
        self.add_area()
        self.assert_result()
        self.close_browsers()

        # 运行套件
        result = self.suite.run(critical="登录测试",
            output="output.xml")

        # 生成日志、报告文件
        ResultWriter(result).write_results(
           report="report.html", log="log.html")

if __name__ == "__main__":
    print("用Python写Robot Framework测试")
    suite = CRM_add_areaTest("慧猿CRM登录新增区域测试")
    suite.run()
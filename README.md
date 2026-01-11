# API自动化测试框架

## 如何生成并查看Allure报告
1. 运行测试并收集结果：`pytest --alluredir=outputs/reports/allure_raw`
2. 生成在线报告（临时查看）: `allure serve outputs/reports/allure_raw`
3. 生成静态HTML报告（永久保存）: `allure generate outputs/reports/allure_raw -o outputs/reports/allure_html --clean`
生成的报告位于 `outputs/reports/allure_html` 目录，用浏览器打开 `index.html` 即可查看。
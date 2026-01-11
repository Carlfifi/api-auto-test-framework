# 🧪 Python 接口自动化测试框架

[![Python Test CI](https://github.com/Carlfifi/api-auto-test-framework/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Carlfifi/api-auto-test-framework/actions/workflows/python-ci.yml)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

一个基于 **Pytest** 和 **Requests** 构建的、企业级的接口自动化测试框架。具备数据驱动、优雅报告和持续集成能力。

## ✨ 核心特性
- **✅ 结构清晰**：采用 `Page Object` 思想封装请求层，分离测试代码与资源。
- **📊 数据驱动**：支持通过 `@pytest.mark.parametrize` 和 `YAML` 文件管理测试数据。
- **🎨 专业报告**：集成 **Allure** 框架，生成详尽且可视化的交互式测试报告。
- **🔄 持续集成**：通过 **GitHub Actions** 实现 CI/CD，代码推送即触发自动化测试。
- **🔧 易于扩展**：模块化设计，轻松适配更多接口类型与测试需求。

## 🗂️ 项目结构
```
api-auto-test-framework/
├── common/               # 公共组件层
│   └── request_handler.py  # 封装的通用HTTP请求客户端
├── config/              # 配置层
│   └── setting.py       # 全局配置（如基础URL）
├── test_cases/          # 测试用例层
│   └── test_demo_api.py # 使用Pytest编写的测试用例
├── test_data/           # 测试数据层
│   └── api_data.yaml    # YAML格式的测试数据
├── outputs/             # 输出目录（报告、日志）
├── .github/workflows/   # GitHub Actions CI/CD 配置
├── requirements.txt     # 项目依赖清单
├── pytest.ini          # Pytest 配置文件
└── README.md           # 项目说明文档
```

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/Carlfifi/api-auto-test-framework.git
cd api-auto-test-framework
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行测试并生成报告
```bash
# 运行所有测试并收集Allure数据
pytest --alluredir=outputs/reports/allure_raw

# 生成并在线预览Allure报告（自动打开浏览器）
allure serve outputs/reports/allure_raw
```

## 📈 CI/CD 状态
本项目已配置 GitHub Actions。每次向 `master` 分支推送代码或提交 Pull Request 时，都会自动运行完整的测试套件。
点击顶部的徽章或访问 [Actions](https://github.com/Carlfifi/api-auto-test-framework/actions) 页面查看最新构建状态。

## 📄 开源协议
本项目基于 [MIT](LICENSE) 协议开源。
# ⚡ Smart Test Automation using AI & DevOps

Real working test automation project — Playwright + PyTest + AI Self-Healing + CI/CD

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt
playwright install chromium

# 2. Run all tests
pytest tests/ -v --html=reports/report.html

# 3. Open report
open reports/report.html
```

## 📁 Project Structure

```
smart_test_project/
├── ai_engine/
│   └── healer.py          # AI Self-Healing locator engine
├── pages/
│   ├── login_page.py      # Login Page Object Model
│   └── products_page.py   # Products Page Object Model
├── tests/
│   ├── test_login.py      # UI Login tests (7 tests)
│   ├── test_products.py   # E-Commerce product tests (9 tests)
│   ├── test_api.py        # REST API tests (12 tests)
│   └── test_ai_healing.py # AI Self-Healing demo (4 tests)
├── config/
│   └── config.py          # URLs, credentials, settings
├── reports/               # HTML test reports (auto-generated)
├── .github/workflows/     # GitHub Actions CI/CD
├── .vscode/               # VS Code settings + launch configs
├── conftest.py            # PyTest fixtures
├── pytest.ini             # PyTest configuration
└── requirements.txt       # Python dependencies
```

## 🧪 Test Targets

| Target | URL |
|--------|-----|
| UI (Login + Cart) | https://www.saucedemo.com |
| REST API | https://dummyjson.com |

## 🤖 AI Self-Healing

When a locator breaks, the AI engine:
1. Detects the broken selector
2. Scans DOM candidates
3. Scores similarity (text + structure)
4. Returns best match with confidence %
5. Logs the healing event

## ▶ VS Code

- Open project folder in VS Code
- Press `Ctrl+Shift+D` → pick a run config → press ▶
- Or use Testing sidebar (flask icon) to run individual tests

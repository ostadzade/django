import os
from pathlib import Path

# مسیرهای پروژه
BASE_DIR = Path(__file__).resolve().parent
APPS_DIR = BASE_DIR / "apps" / "myaccounting"
TEMPLATES_DIR = BASE_DIR / "templates" / "accounting"
STATIC_DIR = BASE_DIR / "static" / "myaccounting"

# ساختار دایرکتوری‌ها
dir_structure = {
    APPS_DIR: [
        "__init__.py",
        "admin.py",
        "apps.py",
        "urls.py",
        "models/__init__.py",
        "models/base.py",
        "models/accounting.py",
        "models/company.py",
        "models/partner.py",
        "services/__init__.py",
        "services/accounting.py",
        "services/reporting.py",
        "templatetags/__init__.py",
        "templatetags/accounting_tags.py",
        "utils/__init__.py",
        "utils/currency.py",
        "utils/date_utils.py",
        "views/__init__.py",
        "views/accounting.py",
        "views/api.py",
        "static/css/accounting.css",
        "static/css/dashboard.css",
        "static/js/accounting.js",
        "static/js/chart.js"
    ],
    TEMPLATES_DIR: [
        "base.html",
        "dashboard.html",
        "accounts/list.html",
        "accounts/form.html",
        "accounts/tree.html",
        "journals/list.html",
        "journals/form.html",
        "moves/list.html",
        "moves/form.html",
        "moves/detail.html",
        "reports/trial_balance.html",
        "reports/profit_loss.html",
        "reports/balance_sheet.html"
    ],
    TEMPLATES_DIR.parent / "partials": [
        "_accounting_sidebar.html",
        "_accounting_navbar.html",
        "_move_lines_table.html"
    ]
}

# محتوای فایل‌ها
file_contents = {
    # محتوای تمام فایل‌هایی که قبلا ارائه شد را اینجا قرار دهید
    # مثال:
    APPS_DIR / "__init__.py": "",
    APPS_DIR / "admin.py": """
from django.contrib import admin
from .models import Account, Journal, AccountMove, AccountMoveLine, Partner, Company, Currency

# محتوای کامل فایل admin.py که قبلا ارائه شد را اینجا قرار دهید
""",
    # به همین ترتیب برای تمام فایل‌ها
}

# ایجاد ساختار
for base_dir, files in dir_structure.items():
    for file in files:
        path = base_dir / file
        os.makedirs(path.parent, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            if path in file_contents:
                f.write(file_contents[path])
            else:
                f.write("")

print("ساختار پروژه با موفقیت ایجاد شد!")
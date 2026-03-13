# Demo Web Shop E2E Automation Framework

Production-style Selenium automation framework using **Python, PyTest, and Page Object Model**.

This project demonstrates a **scalable test automation architecture** for end-to-end testing of the Demo Web Shop application.

---

# 🚀 Tech Stack

* **Python**
* **Selenium WebDriver**
* **PyTest**
* **Allure Reporting**
* **Page Object Model (POM)**
* **WebDriver Manager**
* **Logging Framework**

---

# 🧱 Framework Architecture

The framework follows a layered design for maintainability and scalability.

```
Tests
   ↓
Page Objects
   ↓
Core Framework (Driver, Waits, Utilities)
   ↓
Configuration + Test Data
```

Key design principles:

* Page Object Model (POM)
* Separation of concerns
* Reusable utilities
* Config-driven execution
* Rich reporting

---

# 📁 Project Structure

```
demowebshop-e2e-selenium-pytest
│
├── config
│   ├── config.yaml
│   └── config_reader.py
│
├── core
│   ├── driver_factory.py
│   └── exceptions.py
│
├── data
│   ├── users.json
│   └── products.json
│
├── pages
│   ├── base_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── home_page.py
│   ├── search_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── order_page.py
│
├── tests
│   ├── test_login.py
│   ├── test_register.py
│   └── test_purchase_flow.py
│
├── utils
│   ├── logger.py
│   ├── screenshot.py
│   ├── wait_utils.py
│   └── data_loader.py
│
├── reports
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# ⚙️ Features

* Page Object Model implementation
* Config-driven environment setup
* Centralized driver factory
* Logging system
* Screenshot capture on test failure
* Allure test reporting
* Reusable test utilities
* Clean modular architecture

---

# 🧪 Automated Test Scenarios

### Login Test

* Navigate to login page
* Enter valid credentials
* Verify successful login

### User Registration

* Register new user with random email
* Verify registration success message

### Purchase Flow (E2E)

* Login
* Search product
* Open product page
* Add to cart
* Proceed to checkout
* Verify checkout page

---

# 🛠 Installation

Clone the repository:

```
git clone https://github.com/CypherMorgan/demowebshop-e2e-selenium-pytest.git
```

Navigate into the project:

```
cd demowebshop-e2e-selenium-pytest
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# ▶️ Run Tests

Execute all tests:

```
pytest
```

Run tests with Allure reporting:

```
pytest --alluredir=reports/allure-results
```

---

# 📊 View Allure Report

Generate and open the report:

```
allure serve reports/allure-results
```

The report will include:

* test execution results
* step breakdown
* screenshots on failure
* execution timeline

---

# 📝 Logging

Execution logs are saved in:

```
reports/logs/test.log
```

Logs include:

* test start/end
* navigation actions
* login attempts
* validation steps

---

# 📷 Screenshots

Screenshots are automatically captured on test failures.

Location:

```
reports/screenshots/
```

They are also attached to the Allure report.

---

# 🧩 Configuration

Environment settings are defined in:

```
config/config.yaml
```

Example:

```yaml
environment: qa

browser:
  name: chrome
  headless: false

environments:
  qa:
    base_url: https://demowebshop.tricentis.com
    username: testuser@test.com
    password: Password123
```

---

# 📌 Future Improvements

* Parallel execution using `pytest-xdist`
* CI/CD integration (GitHub Actions)
* Dockerized Selenium execution
* Selenium Grid support
* API + UI test integration

---

# 👨‍💻 Author

Automation framework built as a **portfolio project demonstrating QA automation architecture and best practices**.

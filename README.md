\# Automated UI Test Suite for DemoBlaze E-Commerce Site



This project contains a functional UI test suite for the public demo site \[https://www.demoblaze.com](https://www.demoblaze.com) using Selenium and Pytest. It showcases core automation capabilities for Software QA portfolios.



\## 🔧 Tech Stack

\- Python 3.9

\- Selenium WebDriver

\- Pytest

\- ChromeDriver



\## 🚀 Features

\- Automated functional tests (login, category navigation, modal display)

\- Tests designed to intentionally fail (for screenshot capture)

\- Screenshot-on-failure implementation

\- Pytest fixtures for clean setup/teardown



\## 🧪 Test Cases Included

| Test Name               | Purpose                                    |

|------------------------|--------------------------------------------|

| `test\_homepage\_title`  | Verifies the homepage loads with correct title |

| `test\_category\_laptops`| Navigates to the "Laptops" category         |

| `test\_signup\_modal`    | Confirms the Sign-Up modal displays         |

| `test\_unreal\_button`   | \*Fail test\* – Tries clicking non-existent button |

| `test\_wrong\_hp\_title`  | \*Fail test\* – Asserts incorrect title       |



\## 📷 Screenshot Logging

If a test fails, a screenshot is automatically saved to `/screenshots/` with the test name and timestamp.



\## 📁 Project Structure

demoblaze\_automation/

├── tests/

│ ├── test\_login.py

│ ├── test\_homepage.py

│ └── ...

├── conftest.py

├── screenshots/

├── requirements.txt

└── README.md





\## ▶️ Running Tests

Install dependencies:

```bash

pip install -r requirements.txt



Run all tests:

pytest tests/




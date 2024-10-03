# Scrapy Browser Automation - Part 1

This project demonstrates how to set up a Scrapy-based browser automation environment using a Python virtual environment.

## Setting Up the Project

```bash
# 1. go to the Root Directory documens_source_code

cd documens_source_code
 

# 2. Create a Python Virtual Environment
# Inside the root directory, create a Python virtual environment to manage dependencies:
python3 -m venv venv

# 3. Activate the Virtual Environment
# Activate the virtual environment before installing the necessary packages:
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 4. Install Required Dependencies
# After activating the virtual environment, install the required dependencies from the requirements.txt file:
pip install -r requirements.txt

# 5. Project Structure
# Here's how your directory structure should look:

documents_source_code\
├── requirements.txt
├── venv\  # Virtual environment folder
├── Scrapy_Browser_Automation\
│   ├── scrapy_automation\
│   │   ├── scrapy_automation\
│   │   │   ├── __init__.py
│   │   │   ├── items.py
│   │   │   ├── middlewares.py
│   │   │   ├── pipelines.py
│   │   │   ├── settings.py
│   │   │   └── spiders\
│   │   │       ├── __init__.py
│   │   │       └── basic_scripting_playwright.py 
│   │   │       └──basic_scripting_selenium.py
│   └── scrapy.cfg
│
├── Advanced_Scrapy_Features\
│   ├── advance_scrapy\
│   │   ├── advance_scrapy\
│   │   │   ├── __init__.py
│   │   │   ├── items.py
│   │   │   ├── middlewares.py
│   │   │   ├── pipelines.py
│   │   │   ├── settings.py
│   │   │   └── spiders\
│   │   │       ├── __init__.py
│   │   │       ├── example_spider1.py
│   │   │       └── example_spider2.py
│   └── scrapy.cfg
│
└── Real_World_Scrapy_Applications\
    ├── scrapy_applications\
    │   ├── scrapy_applications\
    │   │   ├── __init__.py
    │   │   ├── items.py
    │   │   ├── middlewares.py
    │   │   ├── pipelines.py
    │   │   ├── settings.py
    │   │   └── spiders\
    │   │       ├── __init__.py
    │   │       └── example_spider1.py
    │   │       └── example_spider2.py
    └── scrapy.cfg


 
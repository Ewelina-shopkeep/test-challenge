# Project Setup


`git clone
`
`cd to project directory
`
Install virtualenv:
`py -m pip install --user virtualenv
`
Create a virtual environment:
`py -m venv env
`
Activate your virtual environment:
`.\env\Scripts\activate
`
Install allure:
`pip install allure
`
# Running Tests

`python -m pytest --alluredir=<allure-results> --browser <firefox/chrome/edge> --headless <true/false>
`
When no browser was selected then chrome will be used.

# Viewing test results in allure report locally:

`allure serve <allure-results>`
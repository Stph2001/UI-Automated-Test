# Task - UI Automated test using Selenium WebDriver

What do you need to do?
Create automated tests using the following test case:
  
Sign in 
Preconditions
* Generated customer with all customer data
Test steps
* Open [Home page](https://demo.evershop.io/ [demo.evershop.io])
* Click *Sign in* button
* Fill *Email address* and *Password* to create an account
* Click *Create an account*
* Log in
* Select 3 differents products and add it to the cart with different quantities
* Go to Checkout page and click on Checkout
* Fill the shipping address and submit
* Click on success to get correct card information
* Fill payment information
* Click Place Order

Assertions
* Verify Order created successful with the correct information Contact, Payment, Shipping Address, Billing Address and Items

## Libraries and Tools used in this project

This project relies on the following Python libraries and tools:

### WebDriver Chrome
I used this test automation tool to allow me to control and manipulate an instance of Chrome from Python code.

### Selenium
Selenium was used to automate a test case in the respective web browser. It allowed the simulation of various actions, such as clicking buttons, filling out forms, navigating between sections, and extracting data from the page.

### Faker
Faker was used to generate fake data for a user from the United States. It provided data to register, such as name, email, and password, as well as data to fill in the shipping address.

### Time
The time library was used to pause the code execution for a few seconds. This ensured that the page loaded properly and allowed the actions to continue without errors.

### Random
Random was primarily used to generate random values throughout the project.

Please make sure to have these libraries and tools installed before running the code. For the libraries you can do so by running `pip install <library-name>` in your terminal/command prompt. For the driver you can download from https://chromedriver.chromium.org/ and you have to add the exe's path to your PATH.

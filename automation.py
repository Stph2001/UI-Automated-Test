from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
import time

# Create a new instance of the browser driver
driver = webdriver.Chrome()
driver.maximize_window()

# Create a explicit wait 
wait = WebDriverWait(driver, 10)

# Open the home page
driver.get("https://demo.evershop.io/")

# Click the Sign in button
sign_in_button = driver.find_element(by=By.XPATH, value="//a[@href='/account/login']")
sign_in_button.click()

# Click the register button
create_account_button = driver.find_element(by=By.XPATH, value="//a[text()='Create an account']")
create_account_button.click()

# Create dummy data for a US user
faker = Faker('en_US')
name = faker.name()
email = faker.email()
password = faker.password(length=8)

# Create an account with the previous data 
name_input = driver.find_element(by=By.NAME, value="full_name")
name_input.send_keys(name)

email_input = driver.find_element(by=By.NAME, value="email")
email_input.send_keys(email)

password_input = driver.find_element(by=By.NAME, value="password")
password_input.send_keys(password)

# Click the Sign up button
sign_up_button = driver.find_element(by=By.XPATH, value="//span[text()='SIGN UP']")
sign_up_button.click()

# Save section buttons
section = ['Men', 'Kids', 'Women']

# Choose 3 products to add to cart
for i in range(3):
    # Choose one of the 3 shoe sections
    section_button = driver.find_element(by=By.XPATH, value="//a[text()='" + section[i] + "']")
    section_button.click()

    # Randomly choose a product from the section
    product_list = driver.find_elements(by=By.CLASS_NAME, value="listing-tem")
    product = random.choice(product_list)
    product.click()

    # Choose as many as you want at random
    quantity_input = driver.find_element(by=By.NAME, value="qty")
    quantity_input.clear()
    quantity_input.send_keys(random.randint(1, 3))

    # Save the two variant lists to choose one option per list
    variant_list = driver.find_elements(by=By.CLASS_NAME, value="variant-option-list")
    size_list = variant_list[0].find_elements(by=By.CLASS_NAME, value="mr-05")
    color_list = variant_list[1].find_elements(by=By.CLASS_NAME, value="mr-05")

    # Choose a random size
    size = random.choice(size_list)
    size.click()

    # Choose a random color
    color = random.choice(color_list)
    color.click()

    # Wait 1 second
    time.sleep(1)

    # Click the Add to Cart button
    add_to_cart_button = driver.find_element(by=By.XPATH, value="//span[text()='ADD TO CART']")
    add_to_cart_button.click()

# Click the Mini Cart button
mini_cart_button = driver.find_element(by=By.CLASS_NAME, value="mini-cart-wrapper")
mini_cart_button.click()

# Click the Checkout button
checkout_button = driver.find_element(by=By.XPATH, value="//span[text()='CHECKOUT']")
checkout_button.click()

# Create dummy shipping address data for a US user
phone_number = faker.phone_number()
address = faker.street_address()
city = faker.city()
zip_code = faker.zipcode()
state = faker.state()

# Fill the shipping address form
name_input = wait.until(EC.element_to_be_clickable((By.NAME, "address[full_name]")))
name_input.send_keys(name)

phone_number_input = driver.find_element(by=By.NAME, value="address[telephone]")
phone_number_input.send_keys(phone_number)

address_input = driver.find_element(by=By.NAME, value="address[address_1]")
address_input.send_keys(address)

city_input = driver.find_element(by=By.NAME, value="address[city]")
city_input.send_keys(city)

country_combo_box = driver.find_element(by=By.NAME, value="address[country]")
country_combo_box = Select(country_combo_box)
country_combo_box.select_by_visible_text("United States")

province_combo_box = driver.find_element(by=By.NAME, value="address[province]")
province_combo_box = Select(province_combo_box)
province_combo_box.select_by_visible_text(state)

zip_code_input = driver.find_element(by=By.NAME, value="address[postcode]")
zip_code_input.send_keys(zip_code)

# Click a random shipping method
shipping_method_list = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "radio-unchecked")))
shipping_method = random.choice(shipping_method_list)
shipping_method.click()

# Click the Payment button
payment_button = driver.find_element(by=By.XPATH, value="//span[text()='Continue to payment']")
payment_button.click()

# Wait 2 seconds
time.sleep(2)

# Choose the payment method with Visa
payment_method_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[local-name()='svg' and @xmlns='http://www.w3.org/2000/svg']")))
payment_method_list[4].click()

# Get valid card details
card_info_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='text-sm text-gray-600']")))

for card_info in card_info_list:
    if 'Test card number' in card_info.text:
        card_number = ''.join(filter(str.isdigit, card_info.text))
    elif 'Test card expiry' in card_info.text:
        card_expiry = card_info.text.split(': ')[1]
    elif 'Test card CVC' in card_info.text:
        card_cvc = card_info.text.split(': ')[1]

# Switch to the frame of the card form to be able to complete it
card_iframe = driver.find_elements(by=By.TAG_NAME, value="iframe")[0]
driver.switch_to.frame(card_iframe)

# Fill the card form
card_number_input = driver.find_element(by=By.NAME, value="cardnumber")
card_number_input.send_keys(card_number)

card_expiry_input = driver.find_element(by=By.NAME, value="exp-date")
card_expiry_input.send_keys(card_expiry)

card_cvc_input = driver.find_element(by=By.NAME, value="cvc")
card_cvc_input.send_keys(card_cvc)

# Go back to the default content
driver.switch_to.default_content()

# Click the Place Order button
place_order_button = driver.find_element(by=By.XPATH, value="//span[text()='Place Order']")
place_order_button.click()

# Compare detail of the order with the expected data

# Get Contact Data
contact_info = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Contact information']")))
email_info = contact_info.find_element(by=By.XPATH, value="following-sibling::div[@class='text-textSubdued']").text

# Get Payment Method Data
payment_info = driver.find_element(by=By.XPATH, value="//div[text()='Payment Method']")
payment_method_info = payment_info.find_element(by=By.XPATH, value="following-sibling::div[@class='text-textSubdued']").text

# Create a function for address data
def get_address_info(element):
    name = element.find_element(by=By.CLASS_NAME, value="full-name").text
    address = element.find_element(by=By.CLASS_NAME, value="address-one").text
    phone_number = element.find_element(by=By.CLASS_NAME, value="telephone").text

    address_more_info = element.find_element(by=By.CLASS_NAME, value="city-province-postcode")
    zip_code = address_more_info.find_element(by=By.XPATH, value="./div[1]").text.split(', ')[0]
    city = address_more_info.find_element(by=By.XPATH, value="./div[1]").text.split(', ')[1]
    state = address_more_info.find_element(by=By.XPATH, value="./div[2]").text.split(', ')[0]
    country = address_more_info.find_element(by=By.XPATH, value="./div[2]").text.split(', ')[1]

    return name, address, phone_number, zip_code, city, state, country

# Get Shipping Address Data
shipping_info = driver.find_element(by=By.XPATH, value="//div[text()='Shipping Address']/following-sibling::div[@class='text-textSubdued']")
name_info, address_info, phone_number_info, zip_code_info, city_info, state_info, country_info = get_address_info(shipping_info)

# Get Billing Address Data
billing_info = driver.find_element(by=By.XPATH, value="//div[text()='Billing Address']/following-sibling::div[@class='text-textSubdued']")
name_info2, address_info2, phone_number_info2, zip_code_info2, city_info2, state_info2, country_info2 = get_address_info(billing_info)

# Get the number of unique products
summary_info = driver.find_element(by=By.CLASS_NAME, value="summary-row")
n_product_info = summary_info.find_element(by=By.XPATH, value="./div/div[1]").text.split(" ")[0]

# Verify the data
assert email_info == email, "The email is incorrect"
assert payment_method_info == "Credit Card", "The payment method is incorrect"

assert name_info == name, "The name is incorrect"
assert address_info == address, "The address is incorrect"
assert phone_number_info == phone_number, "The phone number is incorrect"
assert zip_code_info == zip_code, "The zip code is incorrect"
assert city_info == city, "The city is incorrect"
assert state_info == state, "The state is incorrect"
assert country_info == 'United States', "The country is incorrect"

assert name_info2 == name, "The name is incorrect"
assert address_info2 == address, "The address is incorrect"
assert phone_number_info2 == phone_number, "The phone number is incorrect"
assert zip_code_info2 == zip_code, "The zip code is incorrect"
assert city_info2 == city, "The city is incorrect"
assert state_info2 == state, "The state is incorrect"
assert country_info2 == 'United States', "The country is incorrect"

assert int(n_product_info) == 3, "The number of unique products is incorrect"

print("The purchase details are correct")

# Close the page
time.sleep(100)
driver.quit()
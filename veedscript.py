import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = uc.Chrome()

try:
    # Open InVideo AI login page
    driver.get("https://ai.invideo.io/login")

    # Wait until the Google OAuth button is visible
    wait = WebDriverWait(driver, 5)
    google_login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'c-PJLV c-kXcFJy c-kXcFJy-gsmDXe-state-0 c-PJLV-ifvayZa-css')]"))
    )
    google_login_button.click()

    # Switch to the Google login window
    main_window = driver.current_window_handle
    wait.until(EC.number_of_windows_to_be(2))
    for window in driver.window_handles:
        if window != main_window:
            driver.switch_to.window(window)
            break

   # Wait for Google login page to load and enter email
    email_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_input.send_keys("agentcracker222")  # Replace with your email

    # Click Next
    driver.find_element(By.ID, "identifierNext").click()

    # Wait for the overlay or any other blocking element to disappear
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'kPY6ve')))

    # Now wait for password input field to load
    password_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='whsOnd zHQkBf']"))
    )

    # Click the password input field and enter the password
    password_input.click()
    password_input.send_keys("Ravi@0570")
    # Click Next
    # driver.find_element(By.ID, "passowrdNext").click()
    driver.find_element(By.ID, "passwordNext").click()
    # Click Continue LgbsSe
    continue_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe P62QJc LQeN7 BqKGqe pIzcPc TrZEUc lw1w4b']"))
    )
    continue_button.click()

    # Switch back to the main window
    wait.until(EC.number_of_windows_to_be(1))
    driver.switch_to.window(main_window)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    time.sleep(10)
    driver.quit()


class Page():
    def __init__(self, driver):
        self.driver = driver

        self.login_page_enter_button_xpath = "//span[contains(text(),'Login')]"

        self.login_btn_textbox_class_name = "username"

        self.password_textbox_name = "password"

        self.login_btn_class_name = "submitButton_uHU80"

        self.invalid_message_xpath = "//li[contains(text(),'Wrong email and')]"

        self.title_id = "challenge-list-title"



    def enter_in_login_page(self):
        self.driver.find_element_by_xpath(self.login_page_enter_button_xpath).click()

    def enter_username(self, username):
        self.driver.find_element_by_name(self.login_btn_textbox_class_name).clear()
        self.driver.find_element_by_name(self.login_btn_textbox_class_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_to_login(self):
        self.driver.find_element_by_class_name(self.login_btn_class_name).click()

    def get_title_id(self):
        msg = self.driver.find_element_by_id(self.title_id).text
        return msg



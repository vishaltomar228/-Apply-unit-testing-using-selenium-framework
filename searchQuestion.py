class SearchQuestion():

    def __int__(self):

        self.login_page_enter_button_xpath = "//span[contains(text(),'Login')]"

        self.login_btn_textbox_class_name = "username"

        self.password_textbox_name = "password"

        self.login_btn_class_name = "submitButton_uHU80"

        self.search_id = "searchbar-input"

        self.question_xpath = "//b[contains(text(),'KMP')]"

        self.question_name_id = "problem-title"

    def get_driver(self, driver):
        self.driver = driver

    def enter_in_search_textbox(self, questionname):
        self.driver.find_element_by_id("searchbar-input").send_keys(questionname)


    def click_question(self):
        self.driver.find_element_by_xpath("//b[contains(text(),'KMP')]").click()

    def get_question_name(self):
        msg = self.driver.find_element_by_id("problem-title" ).text
        return msg

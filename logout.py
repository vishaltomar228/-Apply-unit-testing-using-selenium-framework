class Logout():

    def __init__(self, driver):
        self.driver = driver

        self.drop_down_xpath = "//i[@class='fa fa-caret-down']"

        self.logout_xpath = "//a[@class='track-header-profile-box-logout']//li[contains(text(),'Logout')]"

    def get_drop_down(self):
        self.driver.find_element_by_xpath(self.drop_down_xpath).click()

    def logout_btn(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()


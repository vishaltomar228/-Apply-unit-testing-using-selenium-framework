class ActivityTrack():
    def __init__(self, driver):
        self.driver = driver

        self.dropdown_xpath = "//i[@class='fa fa-caret-down']"

        self.activity_button_xpath = "//li[contains(text(),'Activity')]"

        self.total_solved_xpath = "//div[@id='f2f94ad']//tbody//td[1]"
        self.total_accepted_xpath = "//div[@id='f2f94ad']//tbody//td[3]"
        self.total_submission_xpath = "//td[@class='short-col bold'][contains(text(),'3')]"

        self.actvity_css_selector = "div.bl-page:nth-child(14) div.left div:nth-child(2) div.profile-overview.medium-margin table.nice-table-2.align-center tbody:nth-child(2) > tr.dark.regular.weight-600"
        self.question_xpath = "/html[1]/body[1]/div[10]/div[1]/div[9]/div[1]/table[1]/tbody[1]"

    def click_dropdown(self):
        self.driver.find_element_by_xpath(self.dropdown_xpath).click()

    def click_activity_button(self):
        self.driver.find_element_by_xpath(self.activity_button_xpath).click()

    def get_activty(self):
        row = self.driver.find_element_by_css_selector(self.actvity_css_selector)
        activity = row.text.split()

        abc = self.driver.find_element_by_xpath(self.question_xpath)
        question = abc.text

        return activity, question


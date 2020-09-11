from selenium import webdriver
import unittest
import time
from page import Page
from activityTrack import ActivityTrack
from pyunitreport import HTMLTestRunner
from searchQuestion import SearchQuestion
from logout import Logout

class AutomationTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('chromedriver.exe')
        cls.driver.get("https://www.hackerearth.com/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login(self):
        driver = self.driver
        p = Page(driver)
        p.enter_in_login_page()
        p.enter_username("Your email-id")
        p.enter_password("Your Password")
        p.click_to_login()

        title = p.get_title_id()
        print("############## first page title ##############")
        print(title)

        self.assertEqual(title, "Hackathons, Programming Challenges, And Coding Competitions")
        time.sleep(10)

    def test_02_activity(self):
        activitytracker = ActivityTrack(self.driver)
        activitytracker.click_dropdown()
        activitytracker.click_activity_button()

        activity, question = activitytracker.get_activty()

        self.total_solved = activity[0]
        self.total_submission = activity[1]
        self.total_accepted = activity[2]

        print("################### PROGRESS ###############")
        print("TOTAL SOLVED QUESTION = ", self.total_solved)
        print("TOTAL SUBMISSION = ", self.total_submission)
        print("TOTAL ACCEPTED = ", self.total_accepted)

        print("################# QUESTION ###############")
        print(question)

        self.assertEqual(self.total_solved, self.total_accepted)
        self.assertTrue(int(self.total_accepted) <= int(self.total_submission))

    
    def test_03_search_question(self):
        driver = self.driver
        searchquestion = SearchQuestion()
        searchquestion.get_driver(driver)

        questionname = "Apply KMP"
        searchquestion.enter_in_search_textbox(questionname)
        time.sleep(60)

        searchquestion.click_question()

        searched_question = searchquestion.get_question_name()

        print("######## SEARCHED QUESTION NAME ##########")

        print(searched_question)

        self.assertEqual(searched_question, questionname)

    def test_04_logout(self):
        driver = self.driver
        lg = Logout(driver)
        lg.get_drop_down()
        lg.logout_btn()
        time.sleep(10)
        self.driver.close()
        self.driver.quit()



    @classmethod
    def tearDownClass(cls) -> None:
        print("COMPLETED")

if __name__ == '__main__':
    unittest.main()

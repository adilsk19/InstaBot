from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep


class Instabot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path=r'C:/Python/Python36/chromedriver.exe')
        self.driver.get("https://www.instagram.com/accounts/login/?hl=en")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name='username']") \
            .send_keys(username)

        self.driver.find_element_by_xpath("//input[@name='password']") \
            .send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div') \
            .click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]') \
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a') \
            .click()


myBot = Instabot('technically_paranoid', 'technicalbaba')

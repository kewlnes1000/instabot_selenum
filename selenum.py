from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


class SeleniumSpider():
    def __init__(self):
        load_dotenv(find_dotenv())

        # 读取 config
        self.runtime = 0

        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36')
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-gpu')
        options.add_argument('lang=zh-tw.UTF-8')
        options.add_argument(
            'accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
        options.add_argument('accept-encoding=gzip, deflate, br')
        options.add_argument(
            'accept-language=zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7')
        options.add_argument('referer=https://www.instagram.com/')
        options.add_argument('sec-fetch-dest=document')
        options.add_argument('sec-fetch-mode=navigate')
        options.add_argument('sec-fetch-site=same-origin')
        options.add_argument('sec-fetch-user=?1')
        options.add_argument('upgrade-insecure-requests=1')

        self.username = os.getenv("ig_username")
        self.password = os.getenv("ig_password")
        print(self.username)
        self.driver = webdriver.Chrome(
            executable_path=os.getenv("chrome_path"), options=options)

    def login(self):
        start = 1
        self.driver.set_window_position(0, 0)  # 瀏覽器位置
        self.driver.set_window_size(565, 786)  # 瀏覽器大小
        while start == 1:
            self.driver.get(
                "https://www.instagram.com/")
            time.sleep(1)

            useridNumInput = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
            useridNumInput.send_keys(self.username)
            print('key username')
            passNumInput = self.driver.find_element_by_xpath(
                '//*[@id="loginForm"]/div/div[2]/div/label/input')
            passNumInput.send_keys(self.password)
            print('key password')

            time.sleep(1)

            actions = ActionChains(self.driver)
            login = self.driver.find_element_by_xpath(
                '//*[@id="loginForm"]/div/div[3]/button/div')
            actions.click(login).perform()
            print('click login')

            time.sleep(2)
            # actions = ActionChains(self.driver)
            # dailytask = self.driver.find_element_by_xpath(
            #     '//*[@id="mission-overview"]/div[2]/div[2]/div[1]/div[2]/div/a')
            # actions.click(dailytask).perform()
            # print('click task')

            # time.sleep(2)
            # actions = ActionChains(self.driver)
            # product = self.driver.find_element_by_xpath(
            #     '/html/body/main/div[2]/div/a[1]/div[1]/div')
            # actions.click(product).perform()
            # print('click product')

            # time.sleep(11)
            # self.runtime = self.runtime + 1
            # print('complete ' + str(self.runtime) + ' time')

            # 清除浏览器cookies
            # cookies = self.driver.get_cookies()
            # print(f"main: cookies = {cookies}")
            # self.driver.delete_all_cookies()

            # 删除浏览器全部缓存
            # self.driver.get(
            #     "chrome://settings/clearBrowserData")
            # time.sleep(2)
            # clearButton = self.driver.execute_script(
            #     "return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
            # click on the clear button now
            # clearButton.click()
            # print('clean cache & cookies')
            # time.sleep(1)
            # self.driver.close()
            # SeleniumSpider().login()


if __name__ == '__main__':
    SeleniumSpider().login()

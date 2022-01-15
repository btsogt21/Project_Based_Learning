from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from time import sleep
from Checker import checker
from selenium import webdriver


Fb_user = ""
Fb_pass = ""
chromedriverpath = "C:\\Users\\Batmanlai Tsogt\\Desktop\\chromedriver.exe"
###################################################
# Goto Line 6 and set your Chrome Driver path     #
# exemple : C:\\Users\\Joe\\chromedriver.exe      #
# Goto Line 4 and set your facebook username      #
# Goto line 5 and set your facebook password      #
###################################################


class bot():
    def __init__(self):
        if chromedriverpath == "":
            print("Set FaceBook user name and password to login ! ")
            print("! You should have a Tinder account with Facebook if not create one First")
            
        else:
            # The settings below allow you to bypass chrome's bot detection when signing in using windows 10 64 bit device
            #self.chrome_options = webdriver.ChromeOptions()
            #self.prefs = {"profile.default_content_setting_values.notifications": 2}
            #self.chrome_options.add_experimental_option("prefs", self.prefs)
            #self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
            #self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            #self.chrome_options.add_experimental_option('useAutomationExtension', False)
            #self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            #self.driver = webdriver.Chrome(executable_path=chromedriverpath,options=self.chrome_options)
            #stealth(self.driver,
            #        languages=["en-US", "en"],
            #        vendor="Google Inc.",
            #        platform="Win32",
            #        webgl_vendor="Intel Inc.",
            #        renderer="Intel Iris OpenGL Engine",
            #        fix_hairline=True,
            #)

            # another option to bypass bot detection is to just use your local chrome user profile through selenium. You'll have to change the local directory accordingly. This allows you to completely bypass needing to log in through google, provided that you are already logged into tinder on whichever user profile you use.
            self.chrome_options = webdriver.ChromeOptions()
            self.prefs = {"profile.default_content_setting_values.notifications": 2}
            self.chrome_options.add_experimental_option("prefs", self.prefs)
            self.chrome_options.add_argument(r"user-data-dir=C:\\Chrome_Profiles\\User Data") #if you are using chrome concurrently during the running of this application you may find it more convenient to copy over your user_data directory to a new location and use that new folder here. Otherwise, if you want to use your original user_data directory, you need to close all active chrome sessions before running this script.
            self.chrome_options.add_argument(r'--profile-directory=Profile 1') #specify which chrome user profile you want to use here. 
            self.driver = webdriver.Chrome(executable_path=chromedriverpath, options=self.chrome_options)
            # yet another option is to utilize a modified version of chromedriver that bypasses bot detection

    def login(self):

        self.driver.maximize_window()
        self.driver.get('https://tinder.com')
        sleep(2)

        loginbtn = self.driver.find_element(By.XPATH,'//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        sleep(.5)
        loginbtn.click()
        #loginbtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').text
        sleep(.5)
        fb_lgnbtn = self.driver.find_element(By.XPATH,'//*[@id="q-405061102"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
        fb_lgnbtn.click()

        self.driver.get('https://accounts.google.com/o/oauth2/auth/identifier?redirect_uri=storagerelay%3A%2F%2Fhttps%2Ftinder.com%3Fid%3Dauth400728&response_type=permission%20id_token&scope=email%20profile%20openid&openid.realm&include_granted_scopes=true&client_id=230402993429-g4nobau40t3v3j0tvqto4j8f35kil4hf.apps.googleusercontent.com&ss_domain=https%3A%2F%2Ftinder.com&fetch_basic_profile=true&gsiwebsdk=2&flowName=GeneralOAuthFlow')
        self.handle = []
        self.handle = self.driver.window_handles
        print(self.handle)
        print('here')
        sleep(120)
        if 'PHONE' in loginbtn:
            moreoption = self.driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button').click()
            fblogin = self.driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button').click()
        else:
            self.driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()
        sleep(2)

        workspace = self.driver.window_handles[0]
        popup = self.driver.window_handles[1]
        self.driver._switch_to.window(popup)

        sleep(2)

        email_fb = self.driver.find_element(By.XPATH,'//*[@id="email"]')
        email_fb.send_keys(Fb_user)
        passwd_fb = self.driver.find_element(By.XPATH,'//*[@id="pass"]')
        passwd_fb.send_keys(Fb_pass)

        loing_fb = self.driver.find_element(By.XPATH,'//*[@id="u_0_0"]').click()
        sleep(3)

        self.driver.switch_to.window(workspace)

        sleep(2)


    def like(self):

        sleep(2)
        xpath_heart_button = ['//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button', '//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button']
        for i in xpath_heart_button:
            try:
                like = self.driver.find_element(By.XPATH, i)
                like.click()
                break
            except:
                pass
        sleep(1)
    def dislike(self):

        sleep(2)
        xpath_dislike_button = ['//*[@id="q1323319974"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[2]/button', '//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button']
        for i in xpath_dislike_button:
            try:
                dislike = self.driver.find_element(By.XPATH, i)
                dislike.clic    k()
                break
            except:
                pass
        dislike = self.driver.find_element(By.XPATH,'//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        dislike.click()
        sleep(1)

    def sendmsg(self):
        textbox = self.driver.find_element(By.XPATH,'//*[@id="chat-text-area"]')
        textbox.send_keys('Hey Cutie')
        sleep(2)
        sendmsg = self.driver.find_element(By.XPATH,'//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button')
        sendmsg.click()
        sleep(2)

    def getimagelink(self):
        sleep(2)
        link = self.driver.find_element(By.XPATH,'//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/span[1]/div').value_of_css_property('background-image').split('\"')[1]
        return link
    def notintersted(self):
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()



b = bot()
#b.login()
b.driver.maximize_window()
b.driver.get('https://tinder.com')
for i in range(3):
    sleep(2)
    #b.like()
    link = b.getimagelink()
    result = checker(link)
    sleep(1)
    print("result ",result)
    if result == 1:
        b.like()
    else:
        b.dislike()
    #try:
    #    link = b.getimagelink()
    #    result = checker(link)
    #    sleep(1)
    #    print("result ",result)
    #    if result == 1:
    #        b.like()
    #    else:
    #        b.dislike()

    #except :
    #    print('somethign went wrong trying to like and dislike, likely somethign to do with the checker.py or a popup on yoru tinder window (maybe a match!)')
    #    #try :
    #    #    b.sendmsg()
    #    #except :
    #    #    b.notintersted()


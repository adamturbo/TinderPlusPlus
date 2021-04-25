from selenium import webdriver
import urllib.request
import time
import random

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from elasticsearch import Elasticsearch

from tqdm import tqdm

LOCAL = True
es_client = Elasticsearch(hosts=["localhost" if LOCAL else "elasticsearch"])

IS_LINUX = False

driver = webdriver.Firefox(executable_path="geckodriver.exe" if not IS_LINUX else "./chromedriver_linux")

driver.get("https://tinder.com/app/recs")


second_driver = webdriver.Firefox()
second_driver.get("https://instagram.com/")
        
insta_button = second_driver.find_element_by_xpath('//*[@class="aOOlW  bIiDR  "]')
insta_button.click()

time.sleep(2)
second_driver.find_element_by_name("username").send_keys("VinLoring@gmail.com")
time.sleep(2)
second_driver.find_element_by_name("password").send_keys("Tinder123")

insta_button_connect = second_driver.find_element_by_xpath('//*[@class="sqdOP  L3NKy   y3zKF     "]').click()

classbutton = "button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Px(24px) Px(20px)--s Py(0) Bdrs(0) Mih(40px) Fw($semibold) focus-button-style Fz($s) Bdrs(4px) Bg(#fff) C($c-pink) Bg($primary-gradient):h C(#fff):h"
python_button = driver.find_element_by_xpath('//*[@class="'+ classbutton +'"]')
python_button.click()

connect_phone_number = "Connexion avec un numéro de tél."
python_button = driver.find_element_by_xpath('//*[@aria-label="'+ connect_phone_number +'"]')
python_button.click()

driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

python_button = driver.find_element_by_id("home_children_button")
python_button.click()

i = 11

img = driver.find_element_by_id("game_challengeItem_image")
src = img.get_attribute('src')
name = "image_0" + str(i) + ".png"
urllib.request.urlretrieve(src, name)
i += 1

filedata = urllib.request.urlopen(src)
datatowrite = filedata.read()
 
with open('/projet/ESGI/3ESGI/NoSQL/BotCapcha/' + name, 'wb') as f:
    f.write(datatowrite)

driver.switch_to.default_content()
phone_element = driver.find_element_by_name("phone_number")
phone_element.send_keys("0695776028")

def TakeInstagram():
    try:
        class_desc = "P(16px) Ta(start) Us(t) C($c-secondary) BreakWord Whs(pl) Fz($ms)"
        takedesc = driver.find_element_by_xpath('//*[@class="'+ class_desc +'"]')
        takedesc = takedesc.find_elements_by_css_selector("*")

        insta_list = [ "📷 ", "📸 ", "📷: ", "📸: ", "📷 : ", "📸 : ","@",
            "IG: ", "Ig: ","ig: ", "insta: ", "instagram: ", "Insta: ", "Instagram: ", "INSTA: ", "INSTAGRAM: ",
            "IG, ", "Ig, ","ig, ", "insta, ", "instagram, ", "Insta, ", "Instagram, ", "INSTA, ", "INSTAGRAM: ",
            "IG,", "Ig,","ig,", "insta,", "instagram,", "Insta,", "Instagram,", "INSTA,", "INSTAGRAM,",
            "IG:", "Ig:","ig:", "insta:", "instagram:", "Insta:", "Instagram:", "INSTA:", "INSTAGRAM:",
            "IG : ", "Ig : ", "ig : ", "insta : ", "instagram : ", "Insta : ", "Instagram : ", "INSTA : ", "INSTAGRAM : ",
            "IG :", "Ig :","ig :", "insta :", "instagram :", "Insta :", "Instagram :", "INSTA :", "INSTAGRAM :",
            "IG ", "Ig ","ig ", "insta ", "instagram ", "Insta ", "Instagram ", "INSTA  ", "INSTAGRAM "]

        description = takedesc[0].text
        instagram = ""
        description = description.split("\n")

        for desc_split in description:

            for insta_occurent in insta_list:

                result = desc_split.find(insta_occurent, 0, len(desc_split))
                if result != -1:
                    start = result + len(insta_occurent)
                    instagram = desc_split[start: len(desc_split)]
                    break

        instagramlist = instagram.split(" ")

        for word in instagramlist:
            
            if word != " " and word != "" and word != "➡️":
                instagram = word;
                break
        instagram = instagram.replace("(", "").replace(")", "").replace("/", "")
        return instagram
    
    except:
        
        return ""

def TakeTag():
    try:
        class_tag = "Mt(4px)"
        taketag = driver.find_element_by_xpath('//*[@class="'+ class_tag +'"]')
        taketag = taketag.find_elements_by_css_selector("*")
        
        list_tag = []
        
        for tag in taketag:
            list_tag.append(tag.text)
        
        
        return list_tag
    
    except:
        
        return []

def TakeName():
    try:
        class_name = "Fz($xl) Fw($bold) Fxs(1) Fxw(w) Pend(8px) M(0) D(i)"
        takename = driver.find_element_by_xpath('//*[@class="'+ class_name +'"]')
        
        return takename.text
    
    except:
        
        return ""

def TakeAge():
    try:
        class_age = "Whs(nw) Fz($l)"
        takeage = driver.find_element_by_xpath('//*[@class="'+ class_age +'"]')
        
        return takeage.text
    
    except:
        
        return ""


def TakePicture(kk):
    try:
    
        second_driver.get("https://instagram.com/" + kk)
        
        insta_picture_balise = second_driver.find_element_by_xpath('//*[@class="_6q-tv"]')
        insta_picture = insta_picture_balise.get_attribute("src")
        
        try:
            fail = second_driver.find_element_by_xpath('//*class="_7UhW9      x-6xq    qyrsm KV-D4          uL8Hv     l4b0S    "]')
            return ""
        except:
            return insta_picture
    
    except:
        
        return ""

def PushDataBase(data):
    es_client.index(index="tinderplusplus", doc_type='algo', id=None, body=data)

for i in tqdm(range(50)):
    driver.switch_to.default_content()
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_UP + 't')
    actions.perform()
    insta = TakeInstagram()
    if insta != "":
        tag = TakeTag()
        name = TakeName()
        age = TakeAge()
        picture = TakePicture(insta)

        data = {
            "name": name,
            "instagram": insta,
            "age": age,
            "picture": picture,
            "tag": tag
        }
        #print(data)

        if picture != "":
            PushDataBase(data)

    rnd = random.randrange(1,5)   

    time.sleep(rnd)
    #actions.send_keys(Keys.ARROW_RIGHT + 't')
    actions.send_keys(Keys.ARROW_LEFT + 't')
    actions.perform()   
    time.sleep(2)

es_client.count(index='tinderplusplus', doc_type='algo')["count"]

try:
    result = es_client.search(index="tinderplusplus", body={"query": {"match_all": {}}})
    ids = []
    for hit in result['hits']['hits']:
        print("Name : {name}\nAge : {age}\nPicture : {picture} \nInstagram : {instagram} \nTags : {tag} \n".format(**hit['_source']))
        print("******************")
        ids.append(hit["_id"])
except:
     None

driver.close()
seconddriver.close()
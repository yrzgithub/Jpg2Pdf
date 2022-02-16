import file_path_adder
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as cm
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from keyboard import wait as key_wait
from easygui import enterbox,msgbox
from os import listdir,rename
from os.path import join

pth = r"D:\R\saved screenshot images"
combined = "/html/body/main/div/div[4]/button"

prefs = {"download.default_directory":r"D:\R\R outputs"}
options = ChromeOptions()
options.add_experimental_option("prefs",prefs)
driver = Chrome(service = Service(cm().install()),chrome_options = options)
driver.get(r"https://jpg2pdf.com/")

def ById(id):
    return driver.find_element(By.ID,id)

def ByXp(xp):
    return driver.find_element(By.XPATH,xp)

byxp = ByXp
byid = ById

files = listdir(pth)

up = byid(r"fileSelector")
for i in files:
    path = join(pth,i)
    print(path)
    up.send_keys(path)
    

wait(driver,600).until(ec.element_to_be_clickable((By.XPATH,combined)))
byxp(combined).click()
key_wait("esc")
driver.quit()

name = enterbox(title = "R",msg = "R Output file name : ")
rename(r"D:\R\R outputs\jpg2pdf.pdf",r"D:\R\R outputs\{name}.pdf".format(name = name))
msgbox(title = "R",msg = "File Saved SuccessFully")
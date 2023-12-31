from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

chrome_driver_path = r'C:/Users/rrizzon/Desktop/Class35/Mod3/CIS403(Python)/week17/project3/chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://oxylabs.io/blog')

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-16nzj3b')))

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

results = []
otherresults = []
for a in soup.find_all(class_='css-16nzj3b e1qkxeay1'):
    name = a.find(class_='css-rmqaiq e1dscegp1')
    if name and name.text not in results:
        results.append(name.text)

for b in soup.find_all(class_="css-12w6mvz e9shfhl0"):
    date = b.find(class_='css-weczbu e1ymydvc2')
    if date and date.text not in results:
        otherresults.append(date.text)

print(results)
print(otherresults)
df = pd.DataFrame({'Names': results, 'Dates': otherresults})
df.to_csv('names.csv', index=False, encoding='utf-8')

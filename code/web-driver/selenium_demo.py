import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from py2neo import Graph, Node, Relationship
from selenium.webdriver.common.keys import Keys
g = Graph(password="1234")
page_url = "https://www.google.com/"


driver = webdriver.Chrome('./chromedriver')

company_list = ["Microsoft","Apple","Uber", "Youtube"]
person_name_list = g.run("MATCH (p:Person) RETURN p.name as name").data()

for person in person_name_list:
    driver.get(page_url)
    searchBox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    searchBox.send_keys(person['name'])
    searchBox.send_keys(Keys.RETURN)
    try:
        dob = driver.find_element_by_xpath('//*[@id="rhs"]/div/div[1]/div[1]/div[1]/div/div[2]/div/div[3]/div/div/span[2]').text
        print(person['name'] +":" +dob)
        time.sleep(2)
    except:
          print(person['name'],"ERROR")

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import argparse

parser = argparse.ArgumentParser(prog="PROG")
parser.add_argument("-m", "--message", nargs="?", default="", help="Extra message to add to details.")
parser.add_argument("-n", "--number", nargs="?", default=1, type=int, help="Number of cookies to add.")
arguments = parser.parse_args()

chromedriver = webdriver.Chrome()
chromedriver.get("https://app.uhds.oregonstate.edu/food2you/")

parameters = []
with open("config.txt", "r+") as opened:
    for line in opened:
        parameters.append(line)

element = chromedriver.find_element_by_id('username')
element.send_keys(parameters[0])
element = chromedriver.find_element_by_id('password')
element.send_keys(parameters[1])

# element = chromedriver.find_element_by_class("6FreshBakedCookies")
# element.click()

element = chromedriver.find_element_by_css_selector("[data-id='41']")
for i in range(arguments.number):
    element.click()

element = chromedriver.find_element_by_id("verify")
element.send_keys(parameters[2])

element = chromedriver.find_element_by_id("phone")
element.send_keys(parameters[3])

if arguments.message != None:
    element = chromedriver.find_element_by_id("notes")
    element.send_keys(arguments.message)

element = chromedriver.find_element_by_xpath('//*[@id="order"]/div/div[4]/input')
element.click()

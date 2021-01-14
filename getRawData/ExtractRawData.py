
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
from selenium import webdriver
import sys
import re
import random

class ExtractRawData:

    driver = webdriver.Chrome('chromePath')
    optionList = []
    def setDeafultPage(self, optionNum, pageNum):
        self.driver.get(
            'https://finance.naver.com/sise/sise_market_sum.nhn?&page=' + str(pageNum))
        if len(self.optionList) == 0:
            self.optionList = ["option1", "option4","option6","option12","option15","option21"]
        while len(self.optionList) > 0:
            xPath = '''//*[@id="''' + self.optionList[0] + '''"]'''
            e = self.driver.find_element_by_xpath(xPath)
            e.click()
            self.optionList.pop(0)
        optionCheckNum = 1
        for i in range(1,7):
            opNum = i + optionNum * 7
            Option = "option" + str(opNum)
            self.optionList.append(Option)
            xPath = '''//*[@id="''' + Option + '''"]'''
            try:
                e = self.driver.find_element_by_xpath(xPath)
                e.click()
            except:
                pass
            optionCheckNum += 1
        xPath = """//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]/img"""
        e = self.driver.find_element_by_xpath(xPath)
        e.click()


    def getDrawData(self):
        returnList = []

        for _ in range(10):
            pageNum = 1
            for opNum in range(0,4):
                colNameList = []
                oneRow = []
                if opNum == 0:
                    firstOption = True
                else:
                    firstOption = False
                self.setDeafultPage(opNum, pageNum)
                html = self.driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                stockTable = soup.find("table", attrs={'class':'type_2'})

                stockColName = stockTable.findAll("th", attrs={'scope':'col'})
                for k in range(len(stockColName)):
                    colNameList.append(stockColName[k].get_text())
                stockList = stockTable.findAll("tr")
                for i in range(3,len(stockList)):
                    try:
                        stockNumber = stockList[i].findAll("td")
                        for j in range(0, len(stockNumber)):
                            value = (stockNumber[j].get_text())
                            value = re.sub("\\n", "", value)
                            value = re.sub("\\t", "", value)
                            oneRow.append(value)
                    except:
                        break
                print(colNameList)
                print(oneRow)
            pageNum += 1


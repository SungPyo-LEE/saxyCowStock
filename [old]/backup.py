# while optionCheckNum<7: #랜덤필터
#     opNum = random.randrange(1,27)
#     if opNum in self.optionList:
#         pass
#     else:
#         Option = "option" + str(opNum)
#         self.optionList.append(Option)
#         xPath = '''//*[@id="''' + Option + '''"]'''
#         try:
#             e = self.driver.find_element_by_xpath(xPath)
#             e.click()
#         except:
#             pass
#         optionCheckNum += 1
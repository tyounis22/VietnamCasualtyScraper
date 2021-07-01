
#Import relevant libraries 
from os import defpath
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib
from selenium.webdriver.chrome.options import Options
from time import sleep
from tqdm import tqdm
import json

class VeteranScraper:
    '''The purpose of this class is to scrape information on every single American soldier who died in Vietnam. 
    On the website, soldiers are organized alphabetically by last name. The scraper takes on one letter at a time, 
    assembling a list of links for the soldiers in each letter group, and iterating through these links, scraping
    data such as name, date of birth, date of death, and a portrait photograph of each soldier, the information is 
    saved in a local json file and a separate file for the pictures in png format'''
    def __init__(self):
        '''defines driver, baseURL and empty lists to be used later on in the scraping'''
        self.baseURL = "https://www.virtualwall.org/da/0a.htm"
        self.driver = webdriver.Chrome()
        self.setup()
        self.linkOfNames = []
        self.listOfVeteranInfoDictionaries = []
        
    def setup(self): 
        '''adds an implicit wait to the driver that will be used throughout the project'''
        self.driver.implicitly_wait(10)
    
    def getSoldierLinks(self):
        '''creates a list of links of each soldiers profile'''
        self.driver.get(self.baseURL)
        tableOfNames = self.driver.find_element_by_class_name("names")
        linkElements = tableOfNames.find_elements_by_tag_name("a")
        for link in linkElements:
            soldier_link = link.get_attribute("href")
            self.linkOfNames.append(soldier_link)
        print(self.linkOfNames)
    
    def casualtyScraper(self):
        '''iterates over the list of links of each soldier profile, scraping relevant information into a list of of dictionaries, and downloading a picture of them to a local file'''
        for link in tqdm(self.linkOfNames):
            try:
                
                self.driver.get(link)
                window_before = self.driver.window_handles[0]
                soldier_info = self.driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/center/div[2]/a[4]")
                soldier_info.click()
                window_after = self.driver.window_handles[1]
                self.driver.switch_to_window(window_after)
                sleep(1)
                
                soldier_name = self.driver.find_element_by_xpath("/html/body/div[1]").text
                soldier_rank = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[9]/td[2]").text
                date_of_birth = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td[2]").text
                hometown = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td[2]").text
                service_branch = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[7]/td[2]").text
                military_occupational_speciality_code = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[12]/td[2]").text
                id_number = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[11]/td[2]").text
                unit = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[14]/td[2]").text
                start_of_tour = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[16]/td[2]").text
                date_of_death = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[18]/td[2]").text
                age_at_death = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[21]/td[2]").text
                location_of_death = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[22]/td[2]").text
                remains_status = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[23]/td[2]").text
                casualty_type = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[26]/td[2]").text
                casualty_reason = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[27]/td[2]").text
                casualty_detail = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[28]/td[2]").text
                
                
                self.driver.switch_to_window(window_before)
                sleep(1)
                img = self.driver.find_element_by_xpath('/html/body/center/p/table[1]/tbody/tr[1]/td[2]/img')
                src = img.get_attribute('src')
                urllib.request.urlretrieve(src, f"/Users/Tareq/Desktop/VietnamWar/veteran_portraits/{soldier_name}.png")
                
                soldier_dictionary = {
                    'soldier_name' : soldier_name,
                    'soldier_rank' : soldier_rank,
                    'date_of_birth' : date_of_birth,
                    'hometown' : hometown,
                    'service_branch' : service_branch,
                    'military_occupational_speciality_code' : military_occupational_speciality_code,
                    'id_number' : id_number, 
                    'unit' : unit,
                    'start_of tour' : start_of_tour,
                    'date_of_death' : date_of_death,
                    'age_at_death' : age_at_death, 
                    'location_of_death' : location_of_death,
                    'remains_status' : remains_status, 
                    'casualty_type' : casualty_type,
                    'casualty_reason' : casualty_reason, 
                    'casualty_detail' : casualty_detail
                            }   
                self.listOfVeteranInfoDictionaries.append(soldier_dictionary)
            except NoSuchElementException:
                pass
            except:
                pass
                
    def jsonDump(self):        
        with open('soldier_data.json', 'w') as f:
            json.dump(self.listOfVeteranInfoDictionaries, f, indent=4)
            
asdas = VeteranScraper()
asdas.getSoldierLinks()
asdas.casualtyScraper()
asdas.jsonDump()

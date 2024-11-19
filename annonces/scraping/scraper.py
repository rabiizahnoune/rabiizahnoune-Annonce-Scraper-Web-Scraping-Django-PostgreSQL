import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from annonces.scraping.utils import WebScraperUtils
from selenium.webdriver.common.by import By
from tqdm import tqdm


class ApartmentLinkScraper:
    def __init__(self, product, num_pages):
        self.product = product
        self.num_pages = num_pages
        self.links = []
        self.utils = WebScraperUtils()

    def scrape_links(self):
        """Scrape apartment links across multiple pages."""
        
        base_url = f"https://www.avito.ma/fr/maroc/appartements/{self.product}"

        for page in tqdm(range(1, self.num_pages + 1)):
            url = base_url if page == 1 else f"{base_url}?o={page}"
            self.utils.driver.get(url)
            time.sleep(2)

            apartment_elements = self.utils.driver.find_elements(By.XPATH, "//a[@class='sc-1jge648-0 eTbzNs']")
            for element in tqdm(apartment_elements):
                link = element.get_attribute('href')
                if link:
                    self.links.append(link)

        self.utils.close_driver()
        return self.links

    def save_links_to_file(self, path):
        """Save scraped links to a file."""
        with open(path, 'w', encoding='utf-8') as file:
            for link in self.links:
                file.write(link + '\n')
        print('Links saved to file.')




class ApartmentDataScraper:
    def __init__(self, links):
        self.links = links
        self.utils = WebScraperUtils()
        self.appartements_data = []

    def scrape_data(self):
       
        for link in tqdm(self.links):
            self.utils.driver.get(link.strip())
            time.sleep(2)
            try:

               equipement_elements = self.utils.driver.find_elements(By.CLASS_NAME, 'sc-1x0vz2r-0.bXFCIH')

               equipements_list = []

               for equipement_element in equipement_elements:
                    equipements_list.append(equipement_element.text.strip())

               equipements_string = "/".join(equipements_list)
            except NoSuchElementException:
                   equipements_string="NaN"

            data = {
                "title": self.utils.get_text_or_nan("//div[@class='sc-1g3sn3w-9 kvOteU']"),
                "price": self.utils.get_text_or_nan("//p[@class='sc-1x0vz2r-0 lnEFFR sc-1g3sn3w-13 czygWQ']"),
                "location": self.utils.get_text_or_nan("//span[@class='sc-1x0vz2r-0 iotEHk']"),
                "nb_rooms":self.utils.get_text_or_nan("//*[@id='__next']/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div/span"),
                "nb_baths":self.utils.get_text_or_nan("//*[@id='__next']/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div/span"),
                "surface_area": self.utils.get_text_or_nan("//li[.//span[text()='Surface habitable']]/span[@class='sc-1x0vz2r-0 gSLYtF']"),
                "equipment":equipements_string,
                "link": link.strip()
            }
            self.appartements_data.append(data)
        self.utils.close_driver()
        return self.appartements_data

    def save_data_to_csv(self, path):
        """Save scraped apartment data to a CSV file."""
        df = pd.DataFrame(self.appartements_data)
        df.to_csv(path, index=False)
        print('Data saved to CSV.')


import random
from datetime import datetime,timedelta
def random_datetime(start=None, end=None):
    """Génère une date et heure aléatoires entre start et end."""
    if start is None:
        start = datetime(2023, 1, 1, 0, 0, 0)
    if end is None:
        end = datetime(2024, 1, 1, 0, 0, 0)
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)
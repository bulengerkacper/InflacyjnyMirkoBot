from bs4 import BeautifulSoup
import requests

class Scrapper:

    def __init__(self):
        _a='a'

    def get_base_rate_from_pkobp(self): #works ok
        url = "https://www.pkobp.pl/waluty/#/base_rate"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        result = soup.find_all("p", class_="course__irs-tab-subtitle")
        for res in result:
            if "stała stopa bazowa" in res.contents[0]:
                return res.contents[0]
    
    def get_wibors_from_pkobp(self):
        url = "https://www.pkobp.pl/waluty/#/interbank"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        result = soup.find_all("table", class_="course__table course__table--irs")
        for res in result:
            content=res.getText()
            if "WIBOR" in content:
                start="3-mc"
                end="6-mc"
                start2=end
                end2="9-mc"
                wibor3m="Wibor 3m:"
                wibor6m="Wibor 6m:"
                wibor3m+=content[content.find(start)+len(start):content.rfind(end)]
                wibor6m+=content[content.find(start2)+len(start2):content.rfind(end2)]
                concat=wibor3m+ "\n" + wibor6m
                return concat
        return "Cannot fetch wibor data from pkobp"

    def get_interests_rate_from_nbp(self):
        url="https://www.nbp.pl/"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        result = soup.find_all("td")
        content="Stopa referencyjna nbp: "
        for r in result:
            if "Referencyjna" in r.get_text():
                content += r.next_sibling.next_sibling.get_text().strip()
                return content

    def collect_all_data(self):
        return "PKOBP\n" + self.get_wibors_from_pkobp() +"\n" + self.get_base_rate_from_pkobp() + "\nNBP\n" + self.get_interests_rate_from_nbp()


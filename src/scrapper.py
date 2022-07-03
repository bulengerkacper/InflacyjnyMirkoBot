from bs4 import BeautifulSoup
import requests

class Scrapper:

    def get_base_rate_from_pkobp(self): #works ok
        url = "https://www.pkobp.pl/waluty/#/base_rate"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        result = soup.find_all("p", class_="course__irs-tab-subtitle")
        for res in result:
            if "stała stopa bazowa" in res.contents[0]:
                data = res.contents[0].split()
                return "Stała stopa bazowa:" + data[-1]
    
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
                concat=wibor3m+ "  " + wibor6m
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
        return "Cannot fetch data from nbp"
    
    def get_wibor_from_mbank(self):
        url="https://www.mbank.pl/pomoc/oprocentowanie/firmy/"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        result = soup.find_all("td")
        content="Wibor 3M "
        for r in result:
            if "WIBOR 3M dla PLN" in r.get_text():
                content += r.next_sibling.next_sibling.get_text().strip()
                return content
        return "Cannot fetch data from mbank"

    def get_wibor_from_ing(self):
        url="https://www.ing.pl/indywidualni/kredyty-i-pozyczki/kredyt-hipoteczny/informacje-ogolne-o-kredycie-hipotecznym"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        #result = soup.find_all("table", class_="table_type2")
        result2 = soup.find_all("td")
        for r in result2:
            if "Oprocentowanie" in r.get_text():
                content=r.next_sibling.next_sibling.get_text()
                s2 = "WIBOR 6M "
                return (content[content.index(s2) + len(s2):].strip())

    def get_wibor_from_peako(self):
        url = "https://www.pekaobh.pl/strefa-klienta-main/wibor.html"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        result = soup.find_all("td")
        wibor6m= (result[-1].text)
        wibor3m= (result[-2].text)
        return "Wibor 6M: " + wibor6m + "wibor 3M: " + wibor3m
            
    def combine_all_data(self):
        return "PKOBP:(Aktualizacja w dni robocze)\n" + self.get_wibors_from_pkobp() +"\n" + self.get_base_rate_from_pkobp() + \
            "\nPEAKO (Aktualizacja w dni robocze):\n" + self.get_wibor_from_peako() +  \
         "\nMBANK(Aktualizacja raz na 3 miesiace):\n" + self.get_wibor_from_mbank()  + \
            "\nING(Aktualizacja raz na 6 miesiecy):\nWIBOR6M :" + self.get_wibor_from_ing() +  "\nNBP:  " + self.get_interests_rate_from_nbp()


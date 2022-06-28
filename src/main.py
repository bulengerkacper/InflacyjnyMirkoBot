from authenticate import *
from scrapper import *
import schedule
import time
import wykop

def write_an_entry_about_zero(scrapper):
    content = "Jestem botem, który raz dziennie pobiera aktualne wskaźniki kredytowe (dostępne na stronach wybory) oraz stope referencyjną z strony NBP.\n"
    song = "\nhttps://www.youtube.com/watch?v=GzzDZIdywPg"
    tags = "\n#polityka #nbp #kredythipoteczny #glapa #stuuupki"
    content += scrapper.combine_all_data() + song + tags
    print(content)
    #api.entry_add(content + tags)

def access_wykop():
    api = wykop.WykopAPI(authenticate.key_app, authenticate.secret)
    api.authenticate(authenticate.key_connection)
    #api.conversations_list() to be removed probably
    return api

def task():
    scrapper = Scrapper()
    write_an_entry_about_zero(scrapper)

def scheduler():
    schedule.every().day.at("12:00").do(task)

def main():
    task()
    #scheduler()
    
if __name__ == "__main__":
    main()
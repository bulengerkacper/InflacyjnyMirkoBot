from authenticate import *
from scrapper import *
import wykop

def main():
    #api = access_wykop()
    scrapper = Scrapper()
    write_an_entry_about_zero(scrapper)

def write_an_entry_about_zero(scrapper):
    content = "Jestem botem, który raz dziennie pobiera aktualne wskaźniki kredytowe (dostępne na stronach wybory) oraz stope referencyjną z strony NBP.\n"
    song = "\nhttps://www.youtube.com/watch?v=GzzDZIdywPg"
    tags = "\n#polityka #nbp #kredythipoteczny #glapa #stuuupki"
    content += scrapper.combine_all_data() + song + tags
    print(content)
    #api.entry_add(content + tags)

if __name__ == "__main__":
    main()

def access_wykop():
    api = wykop.WykopAPI(authenticate.key_app, authenticate.secret)
    api.authenticate(authenticate.key_connection)
    api.conversations_list()
    return api
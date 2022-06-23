from authenticate import *
from scrapper import *
import wykop

def main():
    #api = wykop.WykopAPI(authenticate.key_app, authenticate.secret)
    #api.authenticate(authenticate.key_connection)
    #api.conversations_list()
    scrapper = Scrapper()
    write_an_entry_about_zero(scrapper)

def write_an_entry_about_zero(scrapper):
    content = "Jestem botem, który raz dziennie pobiera aktualne wskaźniki z stron nbp i banków.\n"
    content += scrapper.collect_all_data()
    tags ="\n#polityka #nbp #kredythipoteczny #glapa #stuuupki"
    print(content + tags)
    #api.entry_add(content + tags)

if __name__ == "__main__":
    main()
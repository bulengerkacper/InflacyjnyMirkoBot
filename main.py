from authenticate import *
from scrapper import *
import wykop

def main():
    #api = access_wykop()
    scrapper = Scrapper()
    write_an_entry_about_zero(scrapper)

def write_an_entry_about_zero(scrapper):
    content = "Jestem botem, który raz dziennie pobiera aktualne wskaźniki odnośnie stóp procentowych i wskaźników referencyjnych z stron nbp i banków.\n"
    content += scrapper.collect_all_data() + "\n#polityka #nbp #kredythipoteczny #glapa #stuuupki"
    print(content)
    #api.entry_add(content + tags)

if __name__ == "__main__":
    main()

def access_wykop():
    api = wykop.WykopAPI(authenticate.key_app, authenticate.secret)
    api.authenticate(authenticate.key_connection)
    api.conversations_list()
    return api
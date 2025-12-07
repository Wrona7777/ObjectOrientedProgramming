from contact import Contact
from contact_list import ContactList

def main():
    my_contacts = ContactList()

    my_contacts.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    my_contacts.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    my_contacts.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    my_contacts.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    my_contacts.display_contacts()

if __name__ == "__main__":
    main()
import requests
from requests.auth import HTTPBasicAuth
from config import *
from models import *
from xml_generation import build_xml
import re


def fetch_vcard():
    url = f"{instance.rstrip('/')}/remote.php/dav/addressbooks/users/{username}/{address_book}?export"
    request = requests.get(url, auth=HTTPBasicAuth(username, password))
    return request.content.decode()


def isolate_cards(vcard: str):
    vcard = vcard.replace("\r\n", "\n").replace("\r\n", "\n")
    vcard = vcard.removeprefix("BEGIN:VCARD\n")
    vcard = vcard.removesuffix("END:VCARD\n")
    cards = vcard.split("\nEND:VCARD\nBEGIN:VCARD\n")
    return cards


def parse_cards(cards: list[str]):
    contacts = []
    for card in cards:
        name = re.search(r"(?<=FN:)(.*?)(?=\n)", card)
        name = name.group(0) if name else None

        phone_match = re.findall(r"(?<=TEL;TYPE=)\"?([a-z,]+)\"?:(.*?)(?=\n)", card, re.IGNORECASE)
        phones = []
        for phone in phone_match:
            if phone[1]:
                phones.append(Phone(phone[0].split(","), phone[1]))

        print(name, phones)
        if phones:
            contacts.append(Contact(name, phones))
    return contacts


def vcard_to_xml():
    doc = fetch_vcard()
    cards = isolate_cards(doc)
    contacts = parse_cards(cards)
    return build_xml(contacts)


if __name__ == "__main__":
    xml = vcard_to_xml()
    xml.write("output.xml")

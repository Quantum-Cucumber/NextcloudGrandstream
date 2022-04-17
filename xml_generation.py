import xml.etree.ElementTree as ET
from models import Contact, Phone


def create_base():
    root = ET.Element("AddressBook")
    version = ET.SubElement(root, "version")
    version.text = "1"
    return root


def contact_xml(contact: Contact):
    contact_root = ET.Element("Contact")

    first_name = ET.SubElement(contact_root, "FirstName")
    first_name.text = contact.firstName

    if contact.lastName:
        last_name = ET.SubElement(contact_root, "LastName")
        last_name.text = contact.lastName

    for phone in contact.phones:
        contact_root.append(phone_xml(phone))

    return contact_root


def phone_xml(phone: Phone):
    phone_model = ET.Element("Phone", {"type": phone.type})

    phone_number = ET.SubElement(phone_model, "phonenumber")
    phone_number.text = phone.number
    return phone_model


def build_xml(contacts: list[Contact]):
    root = create_base()
    for contact in contacts:
        root.append(contact_xml(contact))

    tree = ET.ElementTree(root)
    ET.dump(root)

    return tree

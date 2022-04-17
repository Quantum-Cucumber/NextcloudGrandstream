# Nextcloud Grandstream Contacts
Synchronise Grandstream VOIP phonebooks with Nextcloud Contacts, via an [XML file](https://www.grandstream.com/hubfs/Product_Documentation/GXP_XML_phonebook_guide.pdf).

This will create a flask web server that Grandstream phones can access to receive an up-to-date copy of your nextcloud contacts.

## Requirements
- Python 3.10 or higher (due to type annotations)
- An account on a nextcloud instance that has the [Contacts app](https://apps.nextcloud.com/apps/contacts) installed

## Setup
1. Install dependencies - `python3 -m pip install -r requirements.txt`
2. Create `config.py`. A sample config file is provided in [config_sample.py](config_sample.py)

<details><summary>config.py</summary><p>

```python
flask_port = 8000

# Url of your nextcloud server
instance = "https://nextcloud-instance.example"
# Your nextcloud username (case-sensitive)
username = ""
# If you have 2FA on your account you will need to create an app password (Settings > Security > Create new app password)
# Otherwise you can just use your normal account password
password = ""
# The address book to read contacts from. The default address book is "contacts".
# To determine the name of a different address book, enable debug mode for your nextcloud server (set debug => true in config/config.php),
# then navigate to INSTANCE/remote.php/dav/addressbooks/users/USERNAME in your web browser to find a list of address book names
address_book = ""
```

</p></details>

3. Start the server with `python3 main.py`.
4. Verify the config and webserver is working by going to localhost:8000/phonebook.xml in your browser.
5. Configure your Grandstream VOIP phone's phonebook to download over HTTP, setting the path to be the url to your running webserver.
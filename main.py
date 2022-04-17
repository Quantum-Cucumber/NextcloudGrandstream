from flask import *
from config import flask_port
from parsing import vcard_to_xml
from io import BytesIO

app = Flask(__name__)


@app.route("/phonebook.xml")
def contacts():
    tree = vcard_to_xml()

    file = BytesIO()
    tree.write(file)
    file.seek(0)

    return send_file(file, "text/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=flask_port)

import tcppinglib
import json

from email_sender import EmailSender
from doc_validator import validate_document

def app() -> None:
    data = open("data.json")
    data_dict = json.load(data)

    if data_dict is False:
        


if __name__ == "__main__":
    data = open("data.json")
    data_dict = json.load(data)
    print(validate_document(data_dict))


import tcppinglib
import json
import datetime

from email_sender import EmailSender
from doc_validator import validate_document
from typing import Dict, Any
from logger_to_file import file_logger


def app(data: Dict[str, Any]) -> None:
    """
    Function verifies document, checks if it working hours and if id does, 
    pings all needed web sites, sends emails, logs webs statuses and 
    notifies responsible persons in case of some failures.
        
    Parameters
    ----------
    data : Dict
        File provides all config values to function.
    """
    email_manager = EmailSender(login=data["account_id"],
                                password=data["account_psw"])
    if validate_document(data):
       while datetime.datetime.now().hour < data["work_time"]:
           print(data)
    else:
        file_logger.error("Document haven't passed validation process. Please "
                          "check config document.")
        
         
        
    

if __name__ == "__main__":
    data = open("data.json")
    data_dict = json.load(data)
    print(validate_document(data_dict))

    # app(data_dict)

    


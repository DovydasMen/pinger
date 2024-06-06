import tcppinglib
import json
import datetime
import time

from email_sender import EmailSender
from utils import validate_document, is_web_online_count_correct
from typing import Dict, Any
from logger_to_file import file_logger


def app() -> None:
    """
    Function verifies document, checks if it working hours and if id does, 
    pings all needed web sites, sends emails, logs webs statuses and 
    notifies responsible persons in case of some failures.
    """
    json_data =open("data.json")
    data = json.load(json_data)
    document = validate_document(document=data)
    if not document:
        file_logger.error("Document haven't passed validation process. Please "
                          "check config document.")
        file_logger.info("Next check up will starts in 30 min.")
        time.sleep(seconds=30 * 60)
        app()
    email_manager = EmailSender(login=data["account_id"],
                                password=data["account_psw"])
    login_responce = email_manager.server_login()
    if not login_responce:
        file_logger.error("Email login was not succesfully, please check" 
                              "upper error and act accordingly.")
        file_logger.info("Next check up will starts in 30 min.")
        time.sleep(30 * 60)
        app()

    while datetime.datetime.now().hour < data["work_time"]:
        web_json_data = open("web_status.json")
        web_previous_data = json.load(web_json_data)
        web_previous_status = is_web_online_count_correct(web_previous_data, data["max_not_working_pages"])
        web_current_data = []
        
       
       
            

            
        
         
        
    

if __name__ == "__main__":
    app()

    


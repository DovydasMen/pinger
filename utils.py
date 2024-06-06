from typing import Dict,Any
import re



def validate_document(document: Dict[str,Any]) -> bool:
    document_state = True

    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    for email in document["to_addreses"]:
        if email_pattern.match(email):
            continue
        else:
            document_state = False

    if email_pattern.match(document["error_to_addreses"]):
        pass
    else:
        document_state = False

    if email_pattern.match(document["account_id"]):
        pass
    else:
        document_state = False

    if len(document["account_psw"]) == 0:
        document_state = False

    if isinstance(document["max_not_working_pages"],int) == False:
        document_state = False

    for target in document["test_targets"]:
        if isinstance(target,str) != True:
            document_state = False
    
    if isinstance(document["next_check"],int) != True:
        document_state = False
    
    if isinstance(document["work_time"],int) != True:
        document_state = False

    return document_state

def is_web_online_count_correct(status_info :Dict[str,str], max_not_working_count: int) -> bool:
    not_working = 0
    for status in status_info.keys():
        if status_info[status] == "off":
            not_working +=1
    
    return False if not_working >= 2 else True





    

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

    return document_state



    

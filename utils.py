import re
import tcppinglib

from typing import Dict, Any, List


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

def get_ping_results(hosts: Dict[str,str]) -> Dict[str, str]:
    host_status = {}
    for key in hosts.keys:
        if key.startswith(prefix="http://"):
            splited_host = key.split(":")
            port = splited_host[2]
            host = key.replace(old=f":{port}", new="")
            host_responce=tcppinglib.tcpping(address=host,
                                              port=port)
            if host_responce.is_alive:
                host_status[key] = "on"
            else:
                host_status[key] = "off"
        else:
            host_responce = tcppinglib.tcpping(address=key)
            if host_responce.is_alive:
                host_status[key] = "on"
            else:
                host_status[key] = "off"
            
    return host_status

def get_text_down_targets(ping_result: Dict[str,str], next_check: int) -> str:
    web_offline = []
    for key, value in ping_result.items:
        if value == "off":
            web_offline.append(key)
    return f"Hello,\n connection to bellowpages/IP' are down:{"\n".join(str(web_offline))} Next check will be made in {str(next_check)} ammount of hour"








    

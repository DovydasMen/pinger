import smtplib
from smtplib import SMTPHeloError, SMTPAuthenticationError, SMTPException 
from smtplib import SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError
from smtplib import SMTPNotSupportedError
from email.message import EmailMessage
from logger_to_file import file_logger

class EmailSender:
    def __init__(self, login: str, password: str) -> None:
        self.msg = EmailMessage()
        self.acc = login
        self.password = password
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def set_up_message(self, reciever: str, msg_text: str, subject: str) -> None:
        self.msg["From"] = self.acc
        self.msg["To"] = reciever
        self.msg["Subject"] = subject
        self.msg.set_content(msg_text)
    
    def server_login(self) -> bool:
        try:
            self.server.login(self.acc,self.password)
            return True
        except SMTPHeloError:    
            file_logger.exception("The server didn't reply properly to the HELO" 
                                  "greeting.")
            return False
        except SMTPAuthenticationError:
            file_logger.exception("The server didn't accept the "
                                  "username/password combination.")
            return False
        except SMTPException:
            file_logger.exception("No suitable authentication method was" 
                                  "found.")
            return False

    def send_message(self) -> bool:
        try:
            self.server.send_message(self.msg)
            self.server.quit()
            return True
        except SMTPRecipientsRefused:
            file_logger.debug("All recipients were refused")
            return False
        except SMTPSenderRefused:
            file_logger.exception("The server didn't accept the from_addr.")
            return False
        except SMTPDataError:
            file_logger.exception("The server replied with an unexpected error"
                                  "code")
            return False
        except SMTPNotSupportedError:
            file_logger.exception("SMTPUTF8 was given in the mail_options but "
                                  "is not supported by the server.")
            return False
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib
from email.message import EmailMessage
import ssl


class ActionSendMail(Action):

    def name(self) -> Text:
        return "action_send_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        recipient_email = tracker.get_slot("email")
        
        msg = EmailMessage()
        msg['From'] = "sender@gmail.com"
        msg['To'] = recipient_email
        msg.set_content("Hey, this is a demo")

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as server:
            server.login("sender@gmail.com","password")
            server.sendmail("sender@gmail.com", recipient_email, msg.as_string())
            

        return []

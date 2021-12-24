from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormValidationAction, REQUESTED_SLOT
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List, Optional
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import datetime
import string
import re
import json
from .dbutils import *

class ValidateorderForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_order_form"
    
    async def extract_pizza_name(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict,
    ) -> Dict[Text, Any]:
        price_pizza = 0
        if tracker.get_slot(REQUESTED_SLOT) == "pizza_name":
            user_name_pizza = tracker.latest_message.get("text")
            choices = pizza_name.keys()
            fuz_name = process.extractOne(user_name_pizza ,choices)[0]
            print(fuz_name)
            price_pizza = pizza_name.get(fuz_name)
            print (price_pizza)
            return {
                "pizza_name" : fuz_name,
                "total_bill" : tracker.get_slot("total_bill")+int(price_pizza)
            }
        return {}
    
    async def validate_pizza_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict,
    ) -> Dict[Text, Any]:
        return {}
        

    async def extract_size(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict,
        ) -> Dict[Text, Any]:
            price_size = 0
            if tracker.get_slot(REQUESTED_SLOT) == "size":
                user_name_pizza = tracker.latest_message.get("text")
                fuz_name = process.extractOne(user_name_pizza ,size.keys())[0]
                price_size = size.get(fuz_name)
                return {
                    "size" : fuz_name,
                    "total_bill" : tracker.get_slot("total_bill")*int(price_size)
                }
            return {}
    async def validate_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict,
    ) -> Dict[Text, Any]:
        return {}

    async def extract_extra_cheese(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict,
        ) -> Dict[Text, Any]:
            price_cheese = 0
            pizza_name_1 = None
            if tracker.get_slot(REQUESTED_SLOT) == "extra_cheese":
                user_name_pizza = tracker.latest_message.get("text")
                kname = "cheese burst"
                choices = ["yes" , "yup" , "y" ,"indeed" , "of course"]
                aff = process.extractOne(user_name_pizza ,choices)[0]
                if aff in user_name_pizza:
                    price_cheese = cheese.get(kname)
                    return {
                        "extra_cheese" : True,
                        "total_bill": tracker.get_slot("total_bill")+int(price_cheese)
                    }
                else:
                    return{
                        "extra_cheese" : False,
                        "total_bill": tracker.get_slot("total_bill")+int(price_cheese)
                    }
            return {}

    async def validate_extra_cheese(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict,
    ) -> Dict[Text, Any]:
        return {}

    async def extract_side_order(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict,
    ) -> Dict[Text, Any]:
        price_side_order = 0
        pizza_name_1 = None
        if tracker.get_slot(REQUESTED_SLOT) == "side_order":
            user_name_pizza = tracker.latest_message.get("text")
            intent_name = tracker.latest_message.get("intent").get("name")
            if intent_name == "deny":
                return {
                    "side_order" : False,
                    "total_bill" : tracker.get_slot("total_bill")+int(price_side_order)
                }            
            fuz_name = process.extractOne(user_name_pizza , side_order.keys())[0]
            price_side_order = side_order.get(fuz_name)
            return {
                "side_order" : fuz_name,
                "total_bill" : tracker.get_slot("total_bill")+int(price_side_order)
                }

    async def validate_side_order(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict,
    ) -> Dict[Text, Any]:
        return {}

    async def validate_total_bill(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict,
    ) -> Dict[Text, Any]:
        return {}
   

class actionsubmit(Action):
    def name(self) -> Text:
        return "action_submit"
    
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any],
     ) -> List[Dict]:
        slots = tracker.current_slot_values()
        if slots.get("extra_cheese") is False and slots.get("side_order") is not False:
            dispatcher.utter_message(response="utter_empty_cheese")
        elif slots.get("extra_cheese") is True and slots.get("side_order") is False:
            dispatcher.utter_message(response="utter_empty_soder")
        elif slots.get("extra_cheese") is False and slots.get("side_order") is False:
            dispatcher.utter_message(response="utter_both_empty")
        else:
            dispatcher.utter_message(response="utter_thankyou")
        return []   

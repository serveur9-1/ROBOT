# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import requests
import json

from typing import Any, Text, Dict, List, Union, Optional

from rasa.shared.core.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.types import DomainDict

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ValidateRecuperationDuForm(FormValidationAction):
    """ Exemple of validation action."""
    
    def name(self) -> Text:
        return "validate_recuperation_du_form"
    
    @staticmethod
    def required_slot() -> List[Text]:
        """Mes données obligatoires"""
        return ["nom_personne"]
        
    def validate_nom_personne(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate nom_prenom value."""

        if slot_value is not None:
            # Le nom_prenom est valid, tu peux donc faire la suite de tes action
            
            print( "La valeur de mon slot. ----   " + str(slot_value))
            return {"nom_personne": slot_value}
        else:
            # La validation à echouer 
            # Comme tu as mis un loop l'utilisateur sera demander de nouveau
            return {"nom_personne": None}
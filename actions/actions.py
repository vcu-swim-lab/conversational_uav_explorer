# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_display_info"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        s = []
        for item in tracker.latest_message["entities"]:
            n = {
                "entity" : item["entity"],
                "value" : item["value"]
            }
            s.append(n)
        date_picker = {
            "intent" : tracker.latest_message["intent"]["name"],
            "slots" : s
        }
        dispatcher.utter_message(text = json.dumps(date_picker, sort_keys=True, indent=2, separators=(',', ': ')))

        return []

# class ActionExploreTrue(Action):
#    def name(self) -> Text:
#       return "action_explore_t"

#    def run(self,
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#       return [SlotSet("explore", True)]

# class ActionExploreFalse(Action):
#    def name(self) -> Text:
#       return "action_explore_f"

#    def run(self,
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#       return [SlotSet("explore", None)]
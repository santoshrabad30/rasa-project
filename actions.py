# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core.events import AllSlotsReset
from rasa_core.events import Restarted
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from rasa.core.tracker_store import TrackerStore
from rasa.core.trackers import ActionExecuted, DialogueStateTracker, EventVerbosity
import requests
from rasa_core.domain import Domain
import json

# main class to get the capital name of respective country
class CapitalForm(FormAction):
    def name(self) -> Text:
        return "capital_form"
    @staticmethod
    def required_slots(tracker):
        return ["capital_name"]
    def slot_mappings(self) :
        return {
            "capital_name"    : [self.from_text()],
        }

    def validate_capital_name(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any])->Any:
        lst = ["USA","India", "Greece", "Sweden", "Australia", "Finland","Japan","Russia"]
        if value not in lst:
            return {"capital_name": value}
        else:
            dispatcher.utter_template("utter_wrong_capital_name", tracker)
            return {"capital_name": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],
    ) -> List[Dict] :
        location = tracker.get_slot("capital_name") # get the user click button payload value
        #trac_country = location
        PARAMS = {"country":location}
        headers = {'content-type': 'application/json'}

        url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital"
        response = requests.post(url, data = json.dumps(PARAMS), headers=headers) # post the url with headers and data
        #data = json.loads(response)
        data = response.json()
        ans = data['body']['capital']
      
        print(ans)
        return [SlotSet("trac_capital", ans), SlotSet("trac_country", location)] # return the fetch capital from api and clicked country by user

class PopulationForm(FormAction):
    def name(self) -> Text:
        return "population_form"
    @staticmethod
    def required_slots(tracker):
        return ["total_population"]
    def slot_mappings(self) :
        return {
            "total_population"    : [self.from_text()],
        }
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],
    ) -> List[Dict] :
        location = tracker.get_slot("total_population")
        PARAMS = {"country":location}
        headers = {'content-type': 'application/json'}
        url =  "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation"
        response = requests.post(url, data = json.dumps(PARAMS), headers=headers)
        data = response.json()
        ans = data['body']['population']
        print(ans)
        return [SlotSet("trac_population", ans), SlotSet("trac_pcountry", location)]


# function to get capial name by country name 
def getcapital(name_capital):
    if name_capital == "India_capital":
        location = "India"
    elif name_capital == "USA_capital":
        location = "USA"
    elif name_capital == "Greece_capital":
        location = "Greece"
    elif name_capital == "Sweden_capital":
        location = "Sweden"
    elif name_capital == "Australia_capital":
        location = "Australia"
    elif name_capital == "Finland_capital":
        location = "Finland"
    elif name_capital == "Japan_capital":
        location = "Japan"
    else:
        location = "Russia"
    PARAMS = {"country":location}
    headers = {'content-type': 'application/json'}
    url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital"
    response = requests.post(url, data = json.dumps(PARAMS), headers=headers)
    data = response.json()
    fullcapitalname = data['body']['capital']

    return fullcapitalname,location 



class ActionGetCapital(Action):
    def name(self):
        return "action_get_capital"
    def run(self, dispatcher, tracker, domain):
        cap_name = tracker.latest_message['intent'].get('name') # in this line we get the intent name and pass this intent to the function to get respective capital name
        trac_capital, trac_country = getcapital(cap_name) 
        #print(trac_capital)
        #print(trac_country)
        return [SlotSet("trac_capital", trac_capital), SlotSet("trac_country", trac_country)] # return the slot values 


# function to return population of corresponding country
def getpopulation(total_pop):
    if total_pop == "India_population":
        location = "India"
    elif total_pop == "USA_population":
        location = "USA"
    elif total_pop == "Greece_population":
        location = "Greece"
    elif total_pop == "Sweden_population":
        location = "Sweden"
    elif total_pop == "Australia_population":
        location = "Australia"
    elif total_pop == "Finland_population":
        location = "Finland"
    elif total_pop == "Japan_population":
        location = "Japan"
    else:
        location = "Russia"
    PARAMS = {"country":location}
    headers = {'content-type': 'application/json'}
    url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation"
    response = requests.post(url, data = json.dumps(PARAMS), headers=headers)
    data = response.json()
    totalpopulation = data['body']['population']

    return totalpopulation,location


class ActionGetPopulation(Action):
    def name(self):
        return "action_get_population"
    def run(self, dispatcher, tracker, domain):
        tot_population = tracker.latest_message['intent'].get('name') # in this line we will get the intent of user message
        trac_population, trac_pcountry = getpopulation(tot_population) # call the getpoulation function to get the population of corresponding country
        return [SlotSet("trac_population", trac_population), SlotSet("trac_pcountry", trac_pcountry)] # return the slot population & country name



# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


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
        url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries"
        country_name = requests.get(url)
        country = (country_name.text)
        data = json.loads(country)
        capital_list = data['body']

        if value in capital_list:
            return {"capital_name": value}
        else:
            dispatcher.utter_template("utter_wrong_capital_name", tracker)
            return {"capital_name": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],
    ) -> List[Dict] :
        location = tracker.get_slot("capital_name")
        #trac_country = location
        PARAMS = {"country":location}
        headers = {'content-type': 'application/json'}

        url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital"
        response = requests.post(url, data = json.dumps(PARAMS), headers=headers)
        #data = json.loads(response)
        data = response.json()
        ans = data['body']['capital']
      
        print(ans)
        return [SlotSet("trac_capital", ans), SlotSet("trac_country", location)]

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
    def validate_total_population(self, value:Text, dispatcher:CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any])->Any:
        url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries"
        country_name = requests.get(url)
        country = (country_name.text)
        data = json.loads(country)
        capital_list = data['body']
        if value in capital_list:
            return {"total_population": value}
        else:
            dispatcher.utter_template("utter_wrong_total_population", tracker)
            return {"total_population": None}
 
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



class ActionGetCapital(Action):
    def name(self):
        return "action_get_capital"
    def run(self, dispatcher, tracker, domain):
        url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries"
        country_name = requests.get(url)
        capitals = (country_name.text)
        data = json.loads(capitals)
        capital_list = data['body']
        cap_name = tracker.latest_message['entities'][0]['value']
        capital_list_lower = []
        for i in capital_list:
            i = i.lower()
            capital_list_lower.append(i)
        #capital_lowercase = map(lambda x:x.lower(),capital_list)
        i = 0
        for i in range(len(capital_list_lower)):
            if cap_name == capital_list_lower[i]:
                index_number = int(i)
                country_name = capital_list[index_number]            
            #country_name = cap_name.title()
                PARAMS = {"country":country_name}
                headers = {'content-type': 'application/json'}
                url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital"
                response = requests.post(url, data = json.dumps(PARAMS), headers=headers)
                data = response.json()
                fullcapitalname = data['body']['capital']
                dispatcher.utter_message("The {} is the capital of {}".format(fullcapitalname, country_name))

            if cap_name not in capital_list_lower:
                dispatcher.utter_message("Please re-enter the country name")
                break

        return []



class ActionGetPopulation(Action):
    def name(self):
        return "action_get_population"
    def run(self, dispatcher, tracker, domain):

        url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries"
        country_name = requests.get(url)
        population_country = (country_name.text)
        data = json.loads(population_country)
        capital_list = data['body']
        cap_name = tracker.latest_message['entities'][0]['value']
        population_list_lower = []
        for i in capital_list:
            i = i.lower()
            population_list_lower.append(i)
        i = 0
        for i in range(len(population_list_lower)):
            if cap_name == population_list_lower[i]:
                index_number = int(i)
                country_name = capital_list[index_number]            
                PARAMS = {"country":country_name}
                headers = {'content-type': 'application/json'}
                url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation"
                response = requests.post(url, data = json.dumps(PARAMS), headers=headers)
                data = response.json()
                totalpopulation = data['body']['population']
                dispatcher.utter_message("The total population of {} is {}".format(country_name, totalpopulation))
            if cap_name not in population_list_lower:
                dispatcher.utter_message("Please re-enter the country name")
                break
        return []




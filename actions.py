# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import urllib.request
import json
from rasa_core_sdk import Action
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
                                 ConversationPaused

logger = logging.getLogger(__name__)

class ActionGreet(Action):

	def name(self):
		return "action_greet"

	def run(self, dispatcher, tracker, domain):
		
		person_name = next(tracker.get_latest_entity_values('person_name'), None)
		dispatcher.utter_message("Nice to meet you "+ person_name+ " How can I help you ?")
		
		return [SlotSet("person_name", person_name)]

class ActionBye(Action):

	def name(self):
		return "action_bye"

	def run(self, dispatcher, tracker, domain):
		person_name = tracker.get_slot('person_name')
		dispatcher.utter_message("See you soon "+ person_name)
		
		return []

class ActionCheckTimeSlots(Action):

	def name(self):
		return "action_time_availablity"

	def run(self, dispatcher, tracker, domain):
		time = next(tracker.get_latest_entity_values('time'), None)
		# dispatcher.utter_message("Let me check for the avaliblity on "+ time)
		# contents = urllib.request.urlopen("http://example.com/foo/bar").read()
		# contents = requests.get("http://example.com/foo/bar")
		dispatcher.utter_message("Your Appointment is scheduled for "+ time)

		
		return [SlotSet("time", time)]




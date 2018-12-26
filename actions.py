# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
                                 ConversationPaused

logger = logging.getLogger(__name__)

class ActionStoreName(Action):
    """Stores the users name in a slot"""

    def name(self):
        return "action_store_name"

    def run(self, dispatcher, tracker, domain):

        person_name = next(tracker.get_latest_entity_values('name'), None)

        # if no name was extracted, use the whole user utterance
        # in future this will be stored in a `name_unconfirmed` slot and the
        # user will be asked to confirm their name
        if not person_name:
            person_name = tracker.latest_message.get('text')

        return [SlotSet('person_name', person_name)]

class AcionStorePatientType(Action):
	""" Stores the patient type - New patient: Yes or No """

	def name(self):
		return "action_store_patient_type"

	def run(self, dispatcher, tracker, domain):

		patient_type = next(tracker.get_latest_entity_values('patient_type'), None)

		if not patient_type:
			person_name = tracker.latest_message.get('text')
			if person_name.lower() == 'yes':
				return [SlotSet('new_patient', True)]
			else:
				return [SlotSet('new_patient', False)]

class ActionStoreEmail(Action):
	"""Stores the email in a slot"""

	def name(self):
		return "action_store_email"

	def run(self, dispatcher, tracker, domain):
		email = next(tracker.get_latest_entity_values('email'), None)

        # if no email entity was recognised, prompt the user to enter a valid
        # email and go back a turn in the conversation to ensure future
        # predictions aren't affected
		if not email:
			email = tracker.latest_message.get('text')
			# dispatcher.utter_message("We need your email, "
   #                                   "please enter a valid one.")
			# # return [UserUtteranceReverted()]

		return [SlotSet('email', email)]

class ActionStoreDate(Action):
	""" Store the date time """
	def name(self):
		return "action_store_date"
	
	def run(self, dispatcher, tracker, domain):
		date = next(tracker.get_latest_entity_values('date'), None)
		
		if not date:
			date = tracker.latest_message.get('text')
			# dispatcher.utter_message("please enter a valid date time.")
			# return [UserUtteranceReverted()]
		return [SlotSet('date', date)]

class action_book_appointment(Action):
	""" Booking appt """
	def name(self):
		return "action_book_appointment"

	def run(self, dispatcher, tracker, domain):
		print("its worked!!!!")

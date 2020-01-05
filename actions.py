from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import Email
import zomatopy
import json
import requests
import ast
from nltk.metrics.distance import edit_distance
from validate_email import validate_email

def do_search(dispatcher, tracker, domain, resultCount=5):
	config={ "user_key":"00ef26b0bb975bcdae09c8bc6d0cf016"}
	zomato = zomatopy.initialize_app(config)
	loc = tracker.get_slot('location')
	cuisine = tracker.get_slot('cuisine')
	budget = tracker.get_slot('budget')
	budget_dict = {'lesser than 250':0, '250 to 500':1, '500 to 1000': 2, '1000 to 1500': 3, '1500 to 2500': 4, 'more than 2500': 5}
	budget = budget_dict.get(budget)
	location_detail=zomato.get_location(loc, 1)
	d1 = json.loads(location_detail)
	lat=d1["location_suggestions"][0]["latitude"]
	lon=d1["location_suggestions"][0]["longitude"]
	if cuisine == None:
		cuisine_id = '1,25,50,55,73,85'
	else:
		cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85}
		cuisine_id = cuisines_dict.get(cuisine)	
	if cuisine_id == None:
		return {'results_found': 0}
	results=zomato.restaurant_search("", lat, lon, str(cuisine_id),budget, resultCount)
	d = json.loads(results)
	return d

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		d = do_search(dispatcher, tracker, domain, 5)
		response=""
		if d['results_found'] == 0:
		    response= "No results found, try with some other criteria"
		else:
		    count= 1
		    for restaurant in d['restaurants']:
		        response=response+ "Showing you top rated restaurants:" + "\n"
		        response=response+ str(count) + ") "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n"
		        count = count + 1
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class ActionCheckLocation(Action):
	def name(self):
		return 'action_checklocation'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		servingAreas = ["Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Pune", "Agra", "Ajmer", "Aligarh", "Allahabad", "Amravati", "Amritsar", "Asansol", "Aurangabad", "Bareilly", "Belgaum", "Bhavnagar", "Bhiwandi", "Bhopal", "Bhubaneswar", "Bikaner", "BokaroSteelCity", "Chandigarh", "Coimbatore", "Cuttack", "Dehradun", "Dhanbad", "Durg-BhilaiNagar", "Durgapur", "Erode", "Faridabad", "Firozabad", "Ghaziabad", "Gorakhpur", "Gulbarga", "Guntur", "Gurgaon", "Guwahati‚Gwalior", "Hubli-Dharwad", "Indore", "Jabalpur", "Jaipur", "Jalandhar", "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Kannur", "Kanpur", "Kakinada", "Kochi", "Kottayam", "Kolhapur", "Kollam", "Kota", "Kozhikode", "Kurnool", "Lucknow", "Ludhiana", "Madurai", "Malappuram", "Mathura", "Goa", "Mangalore", "Meerut", "Moradabad", "Mysore", "Nagpur", "Nanded", "Nashik", "Nellore", "Noida", "Palakkad", "Patna", "Pondicherry", "Raipur", "Rajkot", "Rajahmundry", "Ranchi", "Rourkela", "Salem", "Sangli", "Siliguri", "Solapur", "Srinagar", "Sultanpur", "Surat", "Thiruvananthapuram", "Thrissur", "Tiruchirappalli", "Tirunelveli", "Tiruppur", "Ujjain", "Bijapur", "Vadodara", "Varanasi", "Vasai-VirarCity", "Vijayawada", "Visakhapatnam", "Warangal"]
		servingAreas = [x.lower() for x in servingAreas]
		response=""
		if (loc != None) and (loc.lower() in servingAreas):
			return [SlotSet('location',loc)]
		elif loc != None:
			loc = loc.lower()
			correct_locs = [x for x in servingAreas if edit_distance(x, loc) <= 2]
			if len(correct_locs) == 0:
			    response= " Sorry, we don’t operate in this city. Can you please specify some other location"
			    dispatcher.utter_message(response)
			    return [SlotSet('location',None)]
			else:
			    return [SlotSet('location',correct_locs[0])]

class ActionMailCommunication(Action):
	def name(self):
		return 'action_mail'
		
	def run(self, dispatcher, tracker, domain):
		mail_confirmation = tracker.get_slot('mailConfirm')
		mailId = tracker.get_slot('emailId')
		loc = tracker.get_slot('location')
		if mail_confirmation.lower() == "yes":
			if mailId == None or mailId == "":
			    mailId = input("To what email id should I send it to? \n")
			is_valid = validate_email(mailId)
			if is_valid == False:
			    dispatcher.utter_message("Invalid email id")
			    return [SlotSet('location',loc)]
			d = do_search(dispatcher, tracker, domain, 10)
			response=""
			if d['results_found'] == 0:
			    response= "no results found"
			else:
			    response = response+ "Found below restaurants" +"\n"
			    count = 1
			    for restaurant in d['restaurants']:
			        response = response + str(count) + ") " + restaurant['restaurant']['name'] + "\n"
			        response = response + "   Address: " + restaurant['restaurant']['location']['address'] + "\n"
			        response = response + "   Average budget for two people: " + str(restaurant['restaurant']['average_cost_for_two']) + "\n"
			        response = response + "   Rating: " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n"
			        count = count + 1
			Email.send_mail(mailId, response)
			response= "Sent"
		else:
			response= ""
		
		dispatcher.utter_message(""+response)
		return [SlotSet('location',loc)]
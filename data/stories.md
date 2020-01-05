## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - utter_goodbye

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
* affirm
    - utter_goodbye
    - export

## Generated Story -3547874362140095856
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - export

## Generated Story 3566151195271605949
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "250 to 500"}
    - slot{"budget": "250 to 500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 3852501782346226178
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "hyderabad", "budget": "250 to 500"}
    - slot{"budget": "250 to 500"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "hyderabad"}
    - action_checklocation
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "hyderabad"}
* goodbye
    - utter_goodbye
    - export

## Generated Story -2320428114471203414
* greet
    - utter_greet
* restaurant_search{"budget": "250 to 500"}
    - slot{"budget": "250 to 500"}
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_checklocation
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"location": "agra"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "agra"}
    - utter_goodbye
    - export

## Generated Story -6833007476312852310
* greet
    - utter_greet
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_checklocation
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "250 to 500"}
    - slot{"budget": "250 to 500"}
    - action_restaurant
    - slot{"location": "agra"}
    - utter_goodbye
    - export

## Generated Story 4572191921972701572
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story -1979992464519951776
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_checklocation
    - slot{"location": "kolkata"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "250 to 500"}
    - slot{"budget": "250 to 500"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "kolkata"}
    - utter_goodbye
    - export

## Generated Story -9213377110153283843
* greet
    - utter_greet
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_checklocation
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "kolkata"}
    - utter_goodbye
    - export

## Generated Story 1810903124273436502
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_checklocation
    - slot{"location": "chandigarh"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "1000 to 1500"}
    - slot{"budget": "1000 to 1500"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "chandigarh"}
    - utter_goodbye
    - export

## Generated Story -8079565591405381785
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "1000 to 1500"}
    - slot{"budget": "1000 to 1500"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_checklocation
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_checklocation
    - slot{"location": "mumbai"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_goodbye
    - export

## Generated Story -4254770756471910935
* restaurant_search{"cuisine": "chinese", "budget": "1000 to 1500"}
    - slot{"budget": "1000 to 1500"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 5442179104234995245
* greet
    - utter_greet
* restaurant_search{"budget": "of 2000"}
    - slot{"budget": "of 2000"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_checklocation
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "pune"}
    - utter_goodbye
    - export

## Generated Story 2557289548091097396
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_checklocation
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "1500 to 2000"}
    - slot{"budget": "1500 to 2000"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes", "emailId": "bhathaluri.pooja@gmail.com"}
    - slot{"emailId": "bhathaluri.pooja@gmail.com"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "kolkata"}
    - utter_goodbye
    - export

## Generated Story -1247715490417810247
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "1000 to 1500"}
    - slot{"budget": "1000 to 1500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 1982855318683974445
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - utter_goodbye
    - export

## Generated Story -772720745360811409
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "250 to 500"}
    - slot{"budget": "250 to 500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes", "emailId": "manikanta1315@gmail.com"}
    - slot{"emailId": "manikanta1315@gmail.com"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 3578852052238077394
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes", "emailId": "manikanta1315@gmail.com"}
    - slot{"emailId": "manikanta1315@gmail.com"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 1789564220328864090
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "pune", "budget": "1500 to 2500"}
    - slot{"budget": "1500 to 2500"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - action_checklocation
    - slot{"location": "pune"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "pune"}
    - utter_goodbye
    - export

## Generated Story -1910255214885805361
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bangalore", "budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story -330869304446353580
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "pune", "budget": "1500 to 2500"}
    - slot{"budget": "1500 to 2500"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - action_checklocation
    - slot{"location": "pune"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "pune"}
    - utter_goodbye
    - export

## Generated Story -344389415956654504
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_checklocation
    - slot{"location": "chandigarh"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "lesser than 250"}
    - slot{"budget": "lesser than 250"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_checklocation
    - slot{"location": "Mumbai"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - utter_goodbye
    - export

## Generated Story 4195358992858872157
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_checklocation
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_goodbye
    - export

## Generated Story 2811497602643006167
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 3676623928086668247
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_checklocation
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_checklocation
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes", "emailId": "bhathaluri.pooja@gmail.com"}
    - slot{"emailId": "bhathaluri.pooja@gmail.com"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "mumbai"}
    - utter_goodbye
    - export

## Generated Story -4940373858538191945
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "1500 to 2500"}
    - slot{"budget": "1500 to 2500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story -1821516694415638187
* greet
    - utter_greet
* restaurant_search{"location": "marathalli"}
    - slot{"location": "marathalli"}
    - action_checklocation
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "1000 to 1500"}
    - slot{"budget": "1000 to 1500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 6214532815517614899
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_checklocation
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "1000 to 1500"}
    - slot{"budget": "1000 to 1500"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story -1117572117355493951
* greet
    - utter_greet
* restaurant_search{"location": "marathalli"}
    - slot{"location": "marathalli"}
    - action_checklocation
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "1000 to 1500"}
    - slot{"budget": "1000 to 1500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story -1053371842676098735
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 6240557907722571851
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search
    - action_checklocation
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes", "emailId": "bhathaluri.pooja@gmail.com"}
    - slot{"emailId": "bhathaluri.pooja@gmail.com"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story 1264271252201552080
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - action_checklocation
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_checklocation
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story -6393917800406638958
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes", "emailId": "manikanta1315@gmail.com"}
    - slot{"emailId": "manikanta1315@gmail.com"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story -8926324837027276819
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_checklocation
    - slot{"location": null}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "allahabad"}
    - utter_goodbye
    - export

## Generated Story -2624835010486004831
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "tadepalligudem"}
    - slot{"location": "tadepalligudem"}
    - action_checklocation
    - slot{"location": null}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "250 to 500"}
    - slot{"budget": "250 to 500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes", "emailId": "manikanta1315@gmail.com"}
    - slot{"emailId": "manikanta1315@gmail.com"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "bangalore"}
    - utter_goodbye
    - export

## Generated Story -2054397080254458359
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_checklocation
    - slot{"location": "chandigarh"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "chandigarh"}
    - utter_goodbye
    - export

## Generated Story -5782099504115785093
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_checklocation
    - slot{"location": null}
* restaurant_search
    - action_checklocation
    - slot{"location": null}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_checklocation
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetRange
* restaurant_search{"budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "yes"}
    - slot{"mailConfirm": "yes"}
    - action_mail
    - slot{"location": "mumbai"}
    - utter_goodbye
    - export

## Generated Story 6696538308344303414
* restaurant_search{"cuisine": "chinese", "location": "pune", "budget": "500 to 1000"}
    - slot{"budget": "500 to 1000"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - action_checklocation
    - slot{"location": "pune"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_mailconfirmation
* email_restaurantsearch{"mailConfirm": "no"}
    - slot{"mailConfirm": "no"}
    - action_mail
    - slot{"location": "pune"}
    - utter_goodbye
    - export


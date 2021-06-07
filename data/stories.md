## happy path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye


## capital name
* check_capital
    - capital_form
    - form{"name": "capital_form"}
    - form{"name": null}
    - utter_capital_ans
    - action_restart

## total population
* check_population
    - population_form
    - form{"name": "population_form"}
    - form{"name": null}
    - utter_population_ans
    - action_restart

## country capital
* country_capital
    - action_get_capital



## country population
* country_population
    - action_get_population




## generated story
* check_capital
    - action_get_capital
    - slot{"cap_name":"India"}

    
* check_population
    - action_get_population
    - slot{"cap_name":"USA"}

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

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

## India capital
* India_capital
    - action_get_capital
    - utter_capital_ans

## USA capital
* USA_capital
    - action_get_capital
    - utter_capital_ans

## Greece capital
* Greece_capital
    - action_get_capital
    - utter_capital_ans

## Sweden capital
* Sweden_capital
    - action_get_capital
    - utter_capital_ans

## Australia capital
* Australia_capital
    - action_get_capital
    - utter_capital_ans

## Finland capital
* Finland_capital
    - action_get_capital
    - utter_capital_ans

## Japan capital
* Japan_capital
    - action_get_capital
    - utter_capital_ans

## Russia capital
* Russia_capital
    - action_get_capital
    - utter_capital_ans



## India population
* India_population
    - action_get_population
    - utter_population_ans


## USA population
* USA_population
    - action_get_population
    - utter_population_ans

## Greece population
* Greece_population
    - action_get_population
    - utter_population_ans

## Sweden population
* Sweden_population
    - action_get_population
    - utter_population_ans

## Australia population
* Australia_population
    - action_get_population
    - utter_population_ans

## Finland population
* Finland_population
    - action_get_population
    - utter_population_ans

## Japan population
* Japan_population
    - action_get_population
    - utter_population_ans

## Russia population
* Russia_population
    - action_get_population
    - utter_population_ans



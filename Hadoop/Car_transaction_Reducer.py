#!/usr/bin/python

# Reducer for session generation.
# Here we assemble user sessions

import sys
from collections import defaultdict
from itertools import groupby
from operator import attrgetter


def read_key_value(file):
    for line in file:
        # split the line into components, before and after the tab
        yield line.strip().split('\t', 1)
def classify(events):
    #Classify users based on their event_action and event_target
    is_clicker = None
    is_shower = None
    is_visitor = None
    for event in events:
        if event['event_target'] == 'contact form':
            return 'submitter'
        if event['event_action'] == 'click':
            is_clicker = True
        if event['event_action'] == 'show' or event['event_action'] == 'display':
            is_shower = True
        if event['event_action'] == 'visit':
            is_visitor = True
        if is_clicker:
            return 'clicker'
        elif is_shower:
            return 'shower'
        elif is_visitor:
            return 'visitor'
        return 'other'

def printing_output(user_id, event_list):
    #see if the current item is a user
    event_list, car_info_dict = formatting_output(event_list,['mileage','condition','make','model','price'])
    #sort event_list here
    event_list.sort(key = lambda x: x['timestamp'],reverse = False)
    print '{}:{}\t{}\t{}'.format(user_id,classify(event_list), event_list,car_info_dict)

def formatting_output(event_list, car_list):
    #returns event_list and car_info_dict by mapping vin number to key of car_info_dict
    car_info_dict = {}
    new_event_list = []
    for event in event_list:
        if event['vin'] not in car_info_dict.keys():
            car_info_dict[event['vin']] = {attribute: event[attribute] for attribute in car_list}
            event = cleaning_event(event,car_list)
            new_event_list.append(event)
    return new_event_list, car_info_dict

def cleaning_event(event,car_list):
    #Removes attributes from event and append it to new_event_list to avoid duplicates
    for attribute in car_list:
        event.pop(attribute,None)
    return event

def main():
    current_user_id = None
    event_list = []

    for user_id, event_string in read_key_value(sys.stdin):
        # eval() converts a data structure described on a string
        # into that internal data structure (for example, a dictionary).
        event = eval(event_string)

        # Assemble
        if user_id == current_user_id:
            event_list.append(event)
            continue
        else:
            if current_user_id:
                printing_output(current_user_id,event_list)
            current_user_id = user_id
            event_list = [event]

    if user_id == current_user_id:
        printing_output(current_user_id, event_list)

if __name__ == "__main__":
    main()

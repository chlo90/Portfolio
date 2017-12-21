#!/usr/bin/python

# Mapper for session generation.
# Here we examine event log entries of car sales 

import sys

name_list = ['user_id', 'event', 'timestamp', 'vin', 'condition', 'year', 'make', 'model', 'price', 'mileage' ]

def read_input(file):
    for line in file:
        # split the line into individual fields (fields are delimited by tab).
        yield line.strip().split('\t')

def digest_log_entry(field_value_list):
    field_value_dict = {}
    #Split the event by event_action and event_target
    for i in range(len(name_list)):
        if name_list[i] == 'event':
            act = field_value_list[i].split(' ')
            field_value_dict['event_action'] = act[0]
            field_value_dict['event_target'] = act[1]
        #Assign the log entry into field_value_dict with keys from name_list
        else:
            field_value_dict[name_list[i]] = field_value_list[i]
    return field_value_dict

def main():
    # input comes from STDIN (standard input)
    # data is the generator that produces individual inputs
    data = read_input(sys.stdin)

    # For each log entry, digest all the fields,
    # output the user_id as the key,
    # output the digested log entry (a dictionary) as the value
    for log_entry in data:
        digested_log_entry = digest_log_entry(log_entry)
	#eliminate redudnant user_id entry in mapper output
	user_id = digested_log_entry['user_id']
	digested_log_entry.pop('user_id',None)
    #Gives user_id and digested log entry as output for reducer
        print '%s\t%s'% (user_id, digested_log_entry)


if __name__ == "__main__":
    main()

#!/usr/bin/python


import sys
import re

curr_session_count = 0
curr_click_count = 0
curr_contact_form = 0
curr_srp_count = 0
curr_vrp_count = 0
last_vin=None


for line in sys.stdin: #read the input from sys.stdin
    line = line.lower().strip()
    vin, counts = line.split(':')
    count = re.findall(r'\d+', counts)

    session_count, click_count, contact_form, srp, vrp = count #split count
    # print srp
    try:
        session_count = int(session_count) #Throw valueerror if count is not int
        click_count = int(click_count)
        contact_form = int(contact_form)
        srp = int(srp)
        vrp = int(vrp)

    except ValueError:
        continue

    if last_vin == vin:
        curr_session_count += session_count
        curr_click_count += click_count
        curr_contact_form += contact_form
        curr_srp_count += srp
        curr_vrp_count += vrp

    else:
        if last_vin:
            if curr_session_count != 0:
                last_vin = last_vin[1:]
                # print  "\t".join(str(v) for v in [last_vin, curr_session_count, curr_click_count, curr_contact_form, curr_srp_count, curr_vrp_count, "}"])
                print last_vin, "\t", [curr_session_count, curr_click_count, curr_contact_form, curr_srp_count, curr_vrp_count]
        curr_session_count = session_count
        curr_click_count = click_count
        curr_contact_form = contact_form
        curr_srp_count = srp
        curr_vrp_count = vrp
        last_vin = vin
if last_vin == vin:
    if curr_session_count != 0:
        vin = vin[1:]
        # print "\t".join(str(v) for v in [vin, curr_session_count, curr_click_count, curr_contact_form, curr_srp_count, curr_vrp_count, "}"])
        print vin, "\t", [curr_session_count, curr_click_count, curr_contact_form, curr_srp_count, curr_vrp_count]

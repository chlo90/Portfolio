#!/usr/bin/python

# Read session

import sys
def main():
    for line in sys.stdin:

        try:
            value = line.strip().split('\t')
            user_id_string, event_list_string, vin_dict_string = value
            user_id, session_type = user_id_string.split(':')
            event_list = eval(event_list_string)
            vin_dict = eval(vin_dict_string)
            vin_list = []
            for i in vin_dict:
                vin_list.append(i)

            event_dict = {}
            session_count = 0
            click_count = 0
            contact_form = 0

            for event in event_list:

                if event['event_action'] == 'click':
                    click_count = 1
                if event['event_target'] == 'contact form':
                    contact_form = 1
                else:
                    contact_form = 0
                session_count = 1
            for i in vin_list:
                for k, v in event.items():
                    if k == 'vin':
                        event_dict[v] = [session_count, click_count, contact_form, 0, 0]
                print event_dict


        except:
            imp_dict = {}
            value = line.strip().split(',')
            vin, imp, count = value

            srp_count = 0
            vdp_count = 0
            if imp == 'SRP':
                srp_count = count
            elif imp == 'VDP':
                vdp_count = count

            imp_dict[vin] = [0, 0,0, srp_count, vdp_count]
            print imp_dict

if __name__ == "__main__":
    main()

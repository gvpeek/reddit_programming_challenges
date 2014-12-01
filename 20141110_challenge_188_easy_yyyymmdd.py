#!/usr/bin/env python

import os
import sys
from time import strptime, strftime

# Possible formats to be corrected
# yyyy-mm-dd
# mm/dd/yy
# mm#yy#dd
# dd*mm*yyyy
# (month word) dd, yy
# (month word) dd, yyyy

execution_dir = sys.path[0]

correct_format = '%Y-%m-%d'

with open(os.path.join(execution_dir, '20141110_challenge_188_easy_yyyymmdd_converted_dates.txt'), 'wb') as corrected_date_entries:
    with open(os.path.join(execution_dir, '20141110_challenge_188_easy_yyyymmdd.txt'), 'rb') as date_entries:
        for entry in date_entries:
            entry = entry.strip()
            if '-' in entry:
                corrected_entry = entry
            elif '/' in entry:
                corrected_entry = strftime(correct_format, strptime(entry,'%m/%d/%y'))
            elif '#' in entry:
                corrected_entry = strftime(correct_format, strptime(entry,'%m#%y#%d'))
            elif '*' in entry:
                corrected_entry = strftime(correct_format, strptime(entry,'%d*%m*%Y'))
            else:
                try:
                    corrected_entry = strftime(correct_format, strptime(entry,'%b %d, %y'))
                except:
                    corrected_entry = strftime(correct_format, strptime(entry,'%b %d, %Y'))

            if corrected_entry[0:4] > '2049':
                corrected_entry = '19' + corrected_entry[2:]
            
            corrected_date_entries.write(corrected_entry + '\n')
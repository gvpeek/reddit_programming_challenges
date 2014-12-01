#!/usr/bin/env python

import os
import sys

from operator import attrgetter
from datetime import datetime, timedelta

execution_dir = sys.path[0]

# Sample entry
# 11-6-2014: 07:51 AM to 08:25 AM -- personal appointment

class Event():
    def __init__(self, date, start_time, end_time, description):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.begin = datetime.strptime(date + start_time, '%m-%d-%Y%I:%M %p')
        self.end = datetime.strptime(date + end_time, '%m-%d-%Y%I:%M %p')
        self.duration = self.end - self.begin

events = []
schedule =[]
categories = {}

with open(os.path.join(execution_dir, '20141105_challenge_187_intermediate_finding_time_input.txt')) as notes:
    for post_it in notes:
        date, remainder = post_it.split(':', 1)
        times, desc = remainder.split(' -- ')
        begin_time, end_time = times.split(' to ')
        events.append(Event(date.strip(), begin_time.strip(), end_time.strip(), desc.strip()))
        
events.sort(key=attrgetter('begin'))
proc_date = None
proc_end = None
proc_end_time = None
longest_gap = timedelta(0,0)
total_occupied_time = timedelta(0,0)

for event in events:
    if proc_date != event.date:
        if proc_date:
            schedule.insert(hold_index, Event(proc_date, hold_start_time, hold_end_time, 'reddit'))
        proc_date = event.date
        proc_end = event.end
        proc_end_time = event.end_time
        longest_gap = timedelta(0,0)
    else:
        gap = event.begin - proc_end
        if gap > longest_gap:
            longest_gap = gap
            hold_start_time = proc_end_time
            hold_end_time = event.start_time
            hold_index = len(schedule)
        proc_end = event.end
        proc_end_time = event.end_time
        
    schedule.append(event)

# catch the last reddit
schedule.insert(hold_index, Event(proc_date, hold_start_time, hold_end_time, 'reddit'))

for event in schedule:
    if event.description in categories:
        categories[event.description] += event.duration
    else:
        categories[event.description] = event.duration
    
    total_occupied_time += event.duration
        
    print event.date, event.start_time, event.end_time, event.description, event.duration 

print
print 'Total Occupied Time', total_occupied_time    
print

for category, total_time in categories.iteritems():
    pct_of_total_time = total_time.total_seconds() / total_occupied_time.total_seconds()
    print category, total_time, '% of Total', '{:.2%}'.format(pct_of_total_time)
    
        

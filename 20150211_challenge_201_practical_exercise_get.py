import time

from heapq import heappush, heappop
from collections import OrderedDict
from random import choice, randint
from string import ascii_letters

class DualPriorityQueueHeap():
    def __init__(self):
        self.strings = OrderedDict()
        self.next_index=-1
        
    def _get_next_index(self):
        self.next_index += 1
        return self.next_index
        
    def enqueue(self, val_a, val_b, value):
        '''This method accepts three parameters - a string, priority value A,
           and priority value B, where the priority values are real numbers 
           (see above). The string is inserted into the priority queue with the
           given priority values A and B'''
        ix = self._get_next_index()
        self.strings[ix] = ((val_a, val_b, value))

    def _dequeue(self, index):
        ''' Adds entries from enqueued strings to priority queue based on 
            provided index.
        '''
        heap = []
        for key, value in self.strings.iteritems():
            heappush(heap, (value[index], key))
        item = heappop(heap)
        return self.strings.pop(item[1])[2]        
        
    def dequeue_a(self):
        '''This method removes and returns the string from the priority queue 
           with the highest priority A value. If two entries have the same A 
           priority, return whichever was enqueued first.'''
        return self._dequeue(0)
        
    def dequeue_b(self):
        '''This method removes and returns the string from the priority queue 
           with the highest priority B value. If two entries have the same B 
           priority, return whichever was enqueued first.'''
        return self._dequeue(1)
        
    def count(self):
        '''This method returns the number of strings in the queue.'''
        return len(self.strings)
        
    def clear(self):
        '''This removes all entries from the priority queue.'''
        self.strings.clear()
        
    def dequeue_first(self):
        '''This removes and returns the string from the priority queue that 
           was enqueued first, ignoring priority.'''
        return self.strings.popitem(last=False)[1][2]

class DualPriorityQueueODPopLast():
    def __init__(self):
        self.strings = OrderedDict()
        self.next_index=-1
        
    def _get_next_index(self):
        self.next_index += 1
        return self.next_index
        
    def enqueue(self, val_a, val_b, value):
        '''This method accepts three parameters - a string, priority value A,
           and priority value B, where the priority values are real numbers 
           (see above). The string is inserted into the priority queue with the
           given priority values A and B'''
        ix = self._get_next_index()
        self.strings[ix] = ((val_a, val_b, value))

    def _dequeue(self, index):
        ''' Adds entries from enqueued strings to priority queue based on 
            provided index.
        '''
        item = OrderedDict(sorted(self.strings.items(), key=lambda t: (t[1][index], self.strings.keys().index(t[0])), reverse=True)).popitem()
        return self.strings.pop(item[0])[2]
        
    def dequeue_a(self):
        '''This method removes and returns the string from the priority queue 
           with the highest priority A value. If two entries have the same A 
           priority, return whichever was enqueued first.'''
        return self._dequeue(0)
        
    def dequeue_b(self):
        '''This method removes and returns the string from the priority queue 
           with the highest priority B value. If two entries have the same B 
           priority, return whichever was enqueued first.'''
        return self._dequeue(1)
        
    def count(self):
        '''This method returns the number of strings in the queue.'''
        return len(self.strings)
        
    def clear(self):
        '''This removes all entries from the priority queue.'''
        self.strings.clear()
        
    def dequeue_first(self):
        '''This removes and returns the string from the priority queue that 
           was enqueued first, ignoring priority.'''
        return self.strings.popitem(last=False)[1][2]

class DualPriorityQueueODPopFirst():
    def __init__(self):
        self.strings = OrderedDict()
        self.next_index=-1
        
    def _get_next_index(self):
        self.next_index += 1
        return self.next_index
        
    def enqueue(self, val_a, val_b, value):
        '''This method accepts three parameters - a string, priority value A,
           and priority value B, where the priority values are real numbers 
           (see above). The string is inserted into the priority queue with the
           given priority values A and B'''
        ix = self._get_next_index()
        self.strings[ix] = ((val_a, val_b, value))

    def _dequeue(self, index):
        ''' Adds entries from enqueued strings to priority queue based on 
            provided index.
        '''
        item = OrderedDict(sorted(self.strings.items(), key=lambda t: t[1][index])).popitem(last=False)
        return self.strings.pop(item[0])[2]
        
    def dequeue_a(self):
        '''This method removes and returns the string from the priority queue 
           with the highest priority A value. If two entries have the same A 
           priority, return whichever was enqueued first.'''
        return self._dequeue(0)
        
    def dequeue_b(self):
        '''This method removes and returns the string from the priority queue 
           with the highest priority B value. If two entries have the same B 
           priority, return whichever was enqueued first.'''
        return self._dequeue(1)
        
    def count(self):
        '''This method returns the number of strings in the queue.'''
        return len(self.strings)
        
    def clear(self):
        '''This removes all entries from the priority queue.'''
        self.strings.clear()
        
    def dequeue_first(self):
        '''This removes and returns the string from the priority queue that 
           was enqueued first, ignoring priority.'''
        return self.strings.popitem(last=False)[1][2]

nbr_test_cases = 1000
nbr_dequeue_cases = nbr_test_cases / 2
print 'Generating test cases...'
test_cases=[(randint(1,100000),
             randint(1,100000),
             ''.join([choice(ascii_letters) for x in xrange(8)])) for x in xrange(nbr_test_cases)]

print 'Running tests...'
for implementation in [DualPriorityQueueHeap, DualPriorityQueueODPopLast, DualPriorityQueueODPopFirst]:
    print implementation
    dpq = implementation()
    start_time = time.time()
    for case in test_cases:
        dpq.enqueue(*case)
    elapsed_time = time.time() - start_time
    print 'Enqueued list in {0} seconds.'.format(elapsed_time)
    
    start_time = time.time()
    for x in xrange(nbr_dequeue_cases):
        dpq.dequeue_a()
        dpq.dequeue_b()
    elapsed_time = time.time() - start_time
    print 'Dequeued {0} items in {1} seconds.'.format(nbr_dequeue_cases * 2, elapsed_time)
    print
    
    # # Rudimentary Checks
    # dpq = implementation()
    # dpq.enqueue(2,3,'Hello')
    # dpq.enqueue(1,2,'Goodbye')
    # dpq.enqueue(3,1,'What?')
    # dpq.enqueue(1,5,'Giggles')
    # dpq.enqueue(4,5,'Sniggles')
    # print dpq.count()
    # print dpq.dequeue_a()
    # print dpq.count()
    # dpq.enqueue(1,2,'Goodbye')
    # print dpq.dequeue_b()
    # print dpq.dequeue_first()
    # print dpq.count()
    # dpq.clear()
    # print dpq.count()
    
    
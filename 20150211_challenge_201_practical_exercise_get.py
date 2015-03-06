from heapq import heappush, heappop

from collections import OrderedDict

class DualPriorityQueue():
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

# Rudimentary Checks
dpq = DualPriorityQueue()
dpq.enqueue(2,3,'Hello')
dpq.enqueue(1,2,'Goodbye')
dpq.enqueue(3,1,'What?')
dpq.enqueue(1,5,'Giggles')
dpq.enqueue(4,5,'Sniggles')
print dpq.count()
print dpq.dequeue_a()
print dpq.count()
dpq.enqueue(1,2,'Goodbye')
print dpq.dequeue_b()
print dpq.dequeue_first()
print dpq.count()
dpq.clear()
print dpq.count()


class DualPriorityQueue2():
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
        return OrderedDict(sorted(self.strings.items(), key=lambda t: -1 * t[1][index])).popitem()[1][2]       
        
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

# Rudimentary Checks
dpq = DualPriorityQueue2()
dpq.enqueue(2,3,'Hello')
dpq.enqueue(1,2,'Goodbye')
dpq.enqueue(3,1,'What?')
dpq.enqueue(1,5,'Giggles')
dpq.enqueue(4,5,'Sniggles')
print dpq.count()
print dpq.dequeue_a()
print dpq.count()
dpq.enqueue(1,2,'Goodbye')
print dpq.dequeue_b()
print dpq.dequeue_first()
print dpq.count()
dpq.clear()
print dpq.count()
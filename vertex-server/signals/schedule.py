import operator
import threading
import time

from .config import *

global thread
thread = None

def start():
    """Start the schedule thread.
    """
    global thread
    if thread: return

    thread = ScheduleThread()
    thread.start()

    time.sleep(3)
    thread.add_event({'a':'thing'})
    time.sleep(2)
    thread.add_event({'a':'thing 2', 'priority':2})
    time.sleep(2)
    thread.add_event({'a':'thing 2b', 'priority':2})
    time.sleep(2)
    thread.add_event({'a':'thing 2c', 'priority':2}, True)
    time.sleep(2)
    thread.add_event({'a':'thing 1', 'priority':1})
    time.sleep(2)
    thread.add_event({'a':'thing 3', 'priority':3})
    time.sleep(2)

class ScheduleThread(threading.Thread):
    def run(self):
        # dictionary to hold bulb lit status
        self.light_status = {k: {'lit':False} for k in light_pins}

        # generate mapping from mapping_labels
        self.mapping = {
            road: {
                direction: [
                    [self.light_status[label] if label else {} for label in label_list]
                    for label_list in mapping_labels[road][direction]
                ] for direction in mapping_labels[road]
            } for road in mapping_labels
        }

        self.events = []

        while True:
            print('events\n', self.events)
            time.sleep(1)

    def add_event(self, event, allow_overwrite=False):
        if not 'priority' in event:
            print('ERROR: No priority for event:\n{}'.format(event))
            return 1

        # get existing event with same priority if exists
        existing = next((e for e in self.events if e['priority'] == event['priority']), None)
        if existing:
            if allow_overwrite:
                print('WARN: Overwriting event with priority {}'.format(existing['priority']))
                self.events.remove(existing)
            else:
                print('ERROR: Entry already exists for priority {}'.format(existing['priority']))
                return 1

        self.events.append(event)
        self.sort_events()

    def sort_events(self):
        self.events.sort(key=operator.itemgetter('priority'), reverse=True)

'''Some code to help test Paradox alarm interface.'''

import logging
import time
from pyparadox_alarm.alarm_panel import ParadoxAlarmPanel
#from paradox import *
#import paradox

_LOGGER = logging.getLogger(__name__)

loggingconfig = {'level': 'DEBUG',
    'format': '%(asctime)s %(levelname)s <%(name)s %(module)s %(funcName)s> %(message)s',
    'datefmt': '%a, %d %b %Y %H:%M:%S'}

logging.basicConfig(**loggingconfig)

_LOGGER.info('Start')
panel = ParadoxAlarmPanel()

_LOGGER.info('Start test:')
_LOGGER.info('Alarm State before:')
#print(panel.alarm_state['zone'])
print(panel.alarm_state())
panel.start()
time.sleep(80) #Wait because we're using threading
_LOGGER.info('Alarm State after:')
print(panel.alarm_state())
for _ in range(3):
    request = input("Supply a request:")
    panel.submit_request(request)

_LOGGER.info('Disconnecting...')
panel.stop()
_LOGGER.info('Waiting for all to stop:')
time.sleep(10)
_LOGGER.info('End test:')

import os
import sys

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/dev/Self_Service_Project/selfservice')
sys.path.append('/home/dev/Self_Service_Project/selfservice/selfservice')
#sys.path.append('/home/dev/ssp/wavamezz')
#sys.path.append('/home/dev/ssp/msp')
#sys.path.append('/home/dev/ssp/dashboard')
os.environ['DJANGO_SETTINGS_MODULE'] = 'selfservice.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()




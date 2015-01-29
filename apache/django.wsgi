import os
import sys
# Add the app's directory to the PYTHONPATH

sys.path.append('/home/dev/Workspace/sspEnvFolder/self_service_platform/SelfService')
sys.path.append('/home/dev/Workspace/sspEnvFolder/self_service_platform/SelfService/selfservice')
os.environ['DJANGO_SETTINGS_MODULE'] = 'selfservice.settings'

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

with open('/home/dev/Workspace/sspEnvFolder/self_service_platform/SelfService/apache/out.txt','a') as writer:
    writer.write('sys path is :\n')
    for l in sys.path:
        writer.write(l+'\n')

    writer.write('latest result is here\n')
writer.close()



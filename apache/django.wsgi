import os
import sys

# Add the app's directory to the PYTHONPATH
<<<<<<< HEAD
sys.path.append('/home/dev/SelfService')
sys.path.append('/home/dev/SelfService/selfservice')
#sys.path.append('/home/dev/ssp/wavamezz')
#sys.path.append('/home/dev/ssp/msp')
#sys.path.append('/home/dev/ssp/dashboard')
=======
sys.path.append('/home/dev/Workspace/sspEnvFolder/self_service_platform/SelfService')
sys.path.append('/home/dev/Workspace/sspEnvFolder/self_service_platform/SelfService/selfservice')

>>>>>>> 538f38eee9fd4559fb66a7335e636d555121804f
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



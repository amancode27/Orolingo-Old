activate_this = 'C:/Users/Rp_Team/Envs/Rp_Web/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/Rp_Team/Envs/Rp_Web/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/Rp_Team/Rp_Web_Team')
sys.path.append('C:/Users/Rp_Team/Rp_Web_Team/Rp_Hall_Web')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Rp_Hall_Web.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rp_Hall_Web.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

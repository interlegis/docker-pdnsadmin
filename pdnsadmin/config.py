import os
basedir = os.path.abspath(os.path.dirname(__file__))

# BASIC APP CONFIG
WTF_CSRF_ENABLED = True
SECRET_KEY = os.getenv('SECRET_KEY')
BIND_ADDRESS = os.getenv('BIND_ADDRESS')
PORT = int(os.getenv('BIND_PORT'))
LOGIN_TITLE = os.getenv('LOGIN_TITLE')

# TIMEOUT - for large zones
TIMEOUT = int(os.getenv('TIMEOUT'))

# LOG CONFIG 
LOG_LEVEL = os.getenv('LOG_LEVEL')
LOG_FILE = 'logfile.log'

# Upload
UPLOAD_DIR = os.path.join(basedir, 'upload')

# DATABASE CONFIG
SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@mysql/%s" % (os.getenv('MYSQL_ENV_MYSQL_USER'), os.getenv('MYSQL_ENV_MYSQL_PASSWORD'),os.getenv('MYSQL_ENV_MYSQL_DATABASE'))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# LDAP CONFIG
if os.getenv('LDAP_TYPE').lower() != 'none' and os.getenv('LDAP_URI') != '':
  LDAP_TYPE = os.getenv('LDAP_TYPE').lower() # use 'ad' for MS Active Directory, 'ldap' otherwise
  LDAP_URI = os.getenv('LDAP_URI')
  LDAP_USERNAME = os.getenv('LDAP_USERNAME')
  LDAP_PASSWORD = os.getenv('LDAP_PASSWORD')
  LDAP_SEARCH_BASE = os.getenv('LDAP_SEARCHBASE')
  # Additional options only if LDAP_TYPE=ldap
  if os.getenv('LDAP_TYPE').lower() == 'ldap':
    LDAP_USERNAMEFIELD = os.getenv('LDAP_USERNAMEFIELD')
    LDAP_FILTER = os.getenv('LDAP_FILTER')

#Default Auth
BASIC_ENABLED = True
SIGNUP_ENABLED = True

# POWERDNS CONFIG
PDNS_STATS_URL = %PDNS_STATS_URL%
PDNS_API_KEY = os.getenv('PDNS_API_KEY')
PDNS_VERSION = os.getenv('PDNS_VERSION')

# RECORDS ALLOWED TO EDIT
RECORDS_ALLOW_EDIT = ['A', 'AAAA', 'CNAME', 'SPF', 'PTR', 'MX', 'TXT', 'NS', 'DS', 'SOA', 'SRV', 'CAA']
REVERSE_ALLOW_EDIT = ['PTR','NS']

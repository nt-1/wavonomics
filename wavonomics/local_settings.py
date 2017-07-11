import os
# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "z19egbpfu0n=8n#8agv@x)6nfatgh)t4m6wb(!22n4bn34j%6x"
NEVERCACHE_KEY = "3kvz#f*b%mtk&_=k^ot2&3dt^-reb)$jm7q@2ze4i2i53t3qkr"

# "default": {
#     # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
#     "ENGINE": "django.db.backends.sqlite3",
#     # DB name or path to database file if using sqlite3.
#     "NAME": "dev.db",
#     # Not used with sqlite3.
#     "USER": "",
#     # Not used with sqlite3.
#     "PASSWORD": "",
#     # Set to empty string for localhost. Not used with sqlite3.
#     "HOST": "",
#     # Set to empty string for default. Not used with sqlite3.
#     "PORT": "",
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        "default": {
            # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            # DB name or path to database file if using sqlite3.
            'NAME': 'wavonomics',
            # Not used with sqlite3.
            "USER": "antoinef",
            # Not used with sqlite3.
            "PASSWORD": "932900",
            # Set to empty string for localhost. Not used with sqlite3.
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
# ALLOWED_HOSTS = [""]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }

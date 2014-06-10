from {{project_name}}.settings.base import * 
DEBUG = True
TEMPLATE_DEBUG = True

database_dir = os.path.join(BASE_DIR, 'databases')

if not os.path.exists(database_dir):
	os.mkdir(database_dir)

media_dir = os.path.join(BASE_DIR, 'media')

if not os.path.exists(media_dir):
	os.mkdir(media_dir)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(database_dir, 'dev.db'),
    }
}

# Application definition

INSTALLED_APPS += (
)

#==============================================================================
# Static Files
#==============================================================================

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================

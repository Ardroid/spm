DEBUG = False
DEPLOY_PORT = 8106

STATIC_FOLDER = os.path.join(APP_FOLDER, "static")
TEMPLATE_FOLDER = os.path.join(APP_FOLDER, "templates")
SECRET_KEY = "RHBPfLmWFpDmOV0nPmMN5Ho0plwDIsuPKvFpME5zbwk="
MAX_CONTENT_LENGTH = 20 * 1024 * 1024 # Capped to 20MB
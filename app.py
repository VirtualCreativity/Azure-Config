import sys

from azure.identity import DefaultAzureCredential # pip install azure-identity   # pip show azure-identity
from azure.mgmt.web import WebSiteManagementClient # pip install azure-mgmt-web  # pip show azure-mgmt-web

# from azure.mgmt.web.models import SiteAppSettings


# Azure subscription ID
subscription_id = '8a032147-7a98-452f-8c30-84ae213e3b9b' # VirtualCreativity 'your-subscription-id'

# Web App (App Service) details
resource_group_name = 'VC-FlaskResource'
app_service_name = 'stat-gpt-v001'

# Application setting to add/edit
setting_name = 'OPENAI_API_KEY'
setting_value = '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'

# Authenticate using default credentials
# This will use your Azure CLI login, VSCode, or other configured authentication methods
credential = DefaultAzureCredential()

# Initialize the WebSite management client
web_client = WebSiteManagementClient(credential, subscription_id)

# Initialize the WebSite management client
#web_client = WebSiteManagementClient(credential, subscription_id)

# Retrieve the current application settings
# app_settings = web_client.web_apps.list_application_settings(resource_group_name, app_service_name).properties


# Retrieve the current application settings
app_settings = web_client.web_apps.list_application_settings(resource_group_name, app_service_name)

# Modify the settings
app_settings.properties[setting_name] = setting_value

print(app_settings)



# Retrieve the current application settings
# current_settings = web_client.web_apps.list_application_settings(resource_group_name, app_service_name)
# app_settings = current_settings.properties

# print(app_settings)

# sys.exit(0)


# Add/Edit the application setting
# app_settings[setting_name] = setting_value

# Convert dictionary to SiteAppSettings object
# new_settings = SiteAppSettings(properties=app_settings)


# Add/Edit the application setting
#app_settings[setting_name] = setting_value

# Update the application settings
# web_client.web_apps.update_application_settings(resource_group_name, app_service_name, str_dict=app_settings)

# Update the application settings
# updated_settings = web_client.web_apps.update_application_settings(resource_group_name, app_service_name, app_settings)

# Update the application settings
# updated_settings = web_client.web_apps.update_application_settings(resource_group_name, app_service_name, app_settings=new_settings)

# Update the application settings
web_client.web_apps.update_application_settings(resource_group_name, app_service_name, app_settings)



print(f"Application setting '{setting_name}' has been updated.")

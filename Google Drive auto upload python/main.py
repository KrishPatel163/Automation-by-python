from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = "1YyChB6etVBwfk-tEDMmrJXWowdkTs6Gi"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_meta_data = {
        'name': "folder test",
        'parents': [PARENT_FOLDER_ID]
    }

    # Use a raw string for the file path to prevent escape character interpretation
    media_body = MediaFileUpload(file_path)

    file = service.files().create(
        body=file_meta_data,
        media_body=media_body
    ).execute()

upload(r"C:\KRISH\Main Branch XD\Pyhton\Google Calendar API")

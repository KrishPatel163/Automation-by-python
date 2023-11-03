from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import os

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = "1YyChB6etVBwfk-tEDMmrJXWowdkTs6Gi"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    if os.path.isfile(file_path):
        print("<------ UPLOADING A FILE ------>")
        file_name = file_path.split('\\')[-1]

        file_meta_data = {
            'name': file_name,
            'parents': [PARENT_FOLDER_ID]
        }

        media_body = MediaFileUpload(file_path)

        file = service.files().create(
            body=file_meta_data,
            media_body=media_body
        ).execute()
    else:
        print("<------ UPLOADING A FOLDER ------>")

        for root, _, files in os.walk(file_path):
            for file in files:
                file_meta_data = {
                    'name': file,
                    'parents': [PARENT_FOLDER_ID]
                }

                media_body = MediaFileUpload(os.path.join(root, file))

                file = service.files().create(
                    body=file_meta_data,
                    media_body=media_body
                ).execute()

upload(r"C:\KRISH\Main Branch XD\websites\cuberto")

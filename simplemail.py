import os
import zipfile
from simplegmail import Gmail
from simplegmail.query import construct_query
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gmail = Gmail()
print("connected")

def send_mail():
    from simplegmail import Gmail

    params = {
    "to": "rootlevelau@gmail.com",
    "sender": "rootlevelau@gmail.com",
    "subject": "My first test email",
    "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
    "msg_plain": "Hi\nThis is a plain text email.",
    "signature": True  # use my account signature
    }
    message = gmail.send_message(**params)
    print("message sent")
    return message



def download_attachment(filename):

    messages = gmail.get_unread_inbox()

    query_params = {
    "newer_than": (7, "day"),
    "unread": True,
    "spec_attachment": "datafeed.zip"
        }

    messages = gmail.get_messages(query=construct_query(query_params))

    filename = []

    for message in messages:
        if message.attachments:
            for attm in message.attachments:
                print('File: ' + attm.filename)
                attm.save()  # downloads and saves each attachment under it's stored
                            # filename. You can download without saving with `attm.download()`
                filename.append(attm.filename)
    

def unzip():
    try:
        with zipfile.ZipFile("datafeed.zip", 'r') as zip_ref:
            zip_ref.extractall("")

    except Exception as e:
        print(e)



#Login to Google Drive and create drive object
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)
# Importing os and glob to find all PDFs inside subfolder

filename = "datafeed.csv"
with open(filename,"r") as f:
    fn = os.path.basename(f.name)
file_drive = drive.CreateFile({'title': fn })  
file_drive.SetContentString(f.read()) 
file_drive.Upload()
print ("The file: " + fn + " has been uploaded")
   
print ("All files have been uploaded")
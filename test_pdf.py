
import os, glob
from imbox import Imbox # pip install imbox
import traceback

# enable less secure apps on your google account
# https://myaccount.google.com/lesssecureapps

host = "imap.gmail.com"
username = "dr.grubylolek@gmail.com"
password = 'lkvd djam lizu exmo'
download_folder = "C:/Users/piotr/OneDrive/Pulpit/print-box/pdfs_file"

def download_pdf():
    if not os.path.isdir(download_folder):
        os.makedirs(download_folder, exist_ok=True)
        
    mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
    messages = mail.messages() # defaults to inbox

    for (uid, message) in messages:
        mail.mark_seen(uid) # optional, mark message as read

        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')
                download_path = f"{download_folder}/{att_fn}"
                print(download_path)
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())
            except:
                print(traceback.print_exc())

    mail.logout()



def print_file():
    parent_dir = 'C:/Users/piotr/OneDrive/Pulpit/print-box/pdfs_file'
    for pdf_file in glob.glob(os.path.join(parent_dir, '*.pdf')):
        print (pdf_file)


print_file()
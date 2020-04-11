import os

PATH = ""
SERVICE = ""
SECRET = ""

def update():
    os.chdir(PATH)
    os.system("git fetch --all")
    os.system("git checkout --force origin/master")
    os.system("systemctl restart {}".format(SERVICE))
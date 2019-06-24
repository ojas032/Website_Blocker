from datetime import datetime as dt
import time

hosts="hosts"
real_hosts=r"/etc/hosts"
redirect="127.0.0.1"

address=["www.facebook.com","facebook.com","www.youtube.com","https://www.youtube.com","youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) <dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(real_hosts,"r+") as myfile:
            p=myfile.read()
            for web in address:
                if web in p:
                    pass
                else:
                    myfile.write(redirect+" "+web+'\n')


    else:
        with open(real_hosts,"r+") as myfile:
            p=myfile.readlines()
            myfile.seek(0)
            for line in p:
                if not any(website in line for website in address):
                    myfile.write(line)
            myfile.truncate()
    time.sleep(10)

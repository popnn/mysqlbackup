import os
import time

while(1):

	os.system("cd /home/ubuntu/mysqlbackup && sudo git add . && sudo git commit -m 'auto commited from server' && sudo git push")
	time.sleep(86400)

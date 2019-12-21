import os
import time
commitCounter=0
while(1):

	os.system("cd /home/ubuntu/mysqlbackup && sudo git add . && sudo git commit -m 'commit number {}' && sudo git push").format(commitCounter)
	commitCounter+=1
	time.sleep(86400)

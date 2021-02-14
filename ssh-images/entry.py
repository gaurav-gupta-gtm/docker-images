import os
import sys

l=sys.argv
def minimum_env(l):
    if(len(l)==2 and os.system(l[1])==0):
        return False
    return True

if(minimum_env(l)):
    print("PASSWORD Updating...")
    os.system("echo {} | passwd root --stdin".format(l[1]))
    print("Successfully updated...")
    os.system("/usr/sbin/sshd -D")
else:
    print("You need to provide password for login through SSH...")
    print("Please provide ENV variable ROOT_PASSWORD")

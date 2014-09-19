#!/uer/bin/env python

import os
#from sh import nova 

homedir = os.path.expanduser("~/")
username = homedir.split("/")[-2]

# to avoid installing sh
#print nova ("flavor-list")

#print nova ("keypair-add", "--pub-key", "~/.ssh/id_rsa.pub" "%s-india-key" % username)
#print nova ("boot", "--flavor", "m1.small", "--image", "futuregrid/ubuntu-12.04", "--key_name", "%s-india-key" % username, username + "001")

os.system("nova keypair-add --pub-key ~/.ssh/id_rsa.pub {0}-india-key".format(username) )
os.system('nova boot --flavor m1.small --image "futuregrid/ubuntu-14.04" --key_name {0}-india-key {0}-001'.format(username) )

from sh import nova 
username = "gregor"

print nova ("flavor-list")
print nova ("boot", "--flavor", "m1.small", "--image", "futuregrid/ubuntu-12.04", "--key_name", "~/.ssh/id_rsa.pub", username + "001")


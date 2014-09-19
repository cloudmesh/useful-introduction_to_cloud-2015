#! /bin/sh -x

USERNAME=$USER
nova keypair-add --pub-key ~/.ssh/id_rsa.pub $USERNAME-india-key

nova boot --flavor m1.small \
            --image "futuregrid/ubuntu-14.04" \
            --key_name $USERNAME-india-key $USERNAME-001


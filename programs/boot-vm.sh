#! /bin/sh -x

USERNAME=$USER

nova boot --flavor m1.small \
            --image "futuregrid/ubuntu-14.04" \
            --key_name ~/.ssh/idrsa.pub $USERNAME-001

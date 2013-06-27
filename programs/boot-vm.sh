#! /bin/sh -x
nova boot --flavor m1.small \
            --image "futuregrid/ubuntu-12.04" \
            --key_name dmoney4454-key dmoney4454-001

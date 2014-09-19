#! /bin/bash

if [ "$1" != "" ]; then
    nova delete $1
else
    echo "VM ID or Name is required. Run 'nova list' to get the list of VMs"
    exit 1
fi


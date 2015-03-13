Best Practices for Preservation of IaaS and Data in FutureSystems
======================================================================

In any cloud you will be sooner or later be exposed to the question what to do with the images and the data in such images. This is especially important in research clouds such as FutureSystems that does not make any gurantees for preservation of data and images. It is in the users responsibility to deal with these issues.
Why is this so important:

1. there is no gurantee that the VM is running for more than 30 days. In fact VMS on Future systems will be deleted after 30 days. Why?

   Lazy users do not delete their VMs and thus block resources for other users. This is base don the fact that we do not yet charge for service units or ask you for money such as other cloud providers do. Thus please help and shut your vms down once you do not need them.

   Irresponsible users do not update their VMs. We observer that they do not take the machine in the same seriousness as they do when they run an OS on their own hradware (e.g. Laptops). The attidude, oh well, i do not have to deal with security because its not my hardware will fail. If we repeatedly find your VMs are compromised you will get denied access till you have proven responsiblr handeling of the VMS. **YOU ARE RESPONSIBLE TO KEEP UP WITH SECUITY PATCHES**. You must check back daily and follow the instructions of your OS and packages to keep them secure. You are now the administrator of your VMs.
   
2. In case your VM is compromised or the 30 day rule is up, your VM will be mercilessly terminated. Naturally if you have not made a backup, or do a backup of the data while running the VM you may lose what you have worked on.   
   
But how can you avoid catastrophic loss of the VM and the data in the VMs?

Firts the biggest mistake you can make is to develop a VM by hand! This is you download an ISO, log in, do lots of software install by hand, tweak this file, tweak taht file, forget how you actually tweaked it. Instead you **MUST** adopt policies and workflows that allow you to easily recreate images from scratch. Thus you should either work on scripts that you can run within the VM to updare the image with patches, or software or use devops frameworks to assist you in that.

Second, you must presere the runtime data of your programs you run in the VM. This is best achieved while using a source code repository such as git to preserve your code and a data backup to NFS in case you have an IU account. You can certainly back up your data alose remotely in case you are not an IU student. Please also note that data can npt be backed up indefenetly, and if you have special needs they can be discussed with the system administrators and your course teacher.
Furthermore, you can also use volumes that you attach to the VMS. THis is a good practice as it allows you to detach the storage issue form the VM so it is less problematic whne the VM is broken but you still have access to the volume where the data resides.

Summary Recommendations:

1. Backup, Backup, Backup. Its your responsibility.

This is probably pretty clear you can backup the image and the data to your local machine. If something goes wrong, you still have a copy. However if a vm that has been backed up is compromised, do not just rerun it. fix the security issues first.

2. Reproducability, Repreducibility, Repreducibility. Its your responsibility.

We recommend that you never work on a VM that  you can not regenerate with a script or automatic tools facilitated by devops. If the image needs to be tweaked by hand you do something wrong. AUtomate everything.

3. Security, Security, Security, Its your responsibility.

Its obvious that if a security issue occurs we **must** terminate the image. If you use 1 and 2 you will have no issue to deal with this.   

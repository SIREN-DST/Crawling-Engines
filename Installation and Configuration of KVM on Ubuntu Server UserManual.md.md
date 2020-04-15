## Installation and Configuration of KVM on Ubuntu Server

**KVM** (Kernel-based Virtual Machine) is an open source full virtualization solution for Linux like systems, KVM provides virtualization functionality using the virtualization extensions like **Intel VT** or **AMD-V**. 

Whenever we install KVM on any linux box then it turns it into the hyervisor by loading the kernel modules like **kvm-intel.ko**( for intel based machines) and **kvm-amd.ko** ( for amd based machines).
KVM allows us to install and run multiple virtual machines (Windows & Linux). We can create and manage KVM based virtual machines either via **virt-manager** graphical user interface or **virt-install** & **virsh** cli commands.

In this User Manual, we will discuss how to install and configure **KVM hypervisor** on Ubuntu 18.04 LTS server. I am assuming you have already installed Ubuntu 18.04 LTS server on your system. Login to your server and perform the following steps.


##  Verify Whether your system support hardware virtualization

Execute below **egrep** command to verify whether your system supports hardware virtualization or not,

-     serc@kvm-ubuntu18-04:~$ egrep -c '(vmx|svm)' /proc/cpuinfo
-	  serc@kvm-ubuntu18-04: 4
	
If the output is greater than 0 then it means your system supports Virtualization else reboot your system, then go to BIOS settings and enable VT technology.

Now Install “**kvm-ok**” utility using below command, it is used to determine if your server is capable of running hardware accelerated KVM virtual machines.

 -     serc@kvm-ubuntu18-04:~$ sudo apt install cpu-checker

Run kvm-ok command and verify the output,


 -     serc@kvm-ubuntu18-04:~$ sudo kvm-ok

 -     INFO: /dev/kvm exists KVM acceleration can be used

#
## Install KVM and its required packages

Run the below apt commands to install KVM and its dependencies

 -     serc@kvm-ubuntu18-04:~$ sudo apt update

 -     serc@kvm-ubuntu18-04:~$ sudo apt install qemu qemu-kvm libvirt-bin  bridge-utils  virt-manager

Once the above packages are installed successfully, then your local user (In my case serc) will be added to the group libvirtd automatically.

#

## Start & enable libvirtd service

Whenever we install qemu & libvirtd packages in Ubuntu 18.04 Server then it will automatically start and enable libvirtd service, In case libvirtd service is not started and enabled then run beneath commands,

 -     serc@kvm-ubuntu18-04:~$ sudo service libvirtd start

 -     serc@kvm-ubuntu18-04:~$ sudo update-rc.d libvirtd enable

Now verify the status of libvirtd service using below command,


 -     serc@kvm-ubuntu18-04:~$ service libvirtd status

 
**Output would be something like below**


![Libvirtd Service Status](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/1.PNG)

#

## Configure Network Bridge for KVM virtual Machines

Network bridge is required to access the KVM based virtual machines outside the KVM hypervisor or host. In Ubuntu 18.04, network is managed by netplan utility, whenever we freshly installed Ubuntu 18.04 server then netplan file is created under  **/etc/netplan/.**  In most of the hardware and virtualized environment, netplan file name would be “**50-cloud-init.yaml**” or “**01-netcfg.yaml”,** to configure static IP and bridge, netplan utility will refer this file.


As of now I have already configured the static IP via this file and content of this file is below:


![Network Connection](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/2.PNG)

Let’s add the network bridge definition in this file,

 -     serc@kvm-ubuntu18-04:~$ sudo vi /etc/netplan/50-cloud-init.yaml
 
 
 ![Bridge Connection](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/3.PNG)

As you can see we have removed the IP address from interface(ens33) and add the same IP to the bridge ‘**br0**‘ and also added interface (ens33) to the bridge br0. Apply these changes using below netplan command,

 -     serc@kvm-ubuntu18-04:~$ sudo netplan apply

 -     serc@kvm-ubuntu18-04:~$

If you want to see the debug logs then use the below command,

 -     serc@kvm-ubuntu18-04:~$ sudo netplan --debug  apply

Now Verify the bridge status using following methods:

 -     serc@kvm-ubuntu18-04:~$ sudo networkctl status -a

 
![Network Configuration Details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/4.PNG)

-     serc@kvm-ubuntu18-04:~$ ifconfig

![Network Configuration Details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/5.PNG)

#

##  Creating Virtual machine (virt-manager or virt-install command )

There are two ways to create virtual machine:

 - virt-manager (GUI utility)

 - virt-install command (cli utility)

**Creating Virtual machine using virt-manager:**

Start the virt-manager by executing the beneath command,

 -     serc@kvm-ubuntu18-04:~$ sudo virt-manager

![Virt_manager Display](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/6.PNG)

Create a new virtual machine,

![Virt_manager Display](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/7.PNG)

Click on forward and select the ISO file, in my case I am using RHEL 7.3 iso file we could use any other ubuntu iso files to install the Virtual Machine on KVM.

![VM installation](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/8.PNG)

Click on Forward , Make sure that the path of the iso file should be available and it should not be broken in any means.

In the next couple of windows, you will be prompted to specify the RAM, CPU and disk for the VM.

Now Specify the Name of the Virtual Machine and network,

![VM installation](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/9.PNG)

Click on Finish

![VM installation](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/10.PNG)

Now follow the screen instruction and complete the installation.

**Creating Virtual machine from CLI using virt-install command**

Use the below virt-install command to create a VM from terminal, it will start the installation in CLI, replace the name of the VM, description, location of ISO file and network bridge as per your setup.

 -     serc@kvm-ubuntu18-04:~$ sudo virt-install  -n Ubuntu-Server  --description "Test VM for Database"  --os-type=Linux  --os-variant=ubuntu --ram=1096  --vcpus=1  --disk path=/var/lib/libvirt/images/ubuntu.img,bus=virtio,size=100  --network bridge:br0 --graphics none  --location /home/serc/ubuntu18.04-x86_64-dvd.iso --extra-args console=ttyS0
 
#
  **Create, Revert, Delete KVM Virtual Machine with Virsh Command**
  
  While working on the virtualization platform system administrators usually take the snapshot of virtual machine before doing any major activity like deploying the latest patch and code.

Virtual machine  **snapshot**  is a copy of virtual machine’s disk at the specific point of time. In other words we can say snapshot keeps or preserve the state and data of a virtual machine at given point of time.

**Where we can use VM snapshots ..?**

If you are working on **KVM** based **hypervisors** we can take virtual machines or domain snapshot using the virsh command. Snapshot becomes very helpful in a situation where you have installed or apply the latest patches on the VM but due to some reasons, application hosted in the VMs becomes unstable and application team wants to revert all the changes or patches. If you had taken the snapshot of the VM before applying patches then we can restore or revert the VM to its previous state using snapshot.

**Note:** We can only take the snapshot of the VMs whose disk format is **Qcow2** and raw disk format is not supported by kvm virsh command, Use below command to convert the raw disk format to qcow2

 -  	qemu-img convert -f raw -O qcow2 image-name.img image-name.qcow2

**Create KVM Virtual Machine (domain) Snapshot**

I am assuming KVM hypervisor is already configured on CentOS 7 / RHEL 7/Ubuntu box and VMs are running on it. We can list the all the VMs on hypervisor using below virsh command,

![VM Snapshot](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/11.PNG)

Let’s suppose we want to create the snapshot of ‘**webserver**‘ VM, run the below command,

**Syntax :**

-     virsh snapshot-create-as –domain {vm_name} –name {snapshot_name} –description “enter description here”

![VM Snapshot](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/12.PNG)

To list the detailed info of VM’s snapshot, run the beneath virsh command,


![VM Snapshot](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/13.PNG)

We can view the size of snapshot using below qemu-img command,

 -     [root@kvm-hypervisor ~]# qemu-img info /var/lib/libvirt/images/snaptestvm.img

![VM Snapshot](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/14.PNG)

#### Revert / Restore KVM virtual Machine to Snapshot

Let’s assume we want to revert or restore webserver VM to the snapshot that we have created in above step. Use below virsh command to restore Webserver VM to its snapshot “**webserver_snap**”

**Syntax :**

-     virsh snapshot-revert {vm_name} {snapshot_name}

![VM Snapshot](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/15.PNG)

#### Delete KVM virtual Machine Snapshots

To delete KVM virtual machine snapshots, first get the VM’s snapshot details using “**virsh snapshot-list**” command and then use “**virsh snapshot-delete**” command to delete the snapshot. Example is shown below:

![VM Snapshot](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/16.PNG)

![VM Snapshot](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/KVM/17.PNG)

#

That’s conclude the UserManual, I hope this article help you to install KVM on your Ubuntu 18.04 Server. Apart from this, KVM is the default hypervisor for Openstack.


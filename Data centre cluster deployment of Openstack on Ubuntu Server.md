## Data centre cluster deployment of Openstack on Ubuntu Server

This is the simplest Charmed OpenStack deployment process across a small cluster of bare-metal machines. It uses OpenStack charms which provide the operator functionality for OpenStack services, abstracting the entire operations complexity in a form of primitives. OpenStack charms not only simplify the entire deployment process, but also make post-deployment easier, supporting even very complex operations, such as OpenStack upgrades. Use the following instructions for your first data center cluster deployment and  [contact us](https://ubuntu.com/openstack/contact-us)  to continue the journey.

### Installation instructions

#### Minimum requirements
    
    6 x Intel, POWER or ARM servers each with:
    
    -   IPMI BMC
    -   at least 8GB RAM
    -   at least 2 Ethernet NICs
    -   at least 2 disks
    
All machines have to be connected with an Ethernet switch. There should be two isolated /24 subnets configured and each machine should be connected to both. We will call them provisioning and cloud, and use 172.16.7.0/24, and 172.16.8.0/24 subnets respectively. There must not be a DHCP server on the provisioning subnet. There must be access to the Internet from both subnets. We will use 172.16.7.1 and 172.16.8.1 IP addresses as gateways.
    
    NOTE:  HA clouds require 12 nodes for service isolation.
    
#### Bootstrap and configure the first node

The first node, referred to as the MAAS node in the following part of the tutorial, has to be bootstrapped and configured manually.

Download Ubuntu Server LTS from  [here](https://ubuntu.com/download/server)  and install it on the first node. We will call this node a MAAS node. Make sure that both NICs have IP addresses configured. We will use 172.16.7.2 and 172.16.8.2 respectively.
    
Then install prerequisites:

 -     $ sudo apt -y install snapd
 
And update the  `PATH`  environment variable:
```
$ export PATH=$PATH:/snap/bin

$ echo "export PATH=$PATH:/snap/bin" >> .bashrc
```
Now you can move to MAAS installation and configuration.

#### Install and configure MAAS

On the MAAS node, install MAAS by executing the following command:

 -     sudo apt -y install maas

This command takes a while. Once finished, initialise MAAS by running:

-     sudo maas init --mode all

Answer the questions accordingly to create an admin user account, set up its password. You can optionally import public SSH keys from GitHub or Launchpad. Those keys will be used to provide an access to provisioned instances, so ifyou store your public SSH keys in GitHub or Launchpad, it is a good idea to import them now:

```
Create first admin account:
  Username: admin
  Password:
  Again:
  Email: admin@example.com
  Import SSH keys [] (lp:user-id or gh:user-id): lp:tkurek
```

At this point you can access MAAS at `http://<MAAS_IP>:5240/MAAS`. Fill in admin user credentials and press the “Login” button:


![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/1.png)


Configure the “DNS forwarder” field to an IP address of a DNS server of your choice:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/2.png)

Then scroll down and press the “Continue” button:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/3.png)

One more time you have an opportunity to import public SSH keys from GitHub or Launchpad. Once you are done, press the “Go to dashboard” button:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/4.png)

You should see the MAAS Machines page. Do not worry about the warning message for now:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/5.png)

Unless you have imported your public SSH keys from GitHub/Launchpad in one of the previous steps, navigate the “admin” tab in the top right corner and go to the “SSH keys” section. You can use the “Source” drop-down list to either upload or import the keys:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/6.png)

For example, to upload the key, paste its value to the “Public key” field and press the “Import” button:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/7.png)

Then navigate to the ‘Subnets” tab in the top menu and press on the “untagged” VLAN next to the “172.16.7.0/24” subnet (the `provisioning` subnet):

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/8.png)

From the “Take action” drop-down menu on the right select “Provide DHCP”:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/9.png)

Fill in the “Dynamic range start IP” and “Dynamic range end IP” fields and press the “Provide DHCP” button:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/10.png)

At this point, your MAAS instance is ready to provision other machines.

#### Bootstrap and configure other nodes

All other nodes should be configured to PXE boot from the provisioning subnet by default.

Once configured, power them on and wait until they show up in the “Machines” tab in MAAS:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/11.png)

Then click on each of those machines and for each of them perform the following actions:

 Change their name to something more meaningful. Click on the old name, type the new one and press the “Save” button:
 
![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/12.png)

Add power configuration if missing. Navigate to the “Configuration” tab in the machine menu and scroll down to the “Power configuration section”. Select power type (IPMI in this case) and fill in other required fields. Once done, press the “Save changes” button:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/13.png)

Once all machines are configured, navigate to the “Machines” tab in the main menu, check all machines and select “Commission” from the “Take action” menu on the right:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/14.png)

Press “Commission 5 machines” button:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/15.png)

The nodes are going through the commissioning process. It may take a while. Once finished, you should see the following output:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/16.png)

Click on each of the machines again and for each of them go to the “Interfaces” tab in the machine menu. Make sure that both interfaces are configured as per the screenshot below. Adjust them if needed by pressing the lines under “Actions” and selecting “Edit Physical”:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/17.png)

At this point the remaining machines are ready for being provisioned.

#### Bootstrap Juju controller

On the MAAS node, install Juju client by executing the following command:

 -     sudo snap install juju --classic

Add MAAS cloud by running:

 -     juju add-cloud --local

Answer the questions accordingly:
```
Select cloud type: maas
  Enter a name for your maas cloud: maas
  Enter the API endpoint url: http://172.16.7.2:5240/MAAS
  Cloud "maas" successfully added to your local client.
```

Display the MAAS API key. You will need it in the next step.

 -     sudo maas-region apikey --username=admin

Add credentials for the MAAS cloud:

 -     juju add-credential maas

And answer the questions accordingly. Use the MAAS API key in the maas-oauth line:

```
Do you ONLY want to add a credential to this client? (Y/n): Y
  Enter credential name: maas
  Regions
  default
  Select region [any region, credential is not region specific]: default
  Using auth-type "oauth1".
  Enter maas-oauth:
  Credential "maas" added locally for cloud "maas".
```

At this point you can bootstrap the Juju controller on the MAAS cloud:

 -     juju bootstrap maas maas-controller

This command takes a while. Once finished, add a model for your OpenStack installation:

 -     juju add-model openstack

At this point, Juju is ready to deploy OpenStack on the remaining four machines.

#### Deploy OpenStack

In this example, we are using the  [OpenStack Base](https://jaas.ai/openstack-base/bundle/65)  bundle which provides basic OpenStack services and no HA. 

Run the following command to deploy OpenStack Base bundle:

 -     juju deploy cs:bundle/openstack-base

This command takes a while. Once finished you should see the following output on the bottom:

```
Deploy of bundle completed.
```

But it does not mean that your OpenStack deployment is done. In fact, it hasjust started. You have to monitor the status by running juju status command.The deployment is completed once all applications, units and machines turn to the “active” state as depicted on the listing below:

```
juju status
  Model      Controller       Cloud/Region  Version  SLA          Timestamp
  openstack  maas-controller  maas/default  2.7.0    unsupported  12:22:38-05:00

  App                    Version  Status  Scale  Charm                  Store       Rev  OS      Notes
  ceph-mon               14.2.2   active      3  ceph-mon               jujucharms   44  ubuntu
  ceph-osd               14.2.2   active      3  ceph-osd               jujucharms  294  ubuntu
  ceph-radosgw           14.2.2   active      1  ceph-radosgw           jujucharms  283  ubuntu
  cinder                 15.0.0   active      1  cinder                 jujucharms  297  ubuntu
  cinder-ceph            15.0.0   active      1  cinder-ceph            jujucharms  251  ubuntu
  glance                 19.0.0   active      1  glance                 jujucharms  291  ubuntu
  keystone               16.0.0   active      1  keystone               jujucharms  309  ubuntu
  mysql                  5.7.20   active      1  percona-cluster        jujucharms  281  ubuntu
  neutron-api            15.0.0   active      1  neutron-api            jujucharms  282  ubuntu
  neutron-gateway        15.0.0   active      1  neutron-gateway        jujucharms  276  ubuntu
  neutron-openvswitch    15.0.0   active      3  neutron-openvswitch    jujucharms  269  ubuntu
  nova-cloud-controller  20.0.0   active      1  nova-cloud-controller  jujucharms  339  ubuntu
  nova-compute           20.0.0   active      3  nova-compute           jujucharms  309  ubuntu
  ntp                    3.2      active      4  ntp                    jujucharms   36  ubuntu
  openstack-dashboard    16.0.0   active      1  openstack-dashboard    jujucharms  297  ubuntu
  placement              2.0.0    active      1  placement              jujucharms    1  ubuntu
  rabbitmq-server        3.6.10   active      1  rabbitmq-server        jujucharms   97  ubuntu

  Unit                      Workload  Agent  Machine  Public address  Ports              Message
  ceph-mon/0                active    idle   1/lxd/0  172.16.7.164                       Unit is ready and clustered
  ceph-mon/1                active    idle   2/lxd/1  172.16.7.163                       Unit is ready and clustered
  ceph-mon/2*               active    idle   3/lxd/0  172.16.7.165                       Unit is ready and clustered
  ceph-osd/0*               active    idle   1        172.16.7.160                       Unit is ready (1 OSD)
  ceph-osd/1                active    idle   2        172.16.7.161                       Unit is ready (1 OSD)
  ceph-osd/2                active    idle   3        172.16.7.162                       Unit is ready (1 OSD)
  ceph-radosgw/0*           active    idle   0/lxd/0  172.16.7.166    80/tcp             Unit is ready
  cinder/0*                 active    idle   1/lxd/2  172.16.7.168    8776/tcp           Unit is ready
  cinder-ceph/0*          active    idle            172.16.7.168                       Unit is ready
  glance/0*                 active    idle   2/lxd/1  172.16.7.167    9292/tcp           Unit is ready
  keystone/0*               active    idle   3/lxd/2  172.16.7.169    5000/tcp           Unit is ready
  mysql/0*                  active    idle   0/lxd/2  172.16.7.170    3306/tcp           Unit is ready
  neutron-api/0*            active    idle   1/lxd/2  172.16.7.171    9696/tcp           Unit is ready
  neutron-gateway/0*        active    idle   0        172.16.7.159                       Unit is ready
  ntp/0*                  active    idle            172.16.7.159    123/udp            chrony: Ready
  nova-cloud-controller/0*  active    idle   2/lxd/2  172.16.7.172    8774/tcp,8775/tcp  Unit is ready
  nova-compute/0*           active    idle   1        172.16.7.160                       Unit is ready
  neutron-openvswitch/2   active    idle            172.16.7.160                       Unit is ready
  ntp/3                   active    idle            172.16.7.160    123/udp            chrony: Ready
  nova-compute/1            active    idle   2        172.16.7.161                       Unit is ready
  neutron-openvswitch/1   active    idle            172.16.7.161                       Unit is ready
  ntp/2                   active    idle            172.16.7.161    123/udp            chrony: Ready
  nova-compute/2            active    idle   3        172.16.7.162                       Unit is ready
  neutron-openvswitch/0*  active    idle            172.16.7.162                       Unit is ready
  ntp/1                   active    idle            172.16.7.162    123/udp            chrony: Ready
  openstack-dashboard/0*    active    idle   3/lxd/2  172.16.7.174    80/tcp,443/tcp     Unit is ready
  placement/0*              active    idle   2/lxd/3  172.16.7.175    8778/tcp           Unit is ready
  rabbitmq-server/0*        active    idle   0/lxd/2  172.16.7.176    5672/tcp           Unit is ready

  Machine  State    DNS           Inst id              Series  AZ       Message
  0        started  172.16.7.159  openstack1           bionic  default  Deployed
  0/lxd/0  started  172.16.7.166  juju-592de2-0-lxd-3  bionic  default  Container started
  0/lxd/1  started  172.16.7.170  juju-592de2-0-lxd-4  bionic  default  Container started
  0/lxd/2  started  172.16.7.176  juju-592de2-0-lxd-5  bionic  default  Container started
  1        started  172.16.7.160  openstack2           bionic  default  Deployed
  1/lxd/0  started  172.16.7.164  juju-592de2-1-lxd-3  bionic  default  Container started
  1/lxd/1  started  172.16.7.168  juju-592de2-1-lxd-4  bionic  default  Container started
  1/lxd/2  started  172.16.7.171  juju-592de2-1-lxd-5  bionic  default  Container started
  2        started  172.16.7.161  openstack3           bionic  default  Deployed
  2/lxd/0  started  172.16.7.163  juju-592de2-2-lxd-4  bionic  default  Container started
  2/lxd/1  started  172.16.7.167  juju-592de2-2-lxd-5  bionic  default  Container started
  2/lxd/2  started  172.16.7.172  juju-592de2-2-lxd-6  bionic  default  Container started
  2/lxd/3  started  172.16.7.175  juju-592de2-2-lxd-7  bionic  default  Container started
  3        started  172.16.7.162  openstack4           bionic  default  Deployed
  3/lxd/0  started  172.16.7.165  juju-592de2-3-lxd-3  bionic  default  Container started
  3/lxd/1  started  172.16.7.169  juju-592de2-3-lxd-4  bionic  default  Container started
  3/lxd/2  started  172.16.7.174  juju-592de2-3-lxd-5  bionic  default  Container started
```

This is what you should be able to see in the “Machines” tab in MAAS:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/18.png)

At this point, your OpenStack installation is ready for being tested.

#### Interact with OpenStack

Set the admin user’s password for your OpenStack cluster by executing the following command:

 - juju config keystone admin-password=<password>

The Horizon service is available at the IP address displayed by running:
 - juju status | grep openstack-dashboard | tail -n 1 | awk '{print $5}'

Go to `http://<Horizon IP>:80/horizon` URL. You should see the OpenStack login screen. Type your credentials and press the “Sign In” button. Use “admin_domain” in the “Domain” field:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/19.png)

You should be able to see the OpenStack welcome screen. Click on the “admin” drop-down list in the top right corner and press “OpenStack RC File”:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/20.png)

Some browsers may require that you confirm that you want to download this file. If you are using Google Chrome, press “Keep” from the menu on the bottom:

![Cluster Stack Login ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/DataCentre/21.png)

Place the downloaded file on a machine where you want to install the OpenStack client. Then install it by running the following command:

 - sudo apt -y install python3-openstackclient

Source the downloaded RC file:

 - source admin-openrc.sh

 And enter the admin user’s password when asked:

 ```
Please enter your OpenStack Password for project admin as user admin:
```

At this point you can interact with your OpenStack cluster using standard commands, for example:

```
$ openstack catalog list
+-----------+--------------+--------------------------------------------------------------------------+
| Name      | Type         | Endpoints                                                                |
+-----------+--------------+--------------------------------------------------------------------------+
| cinderv2  | volumev2     | RegionOne                                                                |
|           |              |   admin: http://172.16.7.168:8776/v2/d5c39f5ee61b4d7c8a57ed26672f5bf1    |
|           |              | RegionOne                                                                |
|           |              |   public: http://172.16.7.168:8776/v2/d5c39f5ee61b4d7c8a57ed26672f5bf1   |
|           |              | RegionOne                                                                |
|           |              |   internal: http://172.16.7.168:8776/v2/d5c39f5ee61b4d7c8a57ed26672f5bf1 |
|           |              |                                                                          |
| nova      | compute      | RegionOne                                                                |
|           |              |   admin: http://172.16.7.172:8774/v2.1                                   |
|           |              | RegionOne                                                                |
|           |              |   public: http://172.16.7.172:8774/v2.1                                  |
|           |              | RegionOne                                                                |
|           |              |   internal: http://172.16.7.172:8774/v2.1                                |
|           |              |                                                                          |
| neutron   | network      | RegionOne                                                                |
|           |              |   public: http://172.16.7.171:9696                                       |
|           |              | RegionOne                                                                |
|           |              |   internal: http://172.16.7.171:9696                                     |
|           |              | RegionOne                                                                |
|           |              |   admin: http://172.16.7.171:9696                                        |
|           |              |                                                                          |
| cinderv3  | volumev3     | RegionOne                                                                |
|           |              |   public: http://172.16.7.168:8776/v3/d5c39f5ee61b4d7c8a57ed26672f5bf1   |
|           |              | RegionOne                                                                |
|           |              |   admin: http://172.16.7.168:8776/v3/d5c39f5ee61b4d7c8a57ed26672f5bf1    |
|           |              | RegionOne                                                                |
|           |              |   internal: http://172.16.7.168:8776/v3/d5c39f5ee61b4d7c8a57ed26672f5bf1 |
|           |              |                                                                          |
| swift     | object-store | RegionOne                                                                |
|           |              |   internal: http://172.16.7.166:80/swift/v1                              |
|           |              | RegionOne                                                                |
|           |              |   admin: http://172.16.7.166:80/swift                                    |
|           |              | RegionOne                                                                |
|           |              |   public: http://172.16.7.166:80/swift/v1                                |
|           |              |                                                                          |
| keystone  | identity     | RegionOne                                                                |
|           |              |   internal: http://172.16.7.169:5000/v3                                  |
|           |              | RegionOne                                                                |
|           |              |   admin: http://172.16.7.169:35357/v3                                    |
|           |              | RegionOne                                                                |
|           |              |   public: http://172.16.7.169:5000/v3                                    |
|           |              |                                                                          |
| placement | placement    | RegionOne                                                                |
|           |              |   admin: http://172.16.7.175:8778                                        |
|           |              | RegionOne                                                                |
|           |              |   internal: http://172.16.7.175:8778                                     |
|           |              | RegionOne                                                                |
|           |              |   public: http://172.16.7.175:8778                                       |
|           |              |                                                                          |
| glance    | image        | RegionOne                                                                |
|           |              |   public: http://172.16.7.167:9292                                       |
|           |              | RegionOne                                                                |
|           |              |   internal: http://172.16.7.167:9292                                     |
|           |              | RegionOne                                                                |
|           |              |   admin: http://172.16.7.167:9292                                        |
|           |              |                                                                          |
+-----------+--------------+--------------------------------------------------------------------------+
```


In order to create tenants, networks, launch instances, etc., refer to the python-openstackclient [documentation](https://docs.openstack.org/python-openstackclient/latest/cli/command-list.html).


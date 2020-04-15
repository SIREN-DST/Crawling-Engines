# **Multi-node OpenStack deployment on Ubuntu Server**

These instructions use [MicroStack](https://snapcraft.io/microstack) too. However, in this case a clustering feature is used.

**Installation instructions**
#### Minimum requirements

 - At least two machines, each with 16GB RAM, a multi-core processor and at least 50GB of free disk space, connected to a network, and running Ubuntu 18.04 LTS or later.

#### Install MicroStack

 - If you are using Ubuntu 18.04 LTS, which we highly recommend, you can install MicroStack right away by running the following command from the terminal:
	 -     sudo snap install microstack --classic --edge
In case you are using Ubuntu 19.10 or Ubuntu 20.04 LTS, use the following command instead:
 -     sudo snap install microstack --classic --edge
Once installed, you should see the following message on the terminal:
 -     microstack (edge) stein from Canonical✓ installed
 
 The version displayed (here, Stein) matches the most recent stable OpenStack release available with MicroStack.

Install MicroStack on all machines which will be used for OpenStack clustering purposes.

**NOTE:** MicroStack installed with the `--devmode` flag will not receive updates.

#### Initialise MicroStack on the control machine

Run the following command on the machine you want to act as a controller. Answer the questions accordingly and set up a cluster password:

```
$ sudo microstack.init
Do you want to setup clustering? (yes/no) [default=no] > yes
2019-12-16 14:02:05,876 - microstack_init - INFO - Configuring clustering ...
What is this machines' role? (control/compute) > control
Please enter a cluster password >
Please re-enter password >
Please enter the ip address of the control node [default=172.31.31.254] > 172.31.31.254
2019-12-16 14:02:29,825 - microstack_init - INFO - I am a control node.
...
2019-12-16 14:06:54,973 - microstack_init - INFO - Complete. Marked microstack as initialized!
```
Your OpenStack control machine is now running and is ready for adding compute machines.

#### Initialise MicroStack on compute machines

Run the following command on all machines you want to act as compute nodes. Answer the questions accordingly and use the cluster password which you set in the previous step:

```
$ sudo microstack.init
Do you want to setup clustering? (yes/no) [default=no] > yes
2019-12-16 14:14:17,919 - microstack_init - INFO - Configuring clustering ...
What is this machines' role? (control/compute) > compute
Please enter a cluster password >
Please re-enter password >
Please enter the ip address of the control node [default=10.20.20.1] > 172.31.31.254
Please enter the ip address of this node [default=172.31.24.59] > 172.31.24.59
2019-12-16 14:14:46,382 - microstack_init - INFO - I am a compute node.
...
2019-12-16 14:15:03,594 - microstack_init - INFO - Complete. Marked microstack as initialized!
```
Your OpenStack cloud is now running and is ready for use!

#### Interact with MicroStack

You can interact with your OpenStack either via the web GUI or the CLI.

**Web GUI:**

To interact with your OpenStack via the web GUI visit http://10.20.20.1/ and log in with the following credentials:

```
username: admin
password: keystone
```
Type the credentials and press the ‘Sign In’ button:

![OpenStack Login ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/OpenStack/1.PNG)

You should now see the OpenStack dashboard:

![OpenStack Dashboard](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/OpenStack/2.PNG)

You can start playing with your local private cloud (i.e. create additional users, launch instances, etc.).

**CLI:**

You can also interact withOpenStack via the CLI by using the  `microstack.openstack`  command. The MicroStack CLI syntax is identical to the client delivered by the  [python-openstackclient](https://docs.openstack.org/python-openstackclient/latest/cli/command-list.html)  package.

For example, to list available OpenStack endpoints run:

	- microstack.openstack catalog list	
It should return the following list:

```
+-----------+-----------+-----------------------------------------+
| Name      | Type      | Endpoints                               |
+-----------+-----------+-----------------------------------------+
| keystone  |  identity | microstack                              |
|           |           | public: http://10.20.20.1:5000/v3/      |
|           |           | microstack                              |
|           |           | internal: http://10.20.20.1:5000/v3/    |
|           |           | microstack                              |
|           |           | admin: http://10.20.20.1:5000/v3/       |
|           |           |                                         |
| glance    | image     | microstack                              |
|           |           |   admin: http://10.20.20.1:9292         |
|           |           | microstack                              |
|           |           |   public: http://10.20.20.1:9292        |
|           |           | microstack                              |
|           |           |   internal: http://10.20.20.1:9292      |
|           |           |                                         |
| neutron   | network   | microstack                              |
|           |           |   public: http://10.20.20.1:9696        |
|           |           | microstack                              |
|           |           |   admin: http://10.20.20.1:9696         |
|           |           | microstack                              |
|           |           |   internal: http://10.20.20.1:9696      |
|           |           |                                         |
| nova      | compute   | microstack                              |
|           |           |   public: http://10.20.20.1:8774/v2.1   |
|           |           | microstack                              |
|           |           |   admin: http://10.20.20.1:8774/v2.1    |
|           |           | microstack                              |
|           |           |   internal: http://10.20.20.1:8774/v2.1 |
|           |           |                                         |
| placement | placement | microstack                              |
|           |           |   public: http://10.20.20.1:8778        |
|           |           | microstack                              |
|           |           |   admin: http://10.20.20.1:8778         |
|           |           | microstack                              |
|           |           |   internal: http://10.20.20.1:8778      |
|           |           |                                         |
+-----------+-----------+-----------------------------------------+
```

Running  `microstack.openstack --help`  will get you a list of available subcommands and their required syntax.

#### Launch an instance

The quickest way to launch your first OpenStack instance (or a VM) is to run the following command:

```
$ microstack.launch cirros --name test --availability-zone
nova:<compute nodehostname>
```

For example:

```
$ microstack.launch cirros --name test --availability-zone
nova:ip-172-31-24-59
```

This should result in a lot of output from which the most important are the last two lines:

```
Access it with `ssh -i $HOME/.ssh/id_microstack` <username>@10.20.20.3
You can also visit the openstack dashboard at 'http://10.20.20.1/
```

Note that the IP address of the instance may be different in your environment. In order to connect to the instance run the ‘ssh’ command from the output:

Copy to clipboard

You are now connected to your first instance on your OpenStack cluster. You can start playing with it by executing various commands, for example:

```
uptime
15:17:19 up 5 min, 1 users, load average: 0.00, 0.00, 0.00
```

In order to disconnect from the instance type exit.

In order to perform a more advanced launch (e.g. specify the flavor, use a different image, etc.) refer to the python-openstackclient  [documentation](https://docs.openstack.org/python-openstackclient/latest/cli/command-list.html). The syntax of the  `microstack.openstack`  command is the same as the syntax of the upstream client (for example  `microstack.openstack server list`).

#





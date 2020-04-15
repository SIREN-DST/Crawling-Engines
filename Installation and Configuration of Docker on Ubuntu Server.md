# Installation and Configuration of Docker on Ubuntu Server 

Docker is a containerization technology that allows you to quickly build, test, and deploy applications as portable, self-sufficient containers that can run virtually anywhere. Docker has become the de facto standard for container deployment, and it is an essential tool for DevOps engineers and their continuous integration and delivery pipeline.

In this User Manual , we’ll cover how to install Docker on an Ubuntu 18.04 machine and explore the basic Docker concepts and commands.

 ## Prerequisites
 
 Before continuing with this tutorial, make sure you are logged in as a [user with sudo privileges](https://linuxize.com/post/how-to-create-a-sudo-user-on-ubuntu/). All the commands in this tutorial should be run as a non-root user.
 
## Installing Docker on Ubuntu

Although the Docker installation package is available in the official Ubuntu 18.04 repository, it may not always be the latest version. The recommended approach is to install the latest Docker package from the Docker’s repositories.

### Enabling Docker repository

Start by updating the packages list and installing the dependencies necessary to  [add a new repository](https://linuxize.com/post/how-to-add-apt-repository-in-ubuntu/)  over HTTPS:    
    
    $ sudo apt update
    $ sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common    
   
 Import the repository’s GPG key using the following [`curl`](https://linuxize.com/post/curl-command-examples/) command:
 
 
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
 
Add the Docker [APT repository](https://linuxize.com/post/how-to-add-apt-repository-in-ubuntu/) to your system:
 
    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
 
 ## Installing Docker CE
 Now that the Docker repository is enabled, you can install any Docker version you need.
 
 To install the latest version of Docker use the command below. If you want to install a specific Docker version, skip this step and go to the next one.
 
    
    
    $ sudo apt update
    
    
To install a specific version, first list the available versions in the Docker repository:
    
    
    $ apt list -a docker-ce
    
    
  The command prints the available Docker versions in the second column.
    
    Output
    
    docker-ce/bionic 5:18.09.7~3-0~ubuntu-bionic amd64
    docker-ce/bionic 5:18.09.6~3-0~ubuntu-bionic amd64
    docker-ce/bionic 5:18.09.5~3-0~ubuntu-bionic amd64
    
    
 For example, to install version  `18.09.6`  you would type:
    
    
    $ sudo apt install docker-ce=5:18.09.6~3-0~ubuntu-bionic
    
    
  To prevent the Docker package from being automatically updated, mark it as held back:
    
    
    $ sudo apt-mark hold docker-ce
    
    

Once the installation is completed, the Docker service will start automatically. You can verify it by typing:

```
 $ sudo systemctl status docker
```

The output will look something like this:

```
Output
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor p
   Active: active (running) since Tue 2019-07-02 11:28:40 UTC; 15min ago
     Docs: https://docs.docker.com
 Main PID: 11911 (dockerd)
    Tasks: 10
   CGroup: /system.slice/docker.service
```
## Executing docker command without sudo

By default managing, Docker requires administrator privileges.

To run Docker commands as a non-root user without prepending  [`sudo`](https://linuxize.com/post/sudo-command-in-linux/)  you need to add your user to the  `docker`  group. This group is created during the installation of the Docker CE package. To do that run the following command:

```
$ sudo usermod -aG docker $USER
```

`$USER`  is an  [environment variable](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)  that holds your username.

Log out and log back in ti refresh the group membership.

To verify that Docker has been successfully installed and that you can run docker commands without prepending  `sudo`, run:

```
$ docker container run hello-world
```

The command will download a test image, run it in a container, print a “Hello from Docker” message and exit. The output should look like the following:

![Hello Docker Message](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Docker/1.jpg)

## Upgrading the Docker 

When a new Docker version is released you can update the package using the standard upgrade process:
```
$ sudo apt update
$ sudo apt upgrade
``` 
## Uninstalling the Docker

Before uninstalling Docker  [remove all containers, images, volumes, and networks](https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/).

You can uninstall Docker as any other package installed with  `apt`:

```
$ sudo apt purge docker-ce
$ sudo apt autoremove
```


##  Docker Command-Line Interface

The Docker CLI command takes this form:

```
$ docker [option] [subcommand] [arguments]
```

To list all available commands type  `docker`  with no parameters:

```
$ docker
```

If you need more help on any  `[subcommand]`, you can use the  `--help`  switch as shown below:

```
$ docker [subcommand] --help
```

##  Docker Images

A Docker image is made up of a series of filesystem layers representing instructions in the image’s  [Dockerfile](https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/)  that makes up an executable software application. An image is an immutable binary file including the application and all other dependencies such as libraries, binaries, and instructions necessary for running the application.

You can think of a Docker image as a snapshot of a Docker container.

Most Docker images are available on Docker Hub. The Docker Hub is cloud-based registry service which among other functionalities is used for keeping the Docker images in public or private repositories.

**Search Docker Image**
To search for an image from the Docker Hub registry, use the `search` subcommand.

For example, to search for an Ubuntu image, you would type:

```
$ docker search ubuntu
```
The output should look like this:

![Docker Search ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Docker/2.jpg)

As you can see, the search prints a table with five columns, `NAME`, `DESCRIPTION`, `STARS`, `OFFICIAL` and `AUTOMATED`.

The official image is an image that Docker develops in conjunction with upstream partners.

Most Docker images on Docker Hub are tagged with version numbers. When no tag is specified, Docker will pull the latest one.

**Docker Download Image**

For example, to download the latest official build of the Ubuntu 18.04 image, you would use the following `image pull` command:

    docker image pull ubuntu

![Docker Search ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Docker/3.jpg)

Depending on your Internet speed, the download may take a few seconds or minutes.

When not specifying a tag, Docker pulls the latest Ubuntu image, which at the time of writing this article is 18.04.

If you want to download a previous  [Ubuntu release](https://linuxize.com/post/how-to-check-your-ubuntu-version/), let’s say Ubuntu 16.04 then you need to use  `docker image pull ubuntu:16.04`.

To list all downloaded images type:


    docker image ls


The output will look something like this:

![Docker Search ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Docker/4.jpg)

### Remove Docker Image

If for some reasons, you want to delete an image, you can do that with the `image rm [image_name]` subcommand:

    docker image rm ubuntu
    
![Docker Search ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Docker/5.jpg)

#
## Docker Containers

An instance of an image is called a container. A container represents a runtime for a single application, process, or service.

It may not be the most appropriate comparison, but if you are a programmer, you can think of a Docker image as class and Docker container as an instance of a class.

We can start, stop, remove, and manage a container with the  `docker container`  subcommand.

### Start Docker Container

The following command will  [start a Docker container](https://linuxize.com/post/docker-run-command/)  based on the Ubuntu image. If you don’t have the image locally, it will download it first:

    docker container run ubuntu

At first sight, it may seem to you that nothing happened at all. Well, that is not true. The Ubuntu container stops immediately after booting up because it does not have a long-running process, and we didn’t provide any command. The container booted up, ran an empty command, and then exited.

The switch  `-it`  allows us to interact with the container via the command line. To start an interactive container type:
    
    docker container run -it ubuntu /bin/bash


    Output
    [root@719ef9304412 /]#
   
As you can see from the output above, once the container is started, the command prompt is changed. This means that you’re now working [from inside the container](https://linuxize.com/post/how-to-connect-to-docker-container/).

### List Docker Containers

To list active containers, type:

    docker container ls

![Docker Container List ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Docker/6.jpg)

To view both active and inactive containers, pass it the `-a` switch:

    docker container ls -a

![Docker Container List ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Docker/7.jpg)

### Remove Docker Containers
To delete one or more containers copy the container ID (or IDs) and paste them after the `container rm` subcommand:

    docker container rm c55680af670c

## Conclusion

You have learned how to install Docker on your Ubuntu 18.04 machine and how to download Docker images and manage Docker containers. You may also want to read about  [Docker Compose](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/), which allows you to define and run multi-container Docker applications.

This document barely scratches the surface of the Docker ecosystem. In some of our next articles, we will continue to dive into other aspects of Docker. To learn more about Docker check out the official  [Docker documentation](https://docs.docker.com/).



# Docker
This folder containers **Dockerfiles** that can be used to **build Docker container images** with respective names and function.
<br></br>
## commands and steps to build images:
- download Docker in your local machine
- open terminal and type the following command
- docker run dinesh1866/imagename 
> imagename is nay of the above folder name. eg: docker run dinesh1866/hello-world-py



## Introduction to Docker
- Docker is a tool designed to make it easier to create, deploy, and run applications by using containers.
- A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.
- A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.
- Available for both Linux and Windows-based applications, containerized software will always run the same, regardless of the infrastructure. Containers isolate software from its environment and ensure that it works uniformly despite differences for instance between development and staging.

## Docker Architecture
- Docker is made up of three components:
    - Docker Client
    - Docker Daemon
    - Docker Objects

### Docker Client
- The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

### Docker Daemon
- The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.

### Docker Objects
- Docker objects are the components that you use Docker to create and manage. Docker provides commands that let you create, load, list, run, stop, delete, and do other operations on these objects. The commands operate on Docker objects. For example, the docker run command runs a container from an image.

## Docker Engine
- The Docker Engine is a client-server application with these major components:
    - A server which is a type of long-running program called a daemon process (the dockerd command).
    - A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.
    - A command line interface (CLI) client (the docker command).

## Dockerfile
- A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession.

## Docker Image
- An image is an executable package that includes everything needed to run an application--the code, a runtime, libraries, environment variables, and configuration files.
- Images are used to execute code in Docker containers. When you run an image, Docker creates a read-only container with a set of standard attributes. You can then start, stop, move, or delete that container using the Docker API or CLI. You can also connect a container to one or more networks, attach storage to it, or create a new image based on its current state.

## Docker Container
- A container is a runtime instance of an image--what the image becomes in memory when executed (that is, an image with state, or a user process). You can run, start, stop, move, or delete a container using the Docker API or CLI. Just as you can create an image based on your current container, you can also create a new container based on an existing image.

## Docker Registry
- A registry is a storage and content delivery system, holding named Docker images, available in different tagged versions. The registry is a hosted service, which can be public or private, and the images in it can be public or private. The Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default.

## Docker Hub
- Docker Hub is a service provided by Docker for finding and sharing container images with your team. It is the world's largest library and community for container images. You can use Docker Hub to build, test, store, and distribute Docker images. You can also automate the build of Docker images based on code changes, and collaborate with other developers.

## Docker Compose
- Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration. To learn more about all the features of Compose see the list of features.

## Docker Machine
- Machine allows you to provision Docker on virtual hosts, and manage the hosts with docker-machine commands. A machine is made up of a Docker Engine, and a filesystem stored inside a virtual disk. You can use machine to create Docker hosts on your local Mac or Windows box, on your company network, in your data center, or on cloud providers like Azure, AWS, or Digital Ocean.

## Docker Swarm
- Docker Swarm is a native clustering tool for Docker. It turns a pool of Docker hosts into a single, virtual Docker host. Because Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts: dokku, fig, krane, flynn, deis, docker-ui, shipyard, drone, Jenkins... and, of course, the Docker client itself.

## Docker Datacenter
- Docker Datacenter (DDC) is a container management platform that enables enterprises to build, ship, and run any application, anywhere. Docker Datacenter is the only container platform that delivers a complete end-to-end solution for both IT operations and developers. Docker Datacenter is available as a software download or as a fully managed service.

## Docker Enterprise Edition
- Docker Enterprise Edition (Docker EE) is the industry’s most secure enterprise-grade platform for developing and managing modern applications. Docker EE is the only container platform that is certified for production environments, and is backed by Docker’s world-class support and services. Docker EE is available as a software download or as a fully managed service.

## Docker Desktop
- Docker Desktop is an application for MacOS and Windows machines for the building and sharing of containerized applications and microservices. Docker Desktop includes everything you need to build, run, and share containerized applications right from your machine. Docker Desktop replaces Docker Toolbox on Windows and legacy Docker Toolbox on MacOS systems.

## Docker Community Edition
- Docker Community Edition (Docker CE) is ideal for developers and small teams looking to get started with Docker and experimenting with container-based apps. Docker CE is available for Windows Server, Linux, and MacOS. Docker CE is free to use and easy to install. Docker CE is a great option if you’re new to Docker and containers, or if you’re looking to get started with Docker on a small project.

## Docker Store
- Docker Store is a marketplace and a delivery mechanism for trusted Docker content. It is the best place to find, buy, and manage commercial Docker solutions. Docker Store is the only place to find official Docker Certified Containers, Docker Certified Images, and Docker Certified Plugins. Docker Store is also the place to find Docker Certified Infrastructure (DCI) partners, who have been validated by Docker to provide a complete Docker solution.

## Docker Cloud
- Docker Cloud is a hosted and managed application delivery service that enables developers and IT ops teams to collaborate on application development, deployment, and management from development to production. Docker Cloud is a Docker Certified Infrastructure (DCI) partner, and is the only Docker Certified Infrastructure partner that offers a fully managed service.

## Docker Trusted Registry
- Docker Trusted Registry (DTR) is a hosted, highly scalable, and highly available private registry that stores and lets you distribute Docker images. Docker Trusted Registry is the only registry with image signing and role-based access control (RBAC) capabilities. Docker Trusted Registry is a Docker Certified Infrastructure (DCI) partner, and is the only Docker Certified Infrastructure partner that offers a fully managed service.

## Docker Universal Control Plane
- Docker Universal Control Plane (UCP) is a Docker Certified Infrastructure (DCI) partner, and is the only Docker Certified Infrastructure partner that offers a fully managed service. Docker UCP is a container management platform that enables enterprises to build, ship, and run any application, anywhere. Docker UCP is the only container platform that delivers a complete end-to-end solution for both IT operations and developers.

## Docker Datacenter Universal Control Plane
- Docker Datacenter Universal Control Plane (UCP) is a Docker Certified Infrastructure (DCI) partner, and is the only Docker Certified Infrastructure partner that offers a fully managed service. Docker Datacenter UCP is a container management platform that enables enterprises to build, ship, and run any application, anywhere. Docker Datacenter UCP is the only container platform that delivers a complete end-to-end solution for both IT operations and developers.

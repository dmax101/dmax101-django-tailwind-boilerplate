# Django Tailwind Boilerplate

## Introduction

This project is a initial check point allowing the developer start a ***Django*** project using the ***Tailwind CSS*** with the initial configuration, using the ***devcontainer*** configuration and ***Visual Studio Code***.

It was used the [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) documentation to reach this point.

Here you will find a docker compose file inside `.devcontainer` folder with instructions for docker to build 2 containers, one for the development and another to database Postgres. You can ignore the build of the database container editing the docker compose file according the [documentation](https://docs.docker.com/compose/).

## Requirements

* Python 3.8
* Node 18.12.1
* npm 8.19.2
* Docker

## Installation

### Preparing the installation

That project uses the ***devcontainer*** technology allowing you to isolate the application inside a container and for these purpose you have use the Visual Studio Code and to be sure the official Microsoft extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) is installed. To start the installation, **Docker** has to be running.

### Step 1

Clone the project and open it with **Visual Studio Code**

```sh
git clone https://github.com/dmax101/dmax101-django-tailwind-boilerplate.git

cd dmax101-django-tailwind-boilerplate

code .
```

### Step 2
Pressing `Ctrl + Shift + P` and typing `Remote-Containers: Reopen in Container` you will be able to start the installation.

That's it, you are ready to start your project.

## Usage

After the installation, you will be able to start the development server with the command `python manage.py runserver` and the application will be available at `http://localhost:8000`.

For more information about the ***Django-Tailwind***, please, check the [documentation](https://django-tailwind.readthedocs.io/en/latest/usage.html).

For more information about the Django framework, please visit the [official documentation](https://docs.djangoproject.com/en/3.2/).

For more information about how to use Tailwind CSS, please visit the [official documentation](https://tailwindcss.com/docs).

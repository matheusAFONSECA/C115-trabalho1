# C115 - Trabalho 1

Repository dedicated to storing and managing the first assignment for **C115 - Concepts and Technologies for Connected Devices**.

## Overview

This project demonstrates the implementation of an application that utilizes an API to handle requests made by a chatbot. The project is divided into two main components:

- **API**: Handles the responses to the requests made by the chatbot, built using `Flask`.
- **Frontend**: Manages the interaction between the user and the chatbot, developed using `Streamlit`.

The project is built using `Python 3.9`.

## Index
- [Cloning the Repository](#cloning-the-repository)
- [Running the Code Locally](#running-the-code-locally)
  - [Creating and Activating the Virtual Environment](#creating-and-activating-the-virtual-environment)
    - [1 - Using Commands](#1---using-commands)
    - [2 - Using a Script](#2---using-a-script)
  - [Installing the Requirements](#installing-the-requirements)
  - [Running python files](#running-python-files)
- [Running the Code with Docker](#running-the-code-with-docker)

## Cloning the Repository

To get started, clone this repository to your local machine. Run the following command in the directory where you want to save the repository:

```bash
git clone https://github.com/matheusAFONSECA/C115-trabalho1.git
```

## Running the Code Locally

### Creating and Activating the Virtual Environment

A Python interpreter must be previous installed on your machine to create and activate the virtual environment. There are two ways to set up the virtual environment:

#### 1 - Using Commands

To create a virtual environment in your repository, run the following command:

```bash
python -m venv C115venv
```

After creating the virtual environment, activate it with the following command:

```bash
.\C115venv\Scripts\activate
```

#### 2 - Using a script

Alternatively, you can use one of the scripts provided in the `scripts` directory to automate the setup:

- **Windows:**

```bash
.\scripts\create_and_activate_venv.ps1
```

- **Linux or macOS:**

```bash
./scripts/create_and_activate_venv.sh
```

### Installing the Requirements

Once the virtual environment is active, install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### Running python files

To run the application, you'll need to use two terminals:

- In the first terminal, activate the API by running:
```bash
python .\API\main.py
```
- In the second terminal, start the frontend interface by running:

```bash
streamlit run .\frontend\main.py
```

## Running the Code with Docker

An alternative way to run the project is by using Docker, which allows you to containerize the application and its dependencies. Docker ensures that the application runs consistently regardless of the environment it is deployed in.

To run the project using Docker, simply use the following command in the root directory of the project:

```bash
docker-compose up --build
```

This command will build the Docker images for both the API and the frontend, and then start the containers, making the application accessible as defined in the `docker-compose.yml` file.

> **Remember:** Make sure Docker is installed and the Docker Engine is running on your machine before attempting to use Docker commands.

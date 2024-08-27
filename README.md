# C115 - Trabalho 1

Repository dedicated to storing and managing the first assignment for **C115 - Concepts and Technologies for Connected Devices**.

## Overview

This project demonstrates the implementation of an application that utilizes an API to handle requests made by a chatbot. The project is divided into two main components:

- **API**: Handles the responses to the requests made by the chatbot, built using `Flask`.
- **Frontend**: Manages the interaction between the user and the chatbot, developed using `Streamlit`.

The project is built using `Python 3.9`.

## Index
- [Cloning the Repository](#cloning-the-repository)
- [Creating and Activating the Virtual Environment](#creating-and-activating-the-virtual-environment)
  - [1. Using Commands](#1---using-commands)
  - [2. Using a Script](#2---using-a-script)
- [Installing the Requirements](#installing-the-requirements)
- [Running the Code](#running-the-code)

## Cloning the Repository

To get started, clone this repository to your local machine. Run the following command in the directory where you want to save the repository:

```bash
git clone https://github.com/matheusAFONSECA/C115-trabalho1.git
```

## Creating and Activating the Virtual Environment

A Python interpreter must be previous installed on your machine to create and activate the virtual environment. There are two ways to set up the virtual environment:

### 1 - Using Commands

To create a virtual environment in your repository, run the following command:

```bash
python -m venv C115venv
```

After creating the virtual environment, activate it with the following command:

```bash
.\C115venv\Scripts\activate
```

### 2 - Using a script

Alternatively, you can use one of the scripts provided in the `scripts` directory to automate the setup:

- **Windows:**

```bash
.\scripts\create_and_activate_venv.ps1
```

- **Linux or macOS:**

```bash
./scripts/create_and_activate_venv.sh
```

## Installing the Requirements

Once the virtual environment is active, install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Running the code

To run the application, you'll need to use two terminals:

- In the first terminal, activate the API by running:
```bash
python .\API\main.py
```
- In the second terminal, start the frontend interface by running:

```bash
streamlit run .\frontend\main.py
```

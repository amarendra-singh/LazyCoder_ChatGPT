# Under Development
# LazyCoder_ChatGPT

LazyCoder ChatGPT is a chatbot that uses the GPT-3.5 architecture to provide intelligent and conversational responses to user input. This chatbot is built using OpenAI's GPT-3.5 API, and can be used to simulate conversations with a computer program.

# Table of Contents

* Features
* Prerequisites
* Getting Started
* Technologies Used
* Installation

# Features
* Provides intelligent and conversational responses to user input
* Uses GPT-3.5 architecture to simulate conversations with a computer program
* Built using OpenAI's GPT-3.5 API
* Written in Python

## Prerequisites
Before you can get started with the project, you'll need to have the following installed on your machine:

* Python
* PIP

## Technologies used
* Django
* OpenAI GPT-3.5 API
* TailWind CSS

## Getting Started
To get started with the project, simply clone or download the repository to your local machine and navigate to the directory where the repository is located. Then, run the following command in your terminal or command prompt:

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
        
* #### Dependencies
    1. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    2. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
    3. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```

# Portfolio Website

## Introduction

The Portfolio Website is a Python Flask application to host your portfolio.

## Technologies Used

1. Frontend - HTML, CSS, Javascript, Bootstrap
2. Backend - Python Flask

## Update Content.

* Update `data/index.json` to update the website's content.
* Update `static/images/profile_photo/me.jpg` and `static/images/profile_photo/favicon.png` with desired profile photo and favicon.
* Add skills photos under `static/images/skills`.

## Development Setup

1. Make sure `python3`, `pip3` and `virtualenv` are installed on the development setup.
2. Create a Python virtual environment using the command.
    ```bash
    virtualenv portfolio_env
    ```
3. Active the virtual environment using the command. 
    ```bash
    source portfolio_env/bin/activate
    ```
4. Install necessary Python packages using the command. 
    ```bash
    pip3 install -r requirements.txt
    ```
5. To run and debug the Flask app, run the command. 
    ```bash
    python3 debug.py
    ```
6. To test production wsgi, run the command.
    ```bash
    python3 run.py
    ```

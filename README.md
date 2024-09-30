# Portfolio Website

## Status
![Website Status](https://img.shields.io/website?url=https%3A%2F%2Fsashwat.in)
[![Dockerfile Build CI](https://github.com/sashuu69/portfolio-website/actions/workflows/docker-image.yml/badge.svg?branch=main)](https://github.com/sashuu69/portfolio-website/actions/workflows/docker-image.yml)
[![Pylint](https://github.com/sashuu69/portfolio-website/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/sashuu69/portfolio-website/actions/workflows/pylint.yml)

## Introduction

The Portfolio Website is a Python Flask application to host your portfolio.

## Technologies Used

1. Frontend - HTML, CSS, Javascript, Bootstrap
2. Backend - Python Flask

## Update Content.

* Update `data/index.json` to update the website's content.
* Update `static/images/profile_photo/me.jpg` and `static/images/profile_photo/favicon.png` with desired profile photo and favicon.
* Add skills photos under `static/images/skills`.
* Add testimonial profile photos under `static/images/testimonials`.
* Add portfolio project images under `static/images/portfolio`.

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
    ./runner.sh
    ```

## Other Info

If you face any bugs or want to request a new feature, please create an issue under the repository and provide appropriate labels respectively. If you want to do these by yourself, feel free to raise a PR and I will do what is necessary.

If you want to support me, donations will be helpful.



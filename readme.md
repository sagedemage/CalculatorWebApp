# Calculator Web Application

[![Production Workflow](https://github.com/sagedemage/CalculatorWebApp/actions/workflows/prod.yml/badge.svg)](https://github.com/sagedemage/CalculatorWebApp/actions/workflows/prod.yml)

[![Development Workflow](https://github.com/sagedemage/CalculatorWebApp/actions/workflows/dev.yml/badge.svg)](https://github.com/sagedemage/CalculatorWebApp/actions/workflows/dev.yml)


**The calculator web application is the program that
can do basic calculations for a user. 
The web application uses Flask, Jinja and Nginx.
Pandas is used for unit testing.** 

## Video Demonstration of my Calculator Web App
[https://www.youtube.com/watch?v=nUKfz3-4IQQ](https://www.youtube.com/watch?v=nUKfz3-4IQQ)

## Functionality of the Application
The user can do addition, subtraction, multiplication and division of 
two values. It also shows the result of the calculation and shows a 
table on the history of calculations. The user can clear the history 
of calculations if the user wants to.

## Setting up the docker container of the web applicaiton

Build the docker container:
````
docker-compose build
````

Start the docker container:
````
docker-compose up -d
````

To access the docker container shell:
````
docker exec -it $(docker ps -q) /bin/bash
````

## Unit testing the web application

Access the docker container shell:
````
docker exec -it $(docker ps -q) /bin/bash
````

Run pytest to test the web app
```
pytest
```

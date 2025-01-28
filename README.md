# Order Management System for E-commerce

A comprehensive API-based system for managing orders in e-commerce platforms, built with Python and FastAPI.

## Overview

This project provides a robust backend solution for handling orders, products, and delivery options in online stores. It features:

- RESTful API endpoints for CRUD operations on orders and products
- Flexible delivery option management
- User authentication using JWT tokens
- Database integration with PostgreSQL
- Asynchronous processing for improved performance

## Features

- Create, read, update, and delete orders
- Manage product catalog
- Set up and modify delivery options
- Track order status
- User registration and login
- Secure API access with JWT authentication

## Technology Stack

- Backend: Python 3.11, FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Migration Tool: Alembic
- Containerization: Docker, Docker Compose
- Authentication: JWT

to run it on your computer:
1) You need to clone it 'git clone https://github.com/Zofiant/ForYourStoreAPI/'
2) Install all dependencies with requirements.txt: `pip install -r ./requirements.txt`
3) Set up the environment variables: add .env with your database url and secret_key and algoritm!!
4) Run docker command `docker-compose -f docker-compose-local.yaml up -d`
5) Access the API documentation at `http://localhost:8000/docs`

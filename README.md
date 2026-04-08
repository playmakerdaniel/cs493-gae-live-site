# CS493 - Google App Engine Live Site

## 🌐 Live Site
https://cs493-live-site.appspot.com

## 📌 Overview
This project is a Python web application deployed on Google App Engine (GAE).
It demonstrates server-side interactivity using Flask.

The application allows a user to enter their name into a form, sends that data to the server, and returns a dynamically generated response.

## ⚙️ Features
- Server-side processing using Flask
- Form submission handled by backend (POST request)
- Dynamic response generation
- Deployed on Google App Engine
- Publicly accessible URL

## 🛠️ Tech Stack
- Python 3
- Flask
- Gunicorn
- Google App Engine

## 📂 Project Structure

gae_live_site/
│
├── main.py
├── app.yaml
├── requirements.txt
└── README.md

## 🚀 How It Works
1. User accesses the homepage
2. User enters their name in a form
3. Form sends a POST request to the server
4. Server processes the request
5. Server returns a personalized greeting

## 🧪 Example Interaction

Input:
Name: Daniel

Output:
Hello, Daniel! Your request was processed by the server.

## ☁️ Deployment
gcloud app deploy

## 👤 Author
Daniel Burrows



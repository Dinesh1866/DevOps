# Path: DevOps\Programming_Questions\api.py
'''There are five classes running in a school (e.g., class A, class B, class C, class D and class E). Each class
has many students. Every class includes five subjects (for example, math, English, Hindi, science, and computer). Each student can choose their own subject, but at least one subject must be chosen'''

# conditions
# 1. Create a login API for students that returns an authentication token and other API responses based on this token
'''2. Create an API to register student data 
Request body: - 
{ 
 "student_name": "John Smith", 
 "class_id":2, 
 "email": "johnsmith@gmail.com", 
 "password": "343r5$", 
 "subject":[1,2] 
} '''

#3. Create an API to update the above details as well.

'''4.  Create an API which fetch the data from database and response as :- 
{ 
 "student_id": 1, 
 "student_name": "John Smith", 
 "email": "johnsmith@gmail.com", 
 "class_id":2, 
 "class": "class B", 
 "subject": ["Math", "English"] 
}'''

#start coding
# import libraries
import json
import requests
import random
import string
import sqlite3
import datetime
import time
import os
import sys
import re
import hashlib
import base64
import hmac
import urllib
import urllib.parse
import urllib.request
import urllib.error

# create a class
class Student:
      # create a constructor
      def __init__(self, student_name, class_id, email, password, subject):
            self.student_name = student_name
            self.class_id = class_id
            self.email = email
            self.password = password
            self.subject = subject
            self.token = None
      
      # create a method to register student data
      def register_student(self):
            # create a dictionary
            student_data = {
                  "student_name": self.student_name,
                  "class_id": self.class_id,
                  "email": self.email,
                  "password": self.password,
                  "subject": self.subject
            }
            # create a variable to store the url
            url = "http://"
            # create a variable to store the headers
            headers = {
                  "Content-Type": "application/json"
            }
            # create a variable to store the response
            response = requests.post(url, headers=headers, data=json.dumps(student_data))
            # return the response
            return response

      # create a method to update the student data
      def update_student(self):
            # create a dictionary
            student_data = {
                  "student_name": self.student_name,
                  "class_id": self.class_id,
                  "email": self.email,
                  "password": self.password,
                  "subject": self.subject
            }
            # create a variable to store the url
            url = "http://"
            # create a variable to store the headers
            headers = {
                  "Content-Type": "application/json"
            }
            # create a variable to store the response
            response = requests.put(url, headers=headers, data=json.dumps(student_data))
            # return the response
            return response

      # create a method to fetch the student data
      def fetch_student(self):
            # create a variable to store the url
            url = "http://"
            # create a variable to store the headers
            headers = {
                  "Content-Type": "application/json"
            }
            # create a variable to store the response
            response = requests.get(url, headers=headers)
            # return the response
            return response

# create a class
class Login:
      # create a constructor
      def __init__(self, email, password):
            self.email = email
            self.password = password
            self.token = None
      
      # create a method to generate token
      def generate_token(self):
            # create a variable to store the url
            url = "http://"
            # create a variable to store the headers
            headers = {
                  "Content-Type": "application/json"
            }
            # create a dictionary
            data = {
                  "email": self.email,
                  "password": self.password
            }
            # create a variable to store the response
            response = requests.post(url, headers=headers, data=json.dumps(data))
            # return the response
            return response

# create a class
class Subject:
      # create a constructor
      def __init__(self, subject_id, subject_name):
            self.subject_id = subject_id
            self.subject_name = subject_name
      
      # create a method to fetch the subject data
      def fetch_subject(self):
            # create a variable to store the url
            url = "http://"
            # create a variable to store the headers
            headers = {
                  "Content-Type": "application/json"
            }
            # create a variable to store the response
            response = requests.get(url, headers=headers)
            # return the response
            return response

# create a class
class Class:
      # create a constructor
      def __init__(self, class_id, class_name):
            self.class_id = class_id
            self.class_name = class_name
      
      # create a method to fetch the class data
      def fetch_class(self):
            # create a variable to store the url
            url = "http://"
            # create a variable to store the headers
            headers = {
                  "Content-Type": "application/json"
            }
            # create a variable to store the response
            response = requests.get(url, headers=headers)
            # return the response
            return response

# create a class
class StudentSubject:
      # create a constructor
      def __init__(self, student_id, subject_id):
            self.student_id = student_id
            self.subject_id = subject_id
      
      # create a method to fetch the student subject data
      def fetch_student_subject(self):
            # create a variable to store the url
            url = "http://"
            # create a variable to store the headers
            headers = {
                  "Content-Type": "application/json"
            }
            # create a variable to store the response
            response = requests.get(url, headers=headers)
            # return the response
            return response

            

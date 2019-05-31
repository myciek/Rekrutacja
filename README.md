# Chapter I : Exam API

## Installation:
- clone repository
- move to the repo direction
- run setup.sh (It will build compose, populate database and run tests)
- now you can write ```docker-compose up``` in console to start to run app

## Endpoints:
- ```/exercises/```
- ```/possible_answers/```
- ```/exams/```
- ```/answer_sheets/```
- ```/answers/```

You can get details of objects of all endpoints using ```/endpoint/pk``` and PUT/DELETE in the same adress if you are owner.

Exercise,exams and answer sheets can be filtred. Use ```/endpoint?field_name=value```

Log in with one of created users(password is same as username):
- admin
- teacher1
- teacher2
- student

# Chapter II: Programing tasks
Files are located in ```chapterII``` directory. 
- skyphrases.py - task 1 code
- jsons.py - task 2 code
- answers.txt - answers to both tasks

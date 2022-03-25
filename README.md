# Hospital-Management
This repository is designed to handle real-time hospital data service.
It includes a database management system and a set of API to handle it.
The project has been deployed on Amazon EC2 server, with Flask APP and MongoDB running seperately.
Now pushed to EC2 server http://34.238.84.218:8000/
**THERE IS STILL NOT A STABLE VERSION OF THIS SYSTEM, IF YOU ARE STILL INTERESTED PLEASE CHECK DEV BRANCH**

## Content
- [Hospital-Management](#hospital-management)
  - [Content](#content)
  - [Version 0.0.6](#version-006)
  - [Setup](#setup)
    - [Requirement](#requirement)
  - [How to use](#how-to-use)
  - [Query Syntax](#query-syntax)
  - [Database](#database)
  - [Data Fields](#data-fields)
  - [User Stories](#user-stories)
  - [Branching Strategy](#branching-strategy)
  - [Unit Test](#unit-test)

## Version 0.0.6
Updated Speech to Text module, now in chat module, when user upload a wav format conversation, the server can transform it into text and store in database.

## Setup
### Requirement
- Check [requirements.txt](requirements.txt)
## How to use
- Local
  - Run hospital.db first, then post request to http://127.0.0.1:5000/CollectionName (if local), or use test_api to check if the local server is running correctly (make sure test_api.py is set to local mode).
- Remote 
  - Post request to http://34.238.84.218:8000/"CollectionName" (my server), or use test_api to check if the local server is running correctly.

## Query Syntax
- GET
  - Directly access `site_url = http://34.238.84.218:8000/CollectionName` is considered as get command and will return the whole collection as json file. 
  - Get method in python request package can also perform the get query.
  - Example code: 
    ```python
    request.get(site_url)
    ```
- POST
  - Post method in python request package can post data. 
  - Example code: 
    ``` python
    requests.post(site_url, postdata)
    ```
- PUT
  - Put method in python request package can put data.
  - Example code:
    ``` python
    request.put(site_url, putdata)
    ```
- DELETE
  - Use requests.request('DELETE', delete_url) to apply the delete.
    Where the delete_url is made of [site_url + "?id="Your_ID"]
  - Example code:
    ``` python
    request.request('DELETE', site_url + "?id="Your_ID")
    ```

## Database
This project use MongoDB as database.
An API for MongoDB is implemented to control MongoDB queries, check [mongo_api.py](module/database_api/mongo_api.py) for more information.

## Data Fields
Check the ERD:  Hospital DB:  
![image](Hospital%20DB.png)

## User Stories
- Patient:
  - upload basic info
  - check test data of themselves
    - data
    - staff in charge
    - time
    - date
    - device info
  - check where to do the test
- Staff
  - know which patient to treat
  - check test datas of their patient
    - medical history (previous data)
    - patient info
    - time
    - date
    - device info
- Device company
  - interface to inject data from device
- Admin
  - add user
  - change user catagories
    - patient
    - staff
      - doctor
      - nurse
      - title
    - admin


## Branching Strategy
- Main:     A stable release of the system.
- Dev:      A in-developing version of system, unstable. Will bidirectionally integrated with main.
- Hotfix    A of emergency bug fixes. 



## Unit Test
This project use bottom-up unit test method. The unit test is designed to test all function in the module. Unit test can be found at test_api.py.


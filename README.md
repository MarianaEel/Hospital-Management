# Hospital-Management
This repository is designed to handle real-time hospital data service.
It includes a database management system and a set of API to handle it.
Now pushed to EC2 server http://34.238.84.218:8000/
**THERE IS STILL NOT A STABLE VERSION OF THIS SYSTEM, IF YOU ARE STILL INTERESTED PLEASE CHECK DEV BRANCH**

## Content
- [Hospital-Management](#hospital-management)
  - [Content](#content)
  - [Setup](#setup)
    - [Requirement](#requirement)
  - [How to use](#how-to-use)
  - [Query Syntax](#query-syntax)
  - [Database](#database)
  - [Server](#server)
  - [User Stories](#user-stories)
  - [Branching Strategy](#branching-strategy)
  - [Data Fields](#data-fields)
  - [Unit Test](#unit-test)
  - [File Structure](#file-structure)

## Setup
### Requirement

## How to use
- Local
  - Run hospital.db first, then post request to http://127.0.0.1:5000/CollectionName (if local), or use test_api to check if the local server is running correctly (make sure test_api.py is set to local mode).
- Remote 
  - Post request to http://34.238.84.218:8000/"CollectionName" (my server), or use test_api to check if the local server is running correctly.

## Query Syntax
- GET
  - Directly access http://34.238.84.218:8000/CollectionName is considered as get command and will return the whole collection as json file. 
  - Get method in python request package can also perform the get query, use it like 
  - ```python
    request.get(url)
    ```
- POST
  - Post method in python request package can post data. Use it like "requests.post(url, postdata)"
- PUT
  - Put method in python request package can put data.
- DELETE
  - d

## Database
This project use MongoDB as database.

## Server
The project has been deployed on Amazon EC2 server, with Flask APP and MongoDB running seperately.

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

## Data Fields
Check the ERD:  Hospital DB:  
![image](Hospital%20DB.png)

## Unit Test
This project use bottom-up unit test method. The unit test is designed to test all function in the module. Unit test can be found at test_api.py.


## File Structure
│  Hospital DB.png  
│  hospital_db.py  
│  README.md  
│  requirements.txt  
│  test_api.py  
│  
├─data  
│      datas.csv  
│      fac_product.json  
│      patients.csv  
│      staffs.csv  
│  
├─module  
│  │  __init__.py  
│  │  
│  └─user_management   
│     │  management_api.py    
│     │  management_factory.py    
│     └─ __init__.py  
│  
└─test  
       testoutcome.txt  
       testfile.json  

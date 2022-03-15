# Hospital-Management
This repository is designed to handle real-time hospital data service.
It includes a database management system and a set of API to handle it.
**THERE IS STILL NOT A STABLE VERSION OF THIS SYSTEM, IF YOU ARE STILL INTERESTED PLEASE CHECK DEV BRANCH**

## Content
- [Hospital-Management](#hospital-management)
  - [Content](#content)
  - [Setup](#setup)
    - [Requirement](#requirement)
    - [How to use](#how-to-use)
  - [User Stories](#user-stories)
  - [Branching Strategy](#branching-strategy)
  - [Data Fields](#data-fields)
  - [Unit Test](#unit-test)
  - [File Structure](#file-structure)

## Setup
### Requirement

### How to use
- Local
  - Run hospital.db first, then post request to http://127.0.0.1:5000/ (if local), or use test_api to check if the local server is running correctly.

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
This project use bottom-up unit test method. The unit test is designed to test all function in the module.

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

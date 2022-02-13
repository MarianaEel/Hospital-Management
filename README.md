# Hospital-Management
This repository is designed to handle real-time hospital data service.
It includes a database management system and a set of API to handle it.
**THERE IS STILL NOT A STABLE VERSION OF THIS SYSTEM, IF YOU ARE STILL INTERESTED PLEASE CHECK DEV BRANCH**

## Content
- [Hospital-Management](#hospital-management)
  - [Content](#content)
  - [User Stories](#user-stories)
  - [Branching Strategy](#branching-strategy)
  - [Data Fields](#data-fields)
  - [File Structure](#file-structure)
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
Check the ERD:  Hospital DB - ERD with colored entities (UML notation)

## File Structure
|   Hospital DB - ERD with colored entities (UML notation).pdf  
|   Hospital DB - ERD with colored entities (UML notation).png  
|   hospital_db.py  
|   README.md  
|   requirements.txt  
|  
+---module  
|   \---user_management  
|   |       add_user.py  
|
+---test  
|       testfile.txt  
\       test_user.py  

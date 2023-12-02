## Overview
Create a simple python progame (using Fastapi) where user can upload the csv file and it will create a sqlite db where those csv data can upload into database.

## Project Structure
- **run.py:** The main FastAPI application file.
- **req.txt:** all required library in this file.

  ### Installation

1. Clone the repository:
    git clone git@github.com:singh-admin/upload_csv_file.git
   
3. Create the python virtual environment.
    python -m venv env
   
4. Activate the virtual environment.
    env\Scripts\activate

5. Install dependencies:
    pip install -r req.txt

### Running the Application
    python run.py

Result:
once application run http://127.0.0.1:8000/ visit the url will get minimal html page and you can drop the csv file and submit after submition csv.db file will create where whatever the data is present in csv with those data it will create a rows in csv_data table. 
![image](https://github.com/singh-admin/upload_csv_file/assets/61795935/5dae9b73-4161-472e-b735-be8bc6cbef85)


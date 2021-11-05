1. Create virtual environment using below command
python -m venv petltestdemo

2. Once created the environment activate it.
cd scripts
activate

3. Go to root folder and open the folder in VisualStudio with below command
code .

4. Run below command to install the python lirbaries as needed for the process.

pip  install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  -r requirements.txt

5. Create a database and table with user and permissions on SQLServer mentioned in DeoDBDDL.sql file

6. Update the ini file for the ETL process as needed.

7. Check the API call 

8. Develop the application python code using petl lirbary for ETL process and run it to import data from api to SQLServer table created.

9. Check the csv file imported from api.

10. check the exported data from csv to SQLServer.

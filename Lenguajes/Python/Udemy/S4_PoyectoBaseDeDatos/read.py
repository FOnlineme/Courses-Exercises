from pymongo import MongoClient
# creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

# function to read data into mongo db
def read():
    try:
        empcol = db.Employees.find()
        print('\n All data from EmployeeData Database \n')
        for emp in empcol:
            print(emp)
            
    except ImportError:
        platform_specific_module = None
        # print str(e)
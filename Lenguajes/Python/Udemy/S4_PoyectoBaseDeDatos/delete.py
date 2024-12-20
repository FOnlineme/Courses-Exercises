from pymongo import MongoClient
# creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

# function to delete data into mongo db
def delete():
    try:
        criteria = input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id": criteria})
        print('\nDeletion successfully\n')
    
    except ImportError:
        platform_specific_module = None
        # print str(e)
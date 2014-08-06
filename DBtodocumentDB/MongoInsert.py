__author__ = 'rohit'
from pymongo import MongoClient

def construct_record(rows):
    '''Constructs the JSON structure for the MongoDB document'''
    dict = {}
    dict_list = []
    for record in rows:
        p_number,p_name,d_name,f_name,l_name,hours = record

        if len(dict)==0:#initial record
            dict['pnumber'] = p_number
            dict['pname'] = p_name
            dict['dname'] = d_name
            dict['employees'] = [{'fname':f_name,'lname':l_name,'hours':str(hours)}]
        elif dict['pnumber']!=p_number:#new record
            dict_list.append(dict)
            dict = {}
            dict['pnumber'] = p_number
            dict['pname'] = p_name
            dict['dname'] = d_name
            dict['employees'] = [{'fname':f_name,'lname':l_name,'hours':str(hours)}]
        elif dict['pnumber']== p_number:#new employee
            employee_list = dict['employees']
            employee_list.append({'fname':f_name,'lname':l_name,'hours':str(hours)})
            dict['employees'] = employee_list

    return dict_list#returns the target JSON structure abstracted in a list

def insert_record(dict_record):
    '''Inserts a record into MongoDB'''
    connection = MongoClient("localhost")#establishes connection
    db = connection.COMPANY.projects#connects to the collection
    #inserts the record
    db.insert(dict_record)
    # close the connection to MongoDB
    connection.close()







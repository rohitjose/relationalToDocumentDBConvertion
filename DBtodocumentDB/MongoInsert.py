__author__ = 'rohit'
from pymongo import MongoClient

def construct_project_record(rows):
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

def construct_department_record(records):
    '''Constructs the JSON structure for the MongoDB document'''
    dict = {}
    dict_list = []
    for record in records:
        d_number,d_name,l_name,location = record

        if len(dict)==0:#initial record
            dict['dnumber'] = d_number
            dict['dname'] = d_name
            dict['lname'] = l_name
            dict['location'] = [location]
        elif dict['dnumber']!=d_number:#new record
            dict_list.append(dict)
            dict = {}
            dict['dnumber'] = d_number
            dict['dname'] = d_name
            dict['lname'] = l_name
            dict['location'] = [location]
        elif dict['dnumber']== d_number:#new location
            location_list = dict['location']
            location_list.append(location)
            dict['location'] = location_list

    return dict_list#returns the target JSON structure abstracted in a list

def insert_record_department(dict_record):
    '''Inserts a record into MongoDB'''
    connection = MongoClient("localhost")#establishes connection
    db = connection.COMPANY.department#connects to the collection
    #inserts the record
    db.insert(dict_record)
    # close the connection to MongoDB
    connection.close()







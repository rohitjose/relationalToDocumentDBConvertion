__author__ = 'rohit'
import MongoInsert
import AccessSQL

if __name__=='__main__':
    #retrieves the rows of the MySQL DB
    rows = AccessSQL.accessSQL("select p.pnumber,p.pname, d.dname, e.fname,e.lname,w.hours \
    from PROJECT p , DEPARTMENT d , WORKS_ON w, EMPLOYEE e \
    where p.dnum=d.dnumber and p.pnumber=w.pno and w.essn=e.ssn \
    order by p.pnumber")
    #Constructs the target JSON structure
    dicts = MongoInsert.construct_record(rows)
    # Loop for insertion into Mongo DB
    for item in dicts:
        MongoInsert.insert_record(item)
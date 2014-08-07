__author__ = 'rohit'
import MongoInsert
import AccessSQL

def projects():
    #retrieves the rows of the MySQL DB
    rows = AccessSQL.accessSQL("select p.pnumber,p.pname, d.dname, e.fname,e.lname,w.hours \
    from PROJECT p , DEPARTMENT d , WORKS_ON w, EMPLOYEE e \
    where p.dnum=d.dnumber and p.pnumber=w.pno and w.essn=e.ssn \
    order by p.pnumber")
    #Constructs the target JSON structure
    dicts = MongoInsert.construct_project_record(rows)
    # Loop for insertion into Mongo DB
    for item in dicts:
        MongoInsert.insert_record(item)

def department():
    rows = AccessSQL.accessSQL("SELECT D.Dnumber,D.DName, E.Lname, L.Dlocation \
    FROM DEPARTMENT D, EMPLOYEE E, DEPT_LOCATIONS L \
    WHERE D.Mgr_ssn = E.Ssn AND  D.Dnumber=L.Dnumber \
    ORDER BY D.Dnumber")

    dicts = MongoInsert.construct_department_record(rows)

    for item in dicts:
        MongoInsert.insert_record_department(item)


if __name__=='__main__':
    projects()


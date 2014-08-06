__author__ = 'rohit'
import MySQLdb

def accessSQL(query):
    '''Function to access data from the MySQL DB'''
    # Connect to the MySQL database
    db = MySQLdb.connect(host = 'localhost', user = 'root', \
    passwd = 'jose', db = 'company')

    # Creation of a cursor
    cursor = db.cursor()
    # Execution of a SQL statement
    cursor.execute(query)
    # Get the total number of rows
    numrows = int (cursor.rowcount)
    records = []
    #appends each tuple into a list - records
    for i in range (numrows):
        row = cursor.fetchone()
        if (row):
            records.append(row)
    db.close()
    return records # returns the list of tuples

if __name__=='__main__':
    rows = accessSQL("select p.pnumber,p.pname, d.dname, e.fname,e.lname,w.hours \
    from PROJECT p , DEPARTMENT d , WORKS_ON w, EMPLOYEE e \
    where p.dnum=d.dnumber and p.pnumber=w.pno and w.essn=e.ssn \
    order by p.pnumber")
    print rows


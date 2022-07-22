
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "123456789suraj",
    database="employeedata"
)
#creating employee and department table
cursor = db.cursor()

cursor.execute("CREATE TABLE Employee (EmployeeID INT NOT NULL, FirstName VARCHAR(100) NOT NULL, MiddleName VARCHAR(100) NULL,LastName VARCHAR(100) NOT NULL, Joindate DATE NULL ,MonthlySalary FLOAT NULL, DeptID INT PRIMARY KEY NOT NULL)")

cursor.execute("CREATE TABLE Department (DeptID INT NOT NULL, DeptName VARCHAR(100) NOT NULL, DeptCode VARCHAR(100) NULL, ParentDeptID VARCHAR(100) NOT NULL, ManagerID INT NULL, Description TEXT NULL, Active BOOLEAN NOT NULL)"
#Write a Single Query to find the Total Earnings by Employees grouped by Departments.
cursor.execute("SELECT  DATEDIFF(MONTH,CURDATE(),JoinDate)*Monthsalary from Employee group by Department with DeptID")
#Write a Single Query to find the list of Employees belonging to Department Sales, with servic length of more than 6 months.
cursor.execute("SELECT * FROM Department WHERE DeptName='Sales' AND DATEDIFF(MONTH,CURDATE(),JoinDate)>6")
# Write a Single Query to list Employees with their Department Name and their Manager Name.
cursor.execute("SELECT e.EmployeeID,e.FirstName,e.MiddleName,e.LastName,e.joinDate,e.Monthsalary, d.DeptName FROM Employee e, Department d WHERE e.DeptID=d.DeptID AND DeptName="manager"")
class Department:
    count_of_dept=0
    def __init__(self,dept_Id,dept_name,location):
        self.dept_Id=dept_Id
        self.dept_name=dept_name
        self.location=location
        Department.count_of_dept+=1
    def department_info(self):
        print("Department details")
        print("----------------")
        print(f"Department id:{self.dept_Id}")
        print(f"Department name:{self.dept_name}")
        print(f"location :{self.location}")
    @classmethod
    def total_department(cls):
        return cls.count_of_dept
    
    @staticmethod
    def search_by_id(departments,search_id):
        for dept in departments:
            if dept.dept_Id==search_id:
                print("department found by id")
                dept.department_info()
                return
        print("department id not found")    

    @staticmethod
    def search_by_name(departments,search_name):
        for dept in departments:
            if dept.dept_name==search_name:
                print("department found by name")
                dept.department_info()
                return
        print("Invalid department name")    
    


num=int(input("enter no of departments"))
departments=[]
for i in range(num):
    print(f"\nEnter the details of department {i+1}")
    dept_id=int(input("Enter the department id"))
    dept_name=input("Enter Department name")
    location=input("Enter the location")

    dept=Department(dept_id,dept_name,location)
    departments.append(dept)

    for depts in departments:
        print(depts.department_info())

print(f"Total departments ={Department.count_of_dept}") 


while True:
    print("Search options:")
    print("1.search by department Id")
    print("2.Searc by department")
    choice =int(input("enter the choice") )
    if choice ==1:
        search_id=int(input("Enter the department id"))
        Department.search_by_id(departments,search_id)
        break
    elif(choice==2):
        search_name=input("Enter the department name")
        Department.search_by_name(departments,search_name)
        break
    else:
        print("Invalid choice")
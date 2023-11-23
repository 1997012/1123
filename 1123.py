class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name  # 員工姓名
        self.emp_id = emp_id  # 員工編號
        self.emp_salary = emp_salary  # 員工薪水
        self.emp_department = emp_department  # 員工部門

    def emp_assign_department(self, new_department):
        self.emp_department = new_department
        print(f"{self.emp_name}的部門已更改為{new_department}。")

    def print_employee_details(self):
        print(f"員工姓名：{self.emp_name}")
        print(f"員工編號：{self.emp_id}")
        print(f"員工薪水：${self.emp_salary}")
        print(f"員工部門：{self.emp_department}")
        print("\n")

    def calculate_emp_salary(self, hours_worked):
        base_salary = self.emp_salary
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            overtime_amount = (overtime_hours * (base_salary / 50))
            total_salary = base_salary + overtime_amount
            print(f"{self.emp_name}加班了。加班費已加入薪水。")
            print(f"基本薪水：${base_salary}")
            print(f"加班費：${overtime_amount}")
            print(f"總薪水：${total_salary}")
        else:
            total_salary = base_salary
            print(f"{self.emp_name}本月薪水。")
            print(f"總薪水：${total_salary}")

# 範例員工資料
employees = [
    Employee("ADAMS", "E7876", 50000, "會計部"),
    Employee("JONES", "E7499", 45000, "研究部"),
    Employee("MARTIN", "E7900", 50000, "銷售部"),
    Employee("SMITH", "E7698", 55000, "運營部")
]

# 示範使用
for emp in employees:
    emp.print_employee_details()
    emp.calculate_emp_salary(55)  # 假設工作了55小時
    emp.emp_assign_department("人力資源部")  # 分配新的部門
    emp.print_employee_details()

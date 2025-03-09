from payroll.employee import FullTimeEmployee, ContractEmployee

if __name__ == "__main__":
    emp1 = FullTimeEmployee(1,480000,12000)
    emp2 = FullTimeEmployee(2,4800000,120000)
    print(emp1.calculate_monthly_salary(0))
    print(emp2.calculate_monthly_salary(0))
    emp3 = ContractEmployee(3, 360000)
    emp4 = ContractEmployee(4, 720000)
    print(emp3.calculate_monthly_salary())
    print(emp4.calculate_monthly_salary())



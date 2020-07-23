import uuid

from datetime import datetime, date

from rest_framework import serializers

from .constants import EmployeeTypes


class Employee(object):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired,
                 is_best_employee=None, last_name=None
                 ):

        self.employee_id = employee_id                  # UUID
        self.age = age                                  # INT
        self.date_of_joining = date_of_joining          # DATE
        self.last_logged_in = last_logged_in            # DATETIME
        self.salary_in_inr = salary_in_inr              # FLOAT
        self.employee_type = employee_type              # ENUM - Possible values MANAGER,TECHNICIAN,DEVELOPER,SALES_MEMBER 
        self.first_name = first_name                    # CHAR
        self.last_name = last_name                      # CHAR
        self.is_retired = is_retired                    # BOOL
        self.is_best_employee = is_best_employee        # BOOL - Can be None as welcl


class EmployeeSerializer(serializers.Serializer):

    employee_id = serializers.UUIDField()
    age = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    last_logged_in = serializers.DateTimeField()
    salary_in_inr = serializers.FloatField()
    employee_type = serializers.ChoiceField(
        choices=[
            employee_type.value for employee_type in EmployeeTypes
            ]
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField(
        allow_null=True, required=False
    )
    is_retired = serializers.BooleanField()
    is_best_employee = serializers.NullBooleanField(
        required=False
    )


    def create(self, validated_data):
        return Employee(**validated_data)


class Company(object):

    def __init__(self, name, registration_id):
        self.name = name                                # CHAR
        self.registration_id = registration_id          # UUID


class CompanySerializer(serializers.Serializer):

    name = serializers.CharField()
    registration_id = serializers.UUIDField()
    
    def create(self, validated_data):
        return Company(**validated_data)



class EmployeeWithCompanyDetails(Employee):

    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired, company,
                 is_best_employee=None, last_name=None):

        super().__init__(employee_id, age, date_of_joining, last_logged_in,
                         salary_in_inr, employee_type, first_name, is_retired,
                         is_best_employee, last_name)

        self.company = company                          # Company class instance 


class EmployeeWithCompanyDetailsSerializer(EmployeeSerializer):
    company=CompanySerializer()

    def create(self, validated_data):
        company_data= validated_data.pop('company')
        company_inst = Company(**company_data)
        
        employee_with_company_details = EmployeeWithCompanyDetails(
            company=company_inst, **validated_data)
    
        return employee_with_company_details



class CompanyWithEmployeesDetails(Company):

    def __init__(self, name, registration_id, employees):
        super().__init__(name, registration_id)
        self.employees = employees                      # List of Employee class instances 


class CompanyWithEmployeeDetailsSerializer(CompanySerializer):
    employees = EmployeeSerializer(many=True)

    def create(self, validated_data):

        employees_data_list = validated_data.pop('employees')
        serializer = EmployeeSerializer(data=employees_data_list, many=True)
        serializer.is_valid()
        employees = serializer.save()
        company_with_employees_details = CompanyWithEmployeesDetails(
            employees=employees, **validated_data)

        return company_with_employees_details




# creating data 
def create_employee():
    employee=Employee(
        employee_id=uuid.uuid4(),
        age=10,
        date_of_joining=date.today(),
        last_logged_in=datetime.now(),
        salary_in_inr=10.0,
        employee_type=EmployeeTypes.MANAGER.value,
        first_name='steve jobs',
        last_name='chirathala',
        is_retired=False,
        is_best_employee=False
        )
    return employee


def create_company():
    company = Company(
        name = 'sulthan babu',
        registration_id = uuid.uuid4()
        )
    return company


def create_employee_with_company_details():
    emp_with_comp_det = EmployeeWithCompanyDetails(
        employee_id=uuid.uuid4(),
        age=10,
        date_of_joining=date.today(),
        last_logged_in=datetime.now(),
        salary_in_inr=10.0,
        employee_type='MANAGER',
        first_name='steve jobs',
        last_name='chirathala',
        is_retired=False,
        is_best_employee=False,
        
        company=create_company()
        )

    return emp_with_comp_det




#  function section

# Task - 1
def serialize_employee_object(employee_object):

    serialized_obj = EmployeeSerializer(employee_object)
    serialized_obj_to_dict = serialized_obj.data
    return serialized_obj_to_dict


# Task - 2 
def deserialize_data_to_employee_object(employee_data):

    serialized_dict_to_obj = EmployeeSerializer(data=employee_data)
    is_validated_data= serialized_dict_to_obj.is_valid()

    if is_validated_data:
        return serialized_dict_to_obj.save()
    else:
        return serialized_dict_to_obj.errors


# Task - 3
def serialize_list_of_employee_objects(list_of_employee_objects):

    serialized_objs = EmployeeSerializer(
        list_of_employee_objects, many=True
    )
    serialized_objs_to_dicts_list = serialized_objs.data
    return serialized_objs_to_dicts_list


# Task - 4
def deserialize_data_to_list_of_employee_objects(employees_data):

    serialized_dicts_to_objs = EmployeeSerializer(
        data=employees_data, many=True
    )
    is_validated_data= serialized_dicts_to_objs.is_valid()

    if is_validated_data:
        return serialized_dicts_to_objs.save()
    else:
        return serialized_dicts_to_objs.errors


# Task - 5
def serialize_employee_with_company_object(employee_with_company_object):

    serializer_obj = EmployeeWithCompanyDetailsSerializer(
        employee_with_company_object
    )
    serialized_obj_to_dict = serializer_obj.data
    return serialized_obj_to_dict


# Task - 6
def deserialize_data_to_employee_with_company_object(
        employee_with_company_data
):

    serialized_dict_to_obj = EmployeeWithCompanyDetailsSerializer(
        data=employee_with_company_data
    )
    is_validated_data= serialized_dict_to_obj.is_valid()

    if is_validated_data:
        return serialized_dict_to_obj.save()
    else:
        return serialized_dict_to_obj.errors


# Task - 7
def serialize_company_with_employees_object(company_with_employees_object):

    serialized_obj = CompanyWithEmployeeDetailsSerializer(
        company_with_employees_object
    )
    serialized_obj_to_dict = serialized_obj.data
    return serialized_obj_to_dict


# Task - 8
def deserialize_data_to_company_with_employees_object(
        company_with_employees_data
):

    serialized_dict_to_obj = CompanyWithEmployeeDetailsSerializer(
        data=company_with_employees_data
    )
    is_validated_data= serialized_dict_to_obj.is_valid()

    if is_validated_data:
        return serialized_dict_to_obj.save()
    else:
        return serialized_dict_to_obj.errors

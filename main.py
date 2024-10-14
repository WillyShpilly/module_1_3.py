# x = str(7)
# y = str(6)
#
# result = x + y
# print(result)

# class Employee:
#     def __init__(self, employee_id: str, salary: float):
#         self.employee_id: str = employee_id
#         self.salary: float = salary

# class Circle:
#     def __init__(self, radius: float):
#         self.radius: float = radius
#
#     def area(self) -> float:
#         return 3.14159 * self.radius ** 2

# from typing import Union, Optional, Any
#
# def process_data(data: Union[int, str, float, None]) -> Optional[Any]:
#     if data is None:
#         return None
#     if isinstance(data, int):
#         return f'Processed integer: {data * 2}'
#     if isinstance(data, str):
#         return f'Processed string: {data.upper()}'
#     if isinstance(data, float):
#         return f'Processed float: {round(data, 2)}'
#
# print(process_data(42))
# print(process_data('hello'))
# print(process_data(3.1415926535))
# print(process_data(None))

# name = str('Urban')
# print(name, type(name))
# name = int(5)
# print(name, type(name))
# name = float(5.5)
# print(name, type(name))
# name = list([1, 2])
# print(name, type(name))
#
# age = 30
# new_age = '30'
# print(age + new_age)

name = str('Dmitry')
print(f'Name:{name}, Type: {type(name)}')
age = int(31)
print(f'Age:{age}, Type: {type(age)}')
new_age = int(32)
print(f'Name:{new_age}, Type: {type(new_age)}')
is_student = True
print(f'Is Student:{is_student}, Type: {type(is_student)}')
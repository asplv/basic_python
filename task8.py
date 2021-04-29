'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''
class Data:
	 def __init__(self, ddmmyy):
		 self.ddmmyy = ddmmyy

	 @classmethod
	 def extract(cls, ddmmyy):
		 st = ddmmyy.split('-')

		 return int(st[0]), int(st[1]), int(st[2])

	 @staticmethod
	 def valid(ddmmyy):
	 	day, month, year = Data.extract(ddmmyy)

	 	if (1 <= month <= 12) or (1 <= day <= 31) or (year > 0):
	 		return True

	 	return False

	 def __str__(self):
		 return f'{Data.extract(self.ddmmyy)}'


today = Data('01-12-2020')
print(today)
print(today.valid('01-12-2020'))


'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class DivisionSafe:
	 @staticmethod
	 def divide(divider, denominator):
		 try:
			 return (divider / denominator)
		 except:
			 return (f'Zero division')

print(DivisionSafe.divide(10, 0))
print(DivisionSafe.divide(10, 0.1))



'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''
class InputValidator:
	@staticmethod
	def is_number(string):
		return string.isnumeric()

data = []
el = input()
while el != 'stop':
	if InputValidator.is_number(el):
		data.append(int(el))
	else:
		print('should be number')
	el = input()

print(data)



'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''
'''
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
'''
'''
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''
from abc import abstractmethod, ABC

class OrgTech(ABC):
	def __init__(self, model, serial_no, size):
		self.model = model
		self.serial_no = serial_no
		self.size = size

	@abstractmethod
	def __str__(self):
		pass

class Printer(OrgTech):
	def __str__(self):
		return f'Printer model {self.model} s/n {self.serial_no} size {self.size}'

class Xerox(OrgTech):
	def __str__(self):
		return f'Xerox model {self.model} s/n {self.serial_no} size {self.size}'

class Scanner(OrgTech):
	def __str__(self):
		return f'Scanner model {self.model} s/n {self.serial_no} size {self.size}'



class Warehouse:
	def __init__(self, size):
		self.total_size = size
		self.current_size = 0
		self.history = {}
		self.current = set()

	def put_tech(self, tech):
		if tech in self.current:
			print('Item already in warehouse')
			return

		if self.current_size + tech.size > self.total_size:
			print('Warehouse is full')
			return

		self.current_size += tech.size
		self.current.add(tech)

	def move_tech_to_dep(self, tech, dep):
		self.current.remove(tech)
		self.current_size -= tech.size
		self.history[tech] = dep

	def get_list_tech(self):
		return self.current

	def get_size_limit(self):
		return f'Warehouse total size {self.total_size} current {self.current_size}'

printer = Printer(1, 2, 3)
printer_2 = Printer(1, 3, 4)
scanner = Scanner(2, 3, 5)
xerox = Xerox(2, 5, 6)
warehouse = Warehouse(15)

warehouse.put_tech(printer)
warehouse.put_tech(printer)
warehouse.put_tech(printer_2)
warehouse.put_tech(scanner)
print(warehouse.get_list_tech())
warehouse.move_tech_to_dep(printer, 'sale')
print(warehouse.get_list_tech())
warehouse.put_tech(xerox)
print(warehouse.get_list_tech())




'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата
'''
class ComplexNumber:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return ComplexNumber(self.x + other.x, self.y + other.y)

	def __mul__(self, other):
		return ComplexNumber(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

	def __str__(self):
		return f'{self.x} + i * {self.y}'


z_1 = ComplexNumber(5, 3)
z_2 = ComplexNumber(9, -8)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)












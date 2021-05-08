'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
import time
import itertools

class TrafficLight:
	DURATIONS = {'red': 7, 'yellow': 2, 'green': 4}

	def __init__(self):
		self.__color = 'red'

	def running(self):
		for color in itertools.cycle(['red', 'yellow', 'green']):
			self.__color = color
			print(self.__color)
			time.sleep(TrafficLight.DURATIONS[self.__color])

tl = TrafficLight()
tl.running()


'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''
class Road:
	_length = 0
	_width = 0

	def __init__(self, length=0, width=0):
		self._length = length
		self._width = width

	def get_length(self):
		return self._length

	def get_width(self):
		return self._width

	def mass_calc(self, mass, thick):
		return (self._width * self._length * mass * thick) / 100

r = Road(20, 500)
print(r.mass_calc(25, 5))


'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''
class Worker:
	name = ''
	surname = ''
	position = ''
	_income = {}

	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
	def get_full_name(self):
		return f"{self.name} {self.surname}"

	def get_total_income(self):
		return self._income['wage'] + self._income['bonus']

pp = Position('John', 'Smith', 'Nurse', 75, 75)
print(pp.get_full_name())
print(pp.get_total_income())


'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''
import random

class Car:
	_name = ''
	_color = ''
	_speed = 0
	_is_police = False

	def __init__(self, name, color, speed=0, is_police=False):
		self._name = name
		self._color = color
		self._speed = speed
		self._is_police = is_police

	def go(self):
		self.set_speed(random.randint(1, 280))
		print(f'{self._name} set speed to {self._speed}')

	def stop(self):
		self.set_speed(0)
		print(f'{self._name} stopped')

	def turn(self, direction):
		print(f'{self._name} turned {direction}')

	def set_speed(self, speed):
		self._speed = speed

	def get_speed(self):
		return self._speed

	def show_speed(self):
		print(f'{self._name}, current speed: {self._speed}')


class TownCar(Car):
	def __init__(self, name, color='white'):
		super().__init__(name, color=color, is_police=False)

	def show_speed(self):
		print(f'{self._name}, current speed: {self._speed}')
		if self.get_speed() > 60:
			print("car is moving too fast")


class SportCar(Car):
	def __init__(self, name, color='red'):
		super().__init__(name, color=color, is_police=False)


class WorkCar(Car):
	def __init__(self, name, color='yellow'):
		super().__init__(name, color=color, is_police=False)

	def show_speed(self):
		print(f'{self._name}, current speed: {self._speed}')
		if self.get_speed() > 40:
			print('Car is moving too fast')


class PoliceCar(Car):
	def __init__(self, name, color='blue'):
		super().__init__(name, color=color, is_police=True)

random_car = Car('Volvo', 'black')
random_car.go()
random_car.turn('left')
random_car.show_speed()
random_car.stop()

t_car = TownCar('Suzuki')
t_car.go()
t_car.turn('right')
t_car.show_speed()
t_car.stop()

s_car = SportCar('Ferrari')
s_car.go()
s_car.turn('left')
s_car.show_speed()
s_car.stop()

w_car = WorkCar('Reno')
w_car.go()
w_car.turn('right')
w_car.show_speed()
w_car.stop()

p_car = PoliceCar('Lada', 'black')
p_car.go()
p_car.turn('right')
p_car.show_speed()
p_car.stop()


'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
class Stationery:
	_title = ''

	def __init__(self, title='dummy'):
		self._title = title

	def draw(self):
		print(f'using {self._title}')


class Pen(Stationery):
	def __init__(self):
		super().__init__('pen')

	def draw(self):
		print(f'using {self._title}')


class Pencil(Stationery):
	def __init__(self):
		super().__init__('pencil')

	def draw(self):
		print(f'using {self._title}')


class Marker(Stationery):
	def __init__(self):
		super().__init__('marker')

	def draw(self):
		print(f'using {self._title}')


dummy = Stationery()
dummy.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

marker = Marker()
marker.draw()







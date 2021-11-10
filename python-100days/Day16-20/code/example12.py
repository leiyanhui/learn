"""
面向对象的三大支柱：封装、继承、多态
面向对象的设计原则：SOLID原则
面向对象的设计模式：GoF设计模式（单例、工厂、代理、策略、迭代器）
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""

"""
类的设计原则：SOLID，是5个原则的首字母，即:
单一职责原则(Single Responsbility Principle)、
即一个类只负责一个职责，完成一个功能。好处是1。易于维护，可以写出高内聚的代码，即一个类中所有的属性和方法都是紧密相邻的，聚合度高的，不会有不相干的方法
和属性；2.已于代码的复用，由于单一职责，不会和其他职责混在一起，便于重复的使用


开放关闭原则(Open Close Principle)、
对扩展开放，对修改关闭，意思是写好的方法可以允许去进行扩展，但不要随意其修改。好处是1.易于代码维护，提升方法安全性，如果随意对修改方法，有可能会破坏方
法的原有功能；2.保证代码的扩展性，两个例子，如装饰器可以起到扩展方法功能的作用，不会改变原有代码，如几个方法功能相同，只是面向的对象不同，对这几个方法
进行判定调用（if--else语句）时，可以将方法名称改为相同，可以避免新增对象时增加判定语句，这里可以直接调用一个方法即可，因为不管是哪个对象，都是调用这
个名称的方法

里氏替换原则(Liskov Substitution Principle)、
使用基类引用的地方，必须可以使用继承类的对象，即任何地方继承类都可以用来替代基类，如一个父类是鸟类，拥有叫和飞两个方法，但是其继承类是燕子和鸵鸟，而鸵
鸟不具有飞这个方法，所以不能使用鸵鸟来替代鸟类，违背里氏替换原则。
好处是1.防止代码出现不可预知的错误，因为子类继承了父类中一些其不能拥有的方法；
2.方便用在基类上的测试代码，复用在子类上

接口分离原则(Interface Segregation Priciple)、
如果一个类包含很多接口，这些接口在使用中可以分离，那么就尽量将其分离开来，如上述里氏替换原则中的鸟类和鸵鸟的继承，违背了里氏替换原则，这时就可以将鸟内
中的两个方法进行分离在不同的类中，只让鸵鸟继承叫的方法即可，这样即遵循了接口分离原则，也不违背里氏替换原则。其实python中的接口，可以理解为就是抽象的方
法。好处是提高接口的复用价值

依赖倒置原则(Independency Inversion Principle)
即高层模块不应该直接依赖于底层模块，而是依赖于抽象的类或是抽象的方法，如电脑依赖的并不是具体的鼠标类，而是鼠标的类和方法，只要能单击，双击和移动指针就
行，具体的东西可以是鼠标，也可以是键盘

"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工(抽象类)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory:
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp
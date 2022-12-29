class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
        return cls._instance


class MyNumber(metaclass=Singleton):
    def __init__(self, number):
        self.number = number


class MyString(metaclass=Singleton):
    def __init__(self, m_string):
        self.m_string = m_string + ' ' + m_string


n_1 = MyNumber(1)
n_2 = MyNumber(10)
s_1 = MyString('qwerty')
s_2 = MyString('asdfg')

print(n_1.number)
print(n_2.number)
print(s_1.m_string)
print(s_2.m_string)
print('n_1 is n_2 — ', n_1 is n_2)
print('s_1 is s_2 — ', s_1 is s_2)
print('n_1 is s_2 — ', n_1 is s_1)
print('n_2 is s_2 — ', n_2 is s_2)
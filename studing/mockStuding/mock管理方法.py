from unittest.mock import Mock
# spec只是设置的是mock对象的属性，也就是说mock对象有这些属性，但是属性的值呢~~就说不定了~
class Foo1:
    _value1 = 100
    def fun1(self):
        pass
    def fun2(self, arg):
        pass
#
# class Foo2:
#     _value2 = 200
#     def fun3(self):
#         pass
#     def fun4(self, arg):
#         pass
#
#
# mockFoo1 = Mock(spec=Foo1)`
# mockFoo2 = Mock(spec=Foo2)
#
# mockFoo1.attach_mock(mockFoo2, 'mock_att')


mockFoo = Mock(spec=Foo1, return_value=1234)
print(mockFoo())
mockFoo.configure_mock(return_value=2345)
print(mockFoo())
mockFoo.configure_mock(**{'fun1.return_value': 100, "fun2.return_value": 200, '_value': 1000})
print(mockFoo.fun1())
print(mockFoo._value)
print(mockFoo.mock_calls)
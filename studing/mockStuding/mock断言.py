from unittest.mock import Mock
from unittest.mock import call


class Foo:
    _value = 100
    def fun1(self):
        pass
    def fun2(self, arg):
        pass


mockFoo = Mock(spec=Foo)
# print(mockFoo)
# print(mockFoo())
# print(mockFoo(a=10))
# print(mockFoo.fun1(10))
# print(mockFoo.fun2())
# # mockFoo.assert_called_with()
# mockFoo.assert_called_with(a=10)
# mockFoo.fun1.assert_called_with(10)
# mockFoo.fun1.assert_called_once_with(10)
mockFoo(10)
mockFoo.fun1()
mockFoo.fun2(10)
mockFoo.fun2(20)
fooCalls = [call.fun1(), call.fun2(10), call.fun2(20)]
mockFoo.assert_has_calls(fooCalls)
mockFoo.assert_any_call()
name = 'root'


def outer():
    name = 'alex'

    def func():
        nonlocal name
        name = "武沛齐"

        def inner():
            nonlocal name
            name = 123

        inner()
        print(name)

    func()
    print(name)


outer()
print(name)
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

# Ошибка: локальное пространство имен функции test_function() здесь недоступно
# inner_function()
# Зато можно вызвать test_function(), которая вызове inner_function()
test_function()
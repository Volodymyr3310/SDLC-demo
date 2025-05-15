def greet(name):
    return f"Привіт, {name}!"

if __name__ == "__main__":
    user_name = input("Введіть ваше ім'я: ")
    print(greet(user_name))

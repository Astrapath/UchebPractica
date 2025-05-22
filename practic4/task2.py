import sqlite3


def db():
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS alcodrinks ("
        "id INTEGER PRIMARY KEY, "
        "name TEXT NOT NULL, "
        "alcocontent REAL NOT NULL, "
        "stock INTEGER NOT NULL)"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS cocktails ("
        "id INTEGER PRIMARY KEY, "
        "name TEXT NOT NULL, "
        "ingredients TEXT NOT NULL, "
        "price REAL NOT NULL, "
        "strength REAL NOT NULL)"
    )

    conn.commit()
    conn.close()


def addalco(name, alcocontent, stock):
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO alcodrinks (name, alcocontent, stock) VALUES (?, ?, ?)",
        (name, alcocontent, stock)
    )
    conn.commit()
    conn.close()


def addcocktail(name, ingredients, price):
    strength = calcstrength(ingredients)
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cocktails (name, ingredients, price, strength) VALUES (?, ?, ?, ?)",
        (name, ingredients, price, strength)
    )
    conn.commit()
    conn.close()


def calcstrength(ingredients):
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    total = 0
    ingrlist = ingredients.split(',')
    for ingredient in ingrlist:
        cursor.execute(
            "SELECT alcocontent FROM alcodrinks WHERE name = ?",
            (ingredient.strip(),)
        )
        result = cursor.fetchone()
        if result:
            total += result[0]
    return total / len(ingrlist) if ingrlist else 0


def sell(name):
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT stock FROM alcodrinks WHERE name = ?",
        (name,)
    )
    result = cursor.fetchone()
    if result and result[0] > 0:
        cursor.execute(
            "UPDATE alcodrinks SET stock = stock - 1 WHERE name = ?",
            (name,)
        )
        conn.commit()
        print(f"Продано: {name}.")
    else:
        print(f"{name} отсутсвует")
    conn.close()


def restock(name, amount):
    conn = sqlite3.connect('drinks.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE alcodrinks SET stock = stock + ? WHERE name = ?",
        (amount, name)
    )
    conn.commit()
    conn.close()
    print(f"{amount} единиц {name} добавлено")


db()

while True:
    print("\n1.Добавить алкогольный напиток")
    print("2.Добавить коктейль")
    print("3.Продать напиток")
    print("4.Пополнить запасы")
    print("5.Выйти")

    choice = input()

    if choice == '1':
        name = input("название алкогольного напитка: ")
        alcocontent = float(input("крепость алкоголя: "))
        stock = int(input("количество на складе: "))
        addalco(name, alcocontent, stock)

    elif choice == '2':
        name = input("название коктейля: ")
        ingredients = input('ингредиенты (через ","): ')
        price = float(input("цена коктейля: "))
        addcocktail(name, ingredients, price)

    elif choice == '3':
        name = input("название напитка для продажи: ")
        sell(name)

    elif choice == '4':
        name = input("название напитка для пополнения: ")
        amount = int(input("количество для пополнения: "))
        restock(name, amount)

    elif choice == '5':
        break

    else:
        print("такой номер отсутсвует")

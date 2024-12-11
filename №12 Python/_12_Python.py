import json

Magazine = [
    {"Назва": "Bob", "Тираж": 10000, "Ціна": 200},
    {"Назва": "National Geographic", "Тираж": 500000, "Ціна": 300},
    {"Назва": "Creative", "Тираж": 5000, "Ціна": 150},
    {"Назва": "The day", "Тираж": 8000, "Ціна": 120},
    {"Назва": "The night", "Тираж": 1000, "Ціна": 30}
]

jsonData = json.dumps(Magazine)

with open("data.json", "wt") as file:
    file.write(jsonData)
file.close

while True:
    print("Меню:")
    print("1. Вивести всі журнали")
    print("2. Додати журнал")
    print("3. Видалити журнал")
    print("4. Знайти журнал")
    print("5. Обчислити середню вартість журналів з тиражем < 10 000")
    print("0. Вийти")

    x = input("Choose an option: ") 
    x = int(x)

    if x == 1:
        with open("data.json", "rt") as file:
            magazines = json.loads(file.read())
            for i in magazines:
                print(i)
        print("\n")

    elif x == 2:
        with open("data.json", "rt") as file:
            magazines = json.loads(file.read())
        
        name = input("Назва журналу: ")
        tirage = int(input("Тираж журналу: "))
        price = int(input("Ціна журналу: "))
        magazines.append({"Назва": name, "Тираж": tirage, "Ціна": price})
        
        with open("data.json", "wt") as file:
            file.write(json.dumps(magazines))
        print("Журнал додано.\n")

    elif x == 3:
        with open("data.json", "rt") as file:
            magazines = json.loads(file.read())
        
        name = input("Назва журналу, який бажаєте видалити: ")
        magazines = [i for i in magazines if i["Назва"] != name]
        
        with open("data.json", "wt") as file:
            file.write(json.dumps(magazines))
        print("Журнал видалено.\n")

    elif x == 4:
        with open("data.json", "rt") as file:
            magazines = json.loads(file.read())
        
        name = input("Введіть назву журналу, який хочете знайти: ")
        result = [i for i in magazines if i["Назва"] == name]
        if result:
            for i in result:
                print(i)
            print("\n")
        else:
            print("Журнал із такою назвою не знайдено.\n")

    elif x == 5:
        with open("data.json", "rt") as file:
            magazines = json.loads(file.read())
        
        prices = [i["Ціна"] for i in magazines if i["Тираж"] < 10000]
        if prices:
            Price = sum(prices) / len(prices)
            print(f"Середня вартість: {Price}\n")
        else:
            print("Немає журналів з тиражем < 10 000.\n")

    elif x == 0:
        print("Вихід з програми.")
        break

    else:
        print("Некоректне введення, спробуйте знову.\n")
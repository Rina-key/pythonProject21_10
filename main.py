class benzin:
    "Стоимость разных видов бензина"
    def __init__(self, Vid, Cost, Data) -> None:#магический метод init (заключается в том, чтобы инициализировать данные
        self.Vid, self.Cost, self.Data = Vid, Cost, Data
class Data:
    "Дата"
    def __init__(self, data: str) -> None:
        mas_data = data.split("-")
        self.day = mas_data[0]
        self.month = mas_data[1]
        self.year = mas_data[2]
    def __str__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"

def information():
    with open("txt.txt") as f: #считываем файл
        infa = list()
        while True:
           Vid = f.readline()
           if Vid == "":
               break
           else:
               Vid=Vid[:-1]
           Cost = f.readline()[:-1]
           data = f.readline()
           if data[-1] == "\n":
               data = data[:-1]
           infa.append(benzin(Vid, Cost, Data(data)))
    for i in infa:
        print(f"Вид бензина {i.Vid} стоит {i.Cost} рублей на {i.Data}")

information()
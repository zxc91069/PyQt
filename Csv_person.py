import csv
import time
import os

class Person():
    all_person = []
    def __init__(self, name, year, address):
        try:
            self.name = name
        except:
            self.name = name.encode("utf8").decode("cp950", "ignore")
        self.birth = f"{str(year)}"
        self.address = address
        t = time.localtime()
        self.time = time.strftime("%Y/%m/%d", t)
        self.filepath = "./csv"
        self.err = None

    def auto_detective_zodiac(self):
        self.zodiacs = [
                        "豬",
                        "鼠",
                        "牛",
                        "虎",
                        "兔",
                        "龍",
                        "蛇",
                        "馬",
                        "羊",
                        "猴",
                        "雞",
                        "狗"
        ]
        self.calcu = (int(self.birth) - 1899) % 12
        return self.zodiacs[self.calcu]

    def new_person(self):
        self.zodiac = self.auto_detective_zodiac()
        self.n = [self.name,
                  self.birth,
                  self.zodiac,
                  self.address
        ]

        if os.path.exists(self.filepath):
            pass
        else:
            os.mkdir(self.filepath)

        if os.path.isfile('./csv/belever.csv'):
            with open('./csv/belever.csv', newline='') as csvfile:

                c = csv.reader(csvfile)
                lis = (list(c))

            with open('./csv/belever.csv', 'a', newline='') as csvfile:  # 記得改回a 才會新增新的行

                if self.n in lis:
                    print("This person alread exists")
                else:
                    # Family.all_person.append(self.n)
                    self.writer = csv.writer(csvfile)
                try:
                    self.writer.writerow(self.n)
                except Exception as e:
                    self.err = str(e)

        else:
            with open('./csv/belever.csv', 'w', newline='') as csvfile:
                self.writer = csv.writer(csvfile)
                self.writer.writerow(["name", "birthday", "zodiac", "address"])
                try:
                    self.writer.writerow(self.n)
                except Exception as e:
                    self.err = str(e)

    def sorry_about_this(self, date, name):
        with open('./csv/belever.csv', newline='') as csvfile:
            self.c = csv.reader(csvfile)
            lit = []
            for i in self.c:
                if [i[0],i[2]] != [name,date]:
                    lit.append(i)
                else:
                    print(f"{i} has been removed")

        with open('./csv/belever.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            try:
                writer.writerows(lit)
            except Exception as e:
                self.err = str(e)
            print('File has been updated')

    def read_csv(self, csvname, val):

        if os.path.exists(self.filepath):
            pass
        else:
            os.mkdir(self.filepath)

        if os.path.isfile(self.filepath + "/" + csvname):
            with open(self.filepath + "/" + csvname, 'a', newline='') as f:
                writer = csv.writer(f)
                try:
                    writer.writerow(val)
                except Exception as e:
                    self.err = str(e)
        else:
            with open(self.filepath + "/" + csvname, 'w', newline='') as f:
                writer = csv.writer(f)
                try:
                    writer.writerow(val)
                except Exception as e:
                    self.err = str(e)




class Family():
    def __init__(self):
        self.p = []

    def reader_csv(self):
        with open ('./csv/belever.csv', newline='') as f:
            c = csv.reader(f)
            self.allperson = list(c)
        return self.allperson

    def same_address(self, name):
        self.reader_csv()

        self.adr = None
        for j in self.allperson:
            if j[0] == name:
                self.adr = j[3]

        if self.adr:
            for i in self.allperson:
                if i[3] == self.adr:
                    self.p.append(i[0])
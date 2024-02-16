class Library:
    def __init__(self, name, author, year, number):
        self.name = name
        self.author = author
        self.year = year
        self.number = number

    def book_add(self):
        with open("books.txt", "a+") as f:
            f.write(self.name + "," + self.author + "," + str(self.year) + "," + str(self.number) + "\n")

    def book_lists(self):
        with open("books.txt", "r") as f:
            data = f.readlines()
            if not data:
                print("Hiç kitap yok. \n")
            else:
                for line in data:
                    print(line)

    def book_del(self,del_name):
        books = []
        with open("books.txt", "r") as f:
            data = f.readlines()
            for line in data:
                new_line = line.split(",")
                if new_line[0] == del_name:
                    pass
                else:
                    books.append(new_line)
        # silmek istenilen kitap adı dışındaki, kitap adlarını boş bir listeye ekler.

        with open("books.txt", "w") as f:
            for temp in books:
                count = 0
                # print(temp)
                for line in temp:
                    if count == 3:
                        f.write(line)
                    else:
                        f.write(line + ",")
                        count = count + 1
        # doldurulan boş liste tekrar books.txt üzerine yazılır.

control = 1
while control:
    print("1-List Book \n2-Add Book \n3-Remove Book")
    num = input("İşlem numarasını giriniz: ")
    if num == "q":
        print("Program kapatildi.")
        control = 0
    else:
        if int(num) == 2:
            name = input("ad: ")
            author = input("yazar: ")
            year = input("yayın yılı: ")
            number = input("sayfa: ")
            lib = Library(name, author, int(year), int(number))
            lib.book_add()
        else:
            if int(num) == 1:
                try:
                    lib.book_lists()
                except:
                    print("Kitap yok. Kitap yüklemelisin. \n")
            else:
                if int(num) == 3:
                    try:
                        del_name = input("Silinecek kitabin adini girin: ")
                        lib.book_del(del_name)
                        print("Silme işlemi tamamlandi. \n")
                    except:
                        print("Silme işlemin hatali veya aradığın kitap yok. \n")




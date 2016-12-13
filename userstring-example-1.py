import UserString
class MyString(UserString.MutableString):

    def append(self, s):
        self.data = self.data + s
    def insert(self, index, s):
        self.data = self.data[:index] + s + self.data[index:]
    def remove(self, s):
        self.data = self.data.replace(s, "")
file = open("samples/book.txt")
text = file.read()
file.close()
book = MyString(text)
for bird in ["gannet", "robin", "nuthatch"]:
    book.remove(bird)
print book


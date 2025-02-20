#class

class Human:
   
    def __init__(self,name):
      self.name=name
      print("kurucu method")
    def __str__(self):
        return f"str fonksiyonundan dönen değer{self.name}"
    def talk(self,sentence):
        print(f"{self.name}:{sentence}")
    def walk(self,name):
        print(f"{self.name} is walking")

#örnek

human1=Human()

human1.walk("Merhaba","Samet")
human1.walk("Samet")

human2=Human()
human2.name="Ahmet"
human2.walk("Merhaba",)
human2.walk()
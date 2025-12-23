#Задание 1
# class Animal:
#     def __init__(self, nickname: str):
#         self.nickname = nickname
#
#     def __str__(self):
#         return f"Я животное по кличке {self.nickname}"
#
#
# class Cat(Animal):
#     def voice(self):
#         print("Мяу!")
#
#     def run(self):
#         print("Побежали!")


# class Parrot(Animal):
#     def voice(self):
#         print("Кар!")
#
#     def fly(self):
#         print("Полетели!")
#
# cat = Cat("Мурзик")
# print(cat)
# cat.voice()
# cat.run()
#
# parrot = Parrot("Кеша")
# print(parrot)
# parrot.voice()
# parrot.fly()
#Задание 2
class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def showHeader(self):
        print(f"From: {self.sender} -> To: {self.recipient}")


class TextMessage(Message):
    def __init__(self, sender, recipient, text):
        super().__init__(sender, recipient)
        self.text = text

    def send(self):
        self.showHeader()
        print(self.text)
        

class StickerMessage(Message):
    def __init__(self, sender, recipient, sticker):
        super().__init__(sender, recipient)
        self.sticker = sticker
        self.count = 1

    def send(self):
        self.showHeader()
        print(f"{self.sticker} (sent {self.count} times)")
        self.count += 1

msg1 = TextMessage("Алиса", "Ваня", "Привет!")
msg1.send()

msg2 = StickerMessage("Ваня", "Алиса", "(─‿‿─)")
msg2.send()

# from random import shuffle

# class Person:
#     # properties/attributes:
#     def __init__(self, email, first_name, last_name, username):
#         self.email = email
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username

#     # methods/actions/behaviors:
#     def __str__(self):
#         return f"Person(first_name: {self.first_name}, last_name:{self.last_name}, email: {self.email}, username: {self.username})"

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def say_hi(self):
#         return f"Hi, I'm {self.full_name()}"
    
# p = Person("Harry@gmail.com", "Harry", "Potter", "hpotter")

# print(p)
# # p2 = Person("hermione@gmail.com", "Hermione", "Granger", "hgranger")

# # print(p.full_name())
# # print(p.say_hi())

# # print(p2.full_name())
# # print(p2.say_hi())


# class Card:
#     # suit, rank:
#     def __init__(self, rank:str, suit:str):
#         self.rank = rank
#         self.suit = suit

#     def __str__(self):
#         return f"suit: {self.suit}, rank: {self.rank}"
    
#     def show(self):
#         return f"{self.rank} of {self.suit}"
    
# class Deck:
#      # props: list of cards:
#     def __init__(self):
#         self.cards = []
#         ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#         suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

#         #  loop through suits and ranks to populate the list of cards
#         for rank in ranks:
#             for suit in suits:
#                 self.cards.append(Card(rank, suit))

#     def __str__(self):
#         return ", ".join([str(card) for card in self.cards])

#     def shuffle(self):
#         shuffle(self.cards)

        
# deck = Deck()
# deck.shuffle()
# print(deck)





# # class Animal:
# #     # properties/attributes:
# #     def __init__(self, name):
# #         self.name = name

# #     def make_sound(self):
# #         return "Animal sound"
    
# # class Cat(Animal):
# #     def __init__(self, name, breed):
# #         # call the parent class constructor:
# #         super().__init__(name)
# #         self.breed = breed
    
# #     def make_sound(self):
# #         return "Meow"

# # cat1 = Cat("Fluffy", "Siamese")
# # print(cat1.make_sound())



# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# base class:
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Animal sound"

# behavior class:
class Driver:
    def drive(self):
        return "Driving"

# inheritance:
class Cow(Animal, Driver):
    def make_sound(self):
        return "Moo"
    


class Duck:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Duck Sound"

class FlyBehavior:
    def fly(self):
        return "Flying"

class MollardDuck(Duck, FlyBehavior):
    def make_sound(self):
        return "Mollard Quack"
    
class RedheadDuck(Duck, FlyBehavior):
    def make_sound(self):
        return "Quack"

class RubberDuck(Duck):
    def make_sound(self):
        return "Squeak"
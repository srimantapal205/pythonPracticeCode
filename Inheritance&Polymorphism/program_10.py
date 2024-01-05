#Apython program showing single inheritance whichtwo sub class are derived from single base class
#single inheritance
class Banks(object):
    cash = 100000000
    @classmethod
    def available_cash(cls):
        print(cls.cash)
    
class AndhraBank(Banks):
    pass

class StateBank(Banks):
    cash = 20000000
    @classmethod
    def available_cash(cls):
        print(cls.cash +Banks.cash)
        
ab = AndhraBank()
ab.available_cash()

sb = StateBank()
sb.available_cash()

from abc import ABC, abstractmethod

class MTGApiInterface(ABC):
    
    @abstractmethod
    def get_standard_cards(self):
        pass
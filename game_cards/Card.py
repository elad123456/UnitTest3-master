class Card:
    # the function get value and suit and defind the Card object
    def __init__(self,value,suit):
        '''the function get value and suit and defind the Card object'''
        self.d = {'Diamond': 1, 'Spade': 2, 'Heart': 3, 'Club': 4}
        if type(value)==int and type(suit)==str and suit in self.d and 1<=value<=13:
            self.value=value
            self.suit=suit
        else:
            raise TypeError("the arguments are incorrect")
    # the function get another card and return true if the current card is bigger than the argument and return false if it dont happen, edge value: Ace
    def __gt__(self, other):
        ''' the function get another card and return true if the current card is bigger than the argument and return false if it dont happen'''
        self.d = {'Diamond':1, 'Spade':2, 'Heart':3, 'Club':4}
        # check if the argument's type is Card
        if type(other)!=Card:
            raise TypeError("the type must be Card")
        # check if current card is Ace and the argument is not Ace
        if self.value==1 and other.value!=1:
            return True
        # check if current card's value is equal to the argument's value and compare their suits
        elif self.value==other.value:
            if self.d[self.suit]>self.d[other.suit]:
                return True
        # check if the argument is Ace
        elif other.value==1:
            return False
        # check if current value is bigger than the argument's value
        elif self.value>other.value:
            return True
        else:
            return False
    # compare two card according to their values and suits
    def __eq__(self, other):
        '''the function compare between two cards'''
        if type(other)!=Card:
            raise TypeError("the type of the argument is invalid")
        if self.value==other.value and self.suit==other.suit:
            return True
        return False
    # return a string that describe the card's values
    def __repr__(self):
        '''return a string that describe the card's values'''
        val = self.value
        if val==13:
            val='KING'
        elif val==12:
            val='QUEEN'
        elif val==11:
            val='JACK'
        elif val==1:
            val='ACE'
        suit=self.suit
        if suit=='Diamond':
            suit="🔶"
        elif suit=='Heart':
            suit='❤'
        elif suit=='Spade':
            suit='♠'
        elif suit=='Club':
            suit='♣'

        return f"{val} {suit}"

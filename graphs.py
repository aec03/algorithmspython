from collections import deque

class Person:
    """ represents a person in a social network """
    def __init__(self, name, friends=None):
        self.name = name.title()

        if friends == None: self.friends = []
        else: self.friends = friends
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Person({self.name})'

    def add_friends(self, other):
        self.friends.append(Friends(self, other))


class Friends(tuple):
    """ represents a friendship in the social network """
    def __new__(self, p1, p2):
        return tuple.__new__(self, (p1, p2))

    def __repr__(self):
        return f'Friends({self[0]}, {self[1]})'

    __str__ = __repr__


class SocialNetwork(dict):
    """ represents a basic social network """
    def __init__(self, pt=[], ft=[]):
        """ pt = list of people
            ft = list of friends """
        for p in pt:
            self.add_people(p)

        for f in ft:
            self.add_friends(f)

    def add_people(self, p):
        """ add person to graph """
        self[p] = {}
        for f in p.friends:
            self.add_friends((Friends(p, f)))

    def add_friends(self, f):
        """ add friends to graph """
        p1, p2 = f
        self[p1][p2] = f
        self[p2][p1] = f

    def get_friends(self, p1, p2):
        """ try to get friends between people;
        return friends, None otherwise """
        try:
            if self[p1][p2] == self[p1][p2]: return self[p1][p2]
        except: return None

    def people(self):
        """ returns a list of people in social network """
        pt = [p for p in self.keys()]
        return pt

    def friends(self):
        """ returns a list of all friendships in social network """
        et = []
        for p1 in self.values():
            et.extend([p2 for p2 in p1.values() if p2 not in et])
        return et

    def add_all_friends(self):
        """ adds a frienship betweem everybody in dictionary """
        for p1 in self.keys():
            for p2 in self.keys():
                if p1 != p2: self.add_friends(Friends(p1, p2))

    def friend_search(self, p1, p2):
        """ searchs for mutual friends in social network;
        returns True if there is a path connection, False otherwise """
        queue = deque()
        queue.extend(self[p1])
        searched = []
        while queue:
            person = queue.popleft()
            if person == p2: return True
            queue.extend(self[person])
            searched.append(person)
        return False


if __name__ == '__main__':
    sean = Person('sean')
    ngozi = Person('ngozi')
    liam = Person('liam')
    aidan = Person('aidan')
    

    s = SocialNetwork([aidan, sean, liam, ngozi])
    s.add_all_friends()
    print(s.friends())
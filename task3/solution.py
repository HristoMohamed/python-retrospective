class Person:
    person_list = []

    def __init__(self, name, birth_year, gender, *args, **kwargs):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        if kwargs:
            if self.birth_year - kwargs['mother'].birth_year > 18:
                self.mother = kwargs['mother']
            if self.birth_year - kwargs['father'].birth_year > 18:
                self.father = kwargs['father']
        self.__class__.person_list.append(self)

    
    def get_siblings_by_common_parent(self, parent):
        siblings = []
        if parent:
            for person in self.__class__.person_list:
                if parent in person.get_parents() and person is not self:
                    siblings.append(person)
        return (list(set(siblings)))

    def get_parents(self):
        return (self.mother, self.father)

    def get_siblings(self):
        siblings = []
        parents = [self.mother, self.father]
        for parent in parents:
            siblings = self.get_siblings_by_common_parent(parent) + siblings
        return (list(set(siblings)))

    def get_sisters(self):
        return list(filter(lambda sibling: sibling.gender == 'F',
                           self.get_siblings()))

    def get_brothers(self):
        return list(filter(lambda sibling: sibling.gender == 'M',
                           self.get_siblings()))

    def children(self, **kwargs):
        genders = ['F', 'M']
        children_list = []
        if kwargs:
            genders = [kwargs.get('gender')]
        for person in self.__class__.person_list:
            if self in person.get_parents():
                children_list.append(person)
        return list(filter(lambda child: child.gender in genders,
                           children_list))

    def is_direct_successor(self, another_person):
        return another_person in self.children()

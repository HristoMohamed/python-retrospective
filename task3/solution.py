class Person:
    instances = []
    name = None
    birth_year = None
    gender = None
    mother = None
    father = None
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

    def get_brothers(self):
        list_of_brothers = []
        for family_member in self.__class__.person_list:
            if family_member.mother or family_member.father:
                if ((family_member.mother is self.mother or
                   family_member.father is self.father) and
                   family_member.gender == "M"):
                    list_of_brothers.append(family_member)
        return(list_of_brothers)

    def get_sisters(self):
        list_of_sisters = []
        for family_member in self.__class__.person_list:
            if family_member.mother or family_member.father:
                if ((family_member.mother is self.mother or
                   family_member.father is self.father) and
                   family_member.gender == "F"):
                    list_of_sisters.append(family_member)
        return (list_of_sisters)

    def children(self, *args, **kwargs):
        flag = False
        kids = []
        if kwargs:
            if kwargs['gender'] == 'M' or kwargs['gender'] == 'F':
                flag = True
        for family_member in self.__class__.person_list:
            if family_member.mother or family_member.father:
                if (family_member.mother is self or
                   family_member.father is self):
                    kids.append(family_member)
        if flag:
            gender_specific_kids = list(set(
                filter(lambda kid: kid.gender == kwargs['gender'], kids)))
            return(gender_specific_kids)
        else:
            return(kids)

    def is_direct_successor(self, another_person):
        if another_person.mother or another_person.father:
            if self is another_person.mother or self is another_person.father:
                return True
            else:
                return False
        else:
            return False

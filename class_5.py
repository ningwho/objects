class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        print 'Hi my name is %s, email address is %s, and my phone number is %s' % (name, email, phone)
    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)
    def add_friend(self, friend):
        self.friends.append(friend)
    def __repr__(self):
        return 'Person(%s, %s)' % (self.name, self.email)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')


jordan.add_friend(sonny)
sonny.add_friend(jordan)

print jordan.friends

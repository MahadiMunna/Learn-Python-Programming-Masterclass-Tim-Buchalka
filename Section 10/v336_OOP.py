class engineer(object):

    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language


munna = engineer("Mahadi Munna", 26, "Python")

print(f'{munna.name} {munna.age} {munna.language}')
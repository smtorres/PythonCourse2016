class School(object):
    def __init__(self, name):
        self.name = name
        self.roster = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}

    def addStudent(self, name, grade):
        self.roster[grade].append(name)
        print 'Added %s to the %s grade roster' % (name, grade)

    def printRoster(self, grade):
        print '\n'.join(self.roster[grade])

    def __str__(self):
        output = ''
        for grades in self.roster.keys():
            output += 'Grade %d: %s \n' % (grades, str(' '.join(sorted(self.roster[grades]))))
        return output

    def __repr__(self):
        return self.__str__()


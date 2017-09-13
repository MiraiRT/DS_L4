class Term:
    def __init__(self, c, p):
        self.c = c
        self.p = p

    def __str__(self):
        return str(self.c) + 'n' + str(self.p) + ' '

    def __add__(self, other):
        if self.p == other.p:
            return Term(self.c + other.c, self.p)

    def __lt__(self, other):
        if self.p < other.p:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.p >= other.p:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.p == other.p:
            return True
        else:
            return False


class OrderedList:
    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def insert(self, term):
        if self.size() == 0:
            self.list.append(term)
        else:
            isNotAdd = True
            for i in range(self.size()):
                if self.list[i] < term:
                    self.list.insert(i, term)
                    isNotAdd = False
                    break
                elif self.list[i] == term:
                    self.list[i] += term
                    isNotAdd = False
                    break
                else:
                    continue
            if isNotAdd:
                self.list.append(term)

    def __add__(self, other):
        result = OrderedList()
        if self.size() == 0:
            return other
        elif other.size() == 0:
            return self
        else:
            # Code: List + List
            i, j = 0, 0
            while True:
                if self.list[i] >= other.list[j]:
                    if self.list[i] == other.list[j]:
                        result.insert(self.list[i] + other.list[j])
                        i += 1
                        j += 1
                    else:
                        result.insert(self.list[i])
                        i += 1
                else:
                    if self.list[i] == other.list[j]:
                        result.insert(self.list[i] + other.list[j])
                        i += 1
                        j += 1
                    else:
                        result.insert(other.list[j])
                        j += 1
                if i == self.size() and j != other.size():
                    while j != other.size():
                        result.insert(other.list[j])
                        j += 1
                    break
                elif i != self.size() and j == other.size():
                    while i != self.size():
                        result.insert(self.list[i])
                        i += 1
                    break
                elif i == self.size() and j == other.size():
                    break
            return result

    def __str__(self):
        s = ''
        for i in range(self.size()):
            s = s + str(self.list[i].c) + 'n' + str(self.list[i].p) + ' + '
        return s[0:len(s) - 2]


print('Check +')
t1 = Term(1, 2) + Term(-4, 2)
t2 = Term(1, 7) + Term(4, 7)
print(t1)
print(t2)
print(t1 < t2)

print('\nCheck List')
p = OrderedList()
p.insert(Term(1, 2))
p.insert(Term(7, 4))
p.insert(Term(7, 3))
p.insert(Term(-2, 3))
print('p = ' + str(p))
q = OrderedList()
q.insert(Term(2, 6))
q.insert(Term(7, 7))
q.insert(Term(2, 1))
print('q = ' + str(q))
r = p + q
print('p + q = ' + str(r))

import os


class Field():
    def __init__(self, size, quan_queens):
        self.size = size
        self.queens = quan_queens
        self.used_places = list()
        self.matrix = list()
        self.temp_quan = 0
        self.counter = 0
        self.folder = str()
        self.all_var = list()


    def check(self, i, j):
        flag = True
        for k in range(len(self.used_places)):
            if i == self.used_places[k][0] or j == self.used_places[k][1] or\
                abs(i - self.used_places[k][0]) == abs(j - self.used_places[k][1]):
                flag = False
                break
        return flag


    def creat_folder(self):
        if not os.path.exists(f"J:\\Files\\Python\\Homeworks\\Queens\\Variations\\{self.folder}"):
            os.makedirs(f"J:\\Files\\Python\\Homeworks\\Queens\\Variations\\{self.folder}")


    def matrix_done(self):
        for i in range(self.size):
            self.matrix.append([])
            for j in range(self.size):
                self.matrix[i].append("0")


    def recursion(self, ibegin):
        if self.temp_quan < self.queens:
            for i in range(ibegin, self.size):
                for j in range(self.size):
                    if self.check(i, j):
                        self.matrix[i][j] = "1"
                        self.used_places.append([i, j])
                        self.temp_quan += 1
                        self.recursion(i + 1)
        else:
            self.counter += 1
            self.all_var.append(self.matrix)
            
            
        if self.used_places:
            self.matrix[self.used_places[-1][0]][self.used_places[-1][1]] = "0"
            del self.used_places[-1]
        self.temp_quan -= 1
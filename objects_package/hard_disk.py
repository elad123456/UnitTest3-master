class hard_disk:
    def __init__(self):
        self.area=100
        self.full=0
        self.num_files=0
    def show(self):
        print(f"space in hard disk: {self.area}, full space: {self.full}, numbers of file: {self.num_files}")
    def freespace(self):
        return self.area-self.full
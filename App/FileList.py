class FileList:
    def __init__(self):
        self.plainFiles = list()
        self.todoFiles = list()
        self.plainFilesDict = dict()
        self.todoFilesDict = dict()

    def appendPlain(self, line):
        self.plainFiles.append(line)

    def appendTodo(self, file):
        self.todoFiles.append(file)

    def __str__(self):
        return "Plain Files: " + str(self.plainFiles) + "\nTodo Files: " + str(self.todoFiles)

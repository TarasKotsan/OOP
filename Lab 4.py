from abc import ABC, abstractmethod

# --- Composite Pattern ---

class FileSystemComponent(ABC):
    @abstractmethod
    def show_info(self, indent=0):
        pass

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_info(self, indent=0):
        print(' ' * indent + f'File: {self.name}')

class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_info(self, indent=0):
        print(' ' * indent + f'Folder: {self.name}')
        for child in self.children:
            child.show_info(indent + 4)

# --- Facade Pattern ---

class FileSystemFacade:
    def create_sample_structure(self):
        root = Folder("Root")

        folder1 = Folder("Folder1")
        folder1.add(File("file1.txt"))
        folder1.add(File("file2.txt"))

        folder2 = Folder("Folder2")
        folder2.add(File("file3.txt"))

        root.add(folder1)
        root.add(folder2)
        root.add(File("rootfile.txt"))

        return root

    def show_file_system(self):
        root = self.create_sample_structure()
        root.show_info()


# --- Виконання ---

if __name__ == "__main__":
    facade = FileSystemFacade()
    facade.show_file_system()

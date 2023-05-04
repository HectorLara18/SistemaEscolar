class Persona:
    def __init__(self, Name: str, LastnameFather: str, LastnameMother: str):
        self.Nombre = Name
        self.ApellidoPaterno = LastnameFather
        self.ApellidoMaterno = LastnameMother

    def get_Information(self):
        print(f"{self.Nombre} {self.ApellidoPaterno} {self.ApellidoMaterno}")

    def get_str_information(self):
        return f"{self.Nombre} {self.ApellidoPaterno} {self.ApellidoMaterno}"
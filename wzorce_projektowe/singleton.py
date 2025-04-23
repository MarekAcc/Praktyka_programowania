class Singleton:
    # Pole klasowe dostępne "globalnie" dla wszystkich klas
    _instance = None

    # Metoda tworząca nową instancję lub zwracająca istniejącą w przypadku próby stworzenia nowej
    def __new__(cls):
        if cls._instance is None:
            print("Tworzę nową instancję Singleton i ją zwracam")
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            print("Zwracam istniejącą instancję Singleton")
            return cls._instance
            
    # Inne funkcje charakterystyczne dla zadań tego obiektu
    def Function1(self):
        pass
    def Function2(self):
        pass


s1 = Singleton()
s2 = Singleton()
s3 = Singleton()



"""OUTPUT:
Tworzę nową instancję Singleton i ją zwracam
Zwracam istniejącą instancję Singleton
Zwracam istniejącą instancję Singleton
"""

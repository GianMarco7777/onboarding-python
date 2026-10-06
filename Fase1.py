class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.libri = []

# Inserisco i metodi della classe "Biblioteca"

#Aggiunta di un libro

def libro_aggiunto(self, libro: str):
        self.libri.append(libro)
        print (
             f"Il libro aggiunto è: {libro}"
        )

#Ricerca di un libro

def ricerca_libro(self, libro: str):
        for libro in self.libri:        
            if libro == libro:
                  print
                    (
                         f"Il libro {libro} si trova alla biblioteca {self.nome}"

                    )

#Rimozione di un libro

def rimuovere_libro(self, libro: str):
        self.libri.remove(libro)
            print(
                 f" il libro {libro} è stato rimosso"    
            )

#Ricerca di un autore

def ricerca_autore(self, autore: str):
        for libro in self.libri:
              if autore in libro:
                    print (
                          f" L'autore {autore} è presente"
                    )

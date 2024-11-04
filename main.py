class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidade = True  # True significa que o livro está disponível

    def adicionar(self, biblioteca):
        biblioteca.adicionar_livro(self)

    @staticmethod
    def buscar(biblioteca, termo):
        resultado = []
        for livro in biblioteca.livros:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.nome.lower():
                resultado.append(livro)
        return resultado


class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []

    def emprestar_livro(self, livro, biblioteca):
        if livro.disponibilidade:
            livro.disponibilidade = False
            self.livros_emprestados.append(livro)
            print(f'{self.nome} emprestou o livro: {livro.titulo}')
        else:
            print(f'O livro {livro.titulo} não está disponível para empréstimo.')

    def devolver_livro(self, livro, biblioteca):
        if livro in self.livros_emprestados:
            livro.disponibilidade = True
            self.livros_emprestados.remove(livro)
            print(f'{self.nome} devolveu o livro: {livro.titulo}')
        else:
            print(f'{self.nome} não possui o livro {livro.titulo} emprestado.')


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro adicionado: {livro.titulo}')


# Exemplo de uso
if __name__ == "__main__":
    # Criar uma biblioteca
    biblioteca = Biblioteca()

    # Criar autores
    autor1 = Autor("J.K. Rowling", "Britânica")
    autor2 = Autor("George Orwell", "Britânico")

    # Criar livros
    livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1, "978-3-16-148410-0")
    livro2 = Livro("1984", autor2, "978-0-452-28423-4")

    # Adicionar livros à biblioteca
    livro1.adicionar(biblioteca)
    livro2.adicionar(biblioteca)

    # Criar usuário
    usuario = Usuario("Maria", "001")

    # Usuário empresta um livro
    usuario.emprestar_livro(livro1, biblioteca)

    # Busca por um livro
    resultados = Livro.buscar(biblioteca, "Harry")
    for livro in resultados:
        print(f'Livro encontrado: {livro.titulo} de {livro.autor.nome}')
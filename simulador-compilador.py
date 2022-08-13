
from tkinter import *
from tkinter import ttk

from analizador_lexico import analizador


class Compilador():
    def __init__(self) -> None:
        self.principal = Tk()
        self.principal.geometry('600x600')
        self.principal.title('Proyecto Compiladores')

        # Frame principal de la aplicación
        self.marcoPrincipal = ttk.Frame(self.principal, padding=20)
        self.marcoPrincipal.pack()

        self.entradaDatos()
        self.salidaTokens()

    def entradaDatos(self):
        Font_tuple = ("Comic Sans MS", 20, "bold")
        ttk.Label(self.marcoPrincipal, text="Analizador Léxico",
                  font=Font_tuple).pack()
        self.entrada = Text(self.marcoPrincipal, width=40, height=5,
                            padx=5, pady=10, font=Font_tuple
                            )
        self.entrada.pack()
        ttk.Button(self.marcoPrincipal, width='30', text='EJECUTAR',
                   command=self.ejecutar).pack()
        ttk.Button(self.marcoPrincipal, width='30', text='LIMPIAR',
                   command=self.limpiar).pack()

    def salidaTokens(self):
        Font_tuple = ("Comic Sans MS", 20, "bold")
        self.salida = Text(self.marcoPrincipal, width=40, height=5,
                           padx=5, pady=5, font=Font_tuple
                           )
        self.salida.pack()

    def limpiar(self):
        self.entrada.delete('1.0', END)
        self.salida.delete('1.0', END)

    def ejecutar(self):
        dato = self.entrada.get(1.0, END)
        self.resultado = analizador(dato)
        print(self.resultado)
        # MOSTRANDO LOS DATOS EN EL WIDGET TEXTO

        for dato in self.resultado:
            self.salida.insert(END, dato+'\n')

    def run(self):
        self.principal.mainloop()


if __name__ == '__main__':
    compi = Compilador()
    compi.run()

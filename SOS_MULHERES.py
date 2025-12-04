import tkinter as tk
from tkinter import messagebox
import requests

class SistemaSeguranca:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema de d=segurança para mulheres")
        self.janela.geometry("300x200")

        self.botao_emergencia = tk.Button(self.janela, text="BOTÃO DE EMERGÊCIA", command=self.envia_alerta)
        self.botao_emergencia.pack(pady=50)

        self.label_status = tk.Label(self.janela, text="Status: OK")
        self.label_status.pack()

        def envia_alerta(self):
            #Simula a requisição ao sistema naciolnal de segurança
        try:
            resposta = requests.post("http://sistema-nacional.com/alerta", json={"localizacao": "Latitude, Longitude", "tipo": "violência doméstica"})
            if resposta.stb atus_code == 200:
                self.label_status.config](text="status: Alerta enviado com sucesso!")
                messagebox.showinfo("Alerta Enviado", "A polícia militar foi notificada.")
            else:
                self.label_status.config(text="Status: Erro ao enviar alerta.")
                messagebox.showinfo("Alerta Enviado", "A polícia militar foi notificada.")
        except Exception as e:
            self.label_status.config(text="Status: Erro ao enviar alerta.")
            messagebox.showinfo("Erro", str(e))

            def run(self):
                self.janela.mainloop()

                if __name__ == "__main__":
                    sistema = SistemaSeguranca()
                    sistema.run()
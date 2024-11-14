import tkinter as tk
from tkinter import ttk

# Função para calcular e exibir a tabuada
def calcular_tabuada():
    try:
        numero = int(entry_numero.get())
        resultado_texto = f"Tabuada de {numero}:\n"
        for i in range(1, 11):
            resultado_texto += f"  {numero} x {i} = {numero * i}\n"
        label_resultado.config(text=resultado_texto)
    except ValueError:
        label_resultado.config(text="Por favor, insira um número inteiro válido.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Tabuada")
janela.geometry("300x400")
janela.configure(bg="#66CDAA")

# Título
label_titulo = tk.Label(janela, text="Calculadora de Tabuada", font=("Helvetica", 16, "bold"), bg="#4a90e2", fg="white")
label_titulo.pack(pady=10, fill=tk.X)

# Campo de entrada para o número
frame_entrada = tk.Frame(janela, bg="#66CDAA")
frame_entrada.pack(pady=20)
label_numero = tk.Label(frame_entrada, text="Digite um número:", font=("Helvetica", 12), bg="#66CDAA")
label_numero.grid(row=0, column=0, padx=5)
entry_numero = tk.Entry(frame_entrada, font=("Helvetica", 12), width=5)
entry_numero.grid(row=0, column=1, padx=5)

# Botão para calcular a tabuada
botao_calcular = ttk.Button(janela, text="Calcular", command=calcular_tabuada)
botao_calcular.pack(pady=10)

# Área de exibição do resultado
label_resultado = tk.Label(janela, text="", font=("Helvetica", 12), bg="#ffffff", fg="#333333", justify="left")
label_resultado.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

# Estilo do botão
estilo = ttk.Style()
estilo.configure("TButton", background="orangered", font=("Helvetica", 12, "bold"), foreground="indigo")

# Inicia a aplicação
janela.mainloop()

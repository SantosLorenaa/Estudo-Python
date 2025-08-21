import tkinter as tk
from tkinter import messagebox
import json, os


ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def adicionar_tarefa():
    titulo = entrada.get()
    if titulo.strip() == "":
        messagebox.showwarning("Aviso", "Digite uma tarefa!")
        return
    nova_tarefa = {"titulo": titulo, "concluida": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas()
    atualizar_lista()
    entrada.delete(0, tk.END)

def remover_tarefa():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")
        return
    index = selecionado[0]
    tarefas.pop(index)
    salvar_tarefas()
    atualizar_lista()

def alternar_concluida():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para marcar/desmarcar.")
        return
    index = selecionado[0]
    tarefas[index]["concluida"] = not tarefas[index]["concluida"]
    salvar_tarefas()
    atualizar_lista()

def atualizar_lista():
    lista.delete(0, tk.END)
    for t in tarefas:
        status = "✅" if t["concluida"] else "❌"
        lista.insert(tk.END, f"{status} {t['titulo']}")

janela = tk.Tk()
janela.title("To-Do List")


entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

btn_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_tarefa)
btn_adicionar.pack(pady=2)

btn_concluir = tk.Button(janela, text="Marcar/Desmarcar", command=alternar_concluida)
btn_concluir.pack(pady=2)

btn_remover = tk.Button(janela, text="Remover", command=remover_tarefa)
btn_remover.pack(pady=2)


lista = tk.Listbox(janela, width=50, height=10)
lista.pack(pady=5)


tarefas = carregar_tarefas()
atualizar_lista()

janela.mainloop()

"""
keycapture_demo.py
Demo educativo: captura de teclas LOCAL (janela em foco) usando tkinter.
Uso: python3 keycapture_demo.py
"""

import tkinter as tk
import datetime
import pathlib

LOG_FILE = "keycapture_demo_logs.txt"

def registrar_log(texto):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{ts}] {texto}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linha)

def on_key(event):
    
    texto = f"Tecla: {event.keysym} (char='{event.char}')"
    registrar_log(texto)
    status_var.set(f"Última tecla: {event.keysym}")

def limpar_logs():
    p = pathlib.Path(LOG_FILE)
    if p.exists():
        p.unlink()
    status_var.set("Logs limpos.")

def abrir_logs():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = "(nenhum log)"
    top = tk.Toplevel(root)
    top.title("Conteúdo dos logs")
    txt = tk.Text(top, width=80, height=30)
    txt.insert("1.0", content)
    txt.config(state="disabled")
    txt.pack(padx=8, pady=8)

# UI
root = tk.Tk()
root.title("Key Capture Demo (janela em foco)")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

lbl = tk.Label(frame, text="Clique aqui e digite — somente enquanto esta janela estiver em foco.")
lbl.pack(anchor="w")

entry = tk.Entry(frame, width=60)
entry.pack(pady=(6, 12))
entry.focus_set()  # deixar o foco para receber teclas imediatamente

status_var = tk.StringVar(value="Aguardando entrada...")
status_lbl = tk.Label(frame, textvariable=status_var)
status_lbl.pack(anchor="w", pady=(4,8))

btn_frame = tk.Frame(frame)
btn_frame.pack(fill="x", pady=(6,0))
tk.Button(btn_frame, text="Limpar logs", command=limpar_logs).pack(side="left")
tk.Button(btn_frame, text="Abrir logs", command=abrir_logs).pack(side="left")

# Bind: captura eventos de tecla **apenas** quando a janela/entry estiver em foco
root.bind_all("<Key>", on_key)  # cuidado: root.bind_all captura enquanto app em execução e foco no app
# Observação: este demo NÃO captura teclas quando a janela NÃO estiver selecionada.
# Se quiser limitar apenas ao entry, use: entry.bind("<Key>", on_key)

root.mainloop()

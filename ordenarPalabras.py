import openai
import tkinter as tk


openai.api_key = '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'


def ordenar_palabras():
    oracion_desordenada = entrada_oracion.get()
    if oracion_desordenada:
        oracion_ordenada = ordenar_palabras_api(oracion_desordenada)
        texto_resultado.config(text="Oración ordenada: " + oracion_ordenada)


def ordenar_palabras_api(oracion_desordenada):
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Ordena las siguientes palabras para formar una oración coherente:\n{oracion_desordenada}",
        max_tokens=50  # Ajusta esto según sea necesario
    )
    return respuesta.choices[0].text.strip()


ventana = tk.Tk()
ventana.title("Ordenador de Oraciones")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="Ingrese una oración desordenada:")
etiqueta.pack()

entrada_oracion = tk.Entry(ventana)
entrada_oracion.pack()

boton_ordenar = tk.Button(ventana, text="Ordenar Oración", command=ordenar_palabras)
boton_ordenar.pack()

texto_resultado = tk.Label(ventana, text="")
texto_resultado.pack()

ventana.mainloop()


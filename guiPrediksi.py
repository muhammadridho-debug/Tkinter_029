import tkinter as tk

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")  

judul = tk.Label(top, text="Aplikasi prediksi Prodi Pilihan")
judul.grid(row=0, column=0, columnspan=2, pady=10)

L1 = tk.Label(top, text="Nilai Mapel 1: ")
L1.grid(row=1, column=0, sticky="w", padx=20, pady=2)
E1 = tk.Entry(top, bd=3)
E1.grid(row=1, column=1, padx=20, pady=2)

top.mainloop()
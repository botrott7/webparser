import tkinter as tk
import functions
from logs.logs import logger


def main():
    window = tk.Tk()
    window.title("Выбор результатов")

    # Загрузка результатов
    results = functions.load_results()

    # Создание полей выбора
    checkbuttons = []

    for i, result in enumerate(results):
        var = tk.BooleanVar()
        checkbutton = tk.Checkbutton(window, text=result, variable=var,
                                     command=lambda i=i: functions.checkbox_changed(i, checkbuttons)) # lambda i=i, явно сохраняет значение i
        checkbutton.grid(row=i // 15, column=i % 15, sticky="w")
        checkbuttons.append(var)

    button = tk.Button(window, text="Выбрать", command=lambda: functions.show_selection(checkbuttons, results),
                       height=2, bg="red", fg="white",
                       font=("Arial", 12, "bold"))
    button.grid(row=(len(results) - 1) // 3 + 1, column=6, columnspan=3, pady=10)

    window.mainloop()


if __name__ == "__main__":
    logger.info('START')
    main()

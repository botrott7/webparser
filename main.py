import tkinter as tk
import requests
from tkinter import ttk, RIGHT, Y

from bs4 import BeautifulSoup
from logs.logs import logger
from func import functions

RESULTS = []
URL = 'https://www.bestchange.net/wiki/rates.html'

try:
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='codetable')
    logger.info('HTML парсинг успешно завершен')
except requests.exceptions.RequestException as e:
    logger.error(f'Возникла ошибка при запросе к странице: {e}')
    raise SystemExit()


def main():
    try:
        window = tk.Tk()
        window.title("Выбор результатов")
        # Центрирование окна
        window_width = 570
        window_height = 800
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        # Создание скроллбара
        scrollbar = ttk.Scrollbar(orient='vertical')
        scrollbar.pack(side=RIGHT, fill=Y)
        # Создание полотна
        canvas = tk.Canvas(window, yscrollcommand=scrollbar.set)
        canvas.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=canvas.yview)
        # Создание фрейма для размещения полей выбора
        frame = tk.Frame(canvas)
        canvas.create_window(0, 0, anchor="nw", window=frame)

        # Загрузка результатов
        rows = table.find_all('tr')  # добавление этой строки
        for row in rows:
            cell = row.find('td', class_='oddleft')
            if cell:
                RESULTS.append(cell.text)

        # Создание полей выбора
        CHECKBUTTONS = []
        for i, result in enumerate(RESULTS):
            var = tk.BooleanVar()
            checkbutton = tk.Checkbutton(frame, text=result, variable=var,
                                         command=lambda i=i: functions.checkbox_changed(i,
                                                                                        CHECKBUTTONS))  # lambda i=i, явно сохраняет значение i
            checkbutton.grid(row=i // 7, column=i % 5, sticky="w")
            CHECKBUTTONS.append(var)

        button = tk.Button(window, text="Выбрать", command=lambda: functions.show_selection(CHECKBUTTONS, RESULTS),
                           height=2, bg="lime", fg="white",
                           font=("Arial", 12, "bold"))
        button.pack(pady=10)

        # Разрешение прокрутки полотна
        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        canvas.config(yscrollcommand=scrollbar.set)

        # Обновление обработчика событий прокрутки полотна
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)
        window.mainloop()
    except Exception as e:
        logger.exception("Произошла ошибка в main:", e)
        raise SystemExit()


if __name__ == "__main__":
    try:
        logger.info('START')
        main()
    except Exception as e:
        logger.exception("Произошла ошибка в точке входа")
        raise SystemExit()

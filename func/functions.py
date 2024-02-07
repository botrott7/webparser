from tkinter import messagebox
from logs.logs import logger

SELECTED_RESULTS = []


def show_selection(checkbuttons, results):
    '''Обработка выбора, вывод результата, очистка поля выбора'''
    try:
        selected_values = []
        for i, checkbutton in enumerate(checkbuttons):
            if checkbutton.get() and len(selected_values) < 2:
                selected_values.append(results[i])
        if len(selected_values) == 2:
            result = ''.join(selected_values)
            SELECTED_RESULTS.append(result)
            for checkbutton in checkbuttons:
                checkbutton.set(False)
        else:
            messagebox.showerror("Ошибка", "Выберите два значения")
        print(','.join([f'{index}{two}' for two, index in enumerate(SELECTED_RESULTS, start=1)]))
    except:
        logger.error("Произошла ошибка во время выполнения функции show_selection().")


def checkbox_changed(index, checkbuttons):
    '''Обработка события изменения флажка в поле выбора'''
    try:
        if checkbuttons[index].get():
            count = 0
            for i, checkbutton in enumerate(checkbuttons):
                if checkbutton.get():
                    count += 1
                    if count > 2:
                        checkbuttons[index].set(False)
                        messagebox.showerror("Ошибка", "Выбрано более двух значений")
                        return
                else:
                    checkbutton.set(False)
    except:
        logger.error("Произошла ошибка во время выполнения функции checkbox_changed().")

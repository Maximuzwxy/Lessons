import tkinter as tk
import time
# window = tk.Tk()
#
# window.title('lesson5')
# window.geometry('300x300')

# window.mainloop()

window = None
for i in range(5):
    window = tk.Tk()
    window.update()
    time.sleep(1)
window.title('lll')
window.mainloop()


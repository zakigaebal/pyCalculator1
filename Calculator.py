import tkinter as tk

from pandas import value_counts

calc = tk.Tk()
calc.title("Calculator")
calc.geometry("300x300")

def calculate(event):            # func 함수 작성
    value = tk.Entry.get(display)
    if value != '':
        result = eval(value)
        print(result)
        display.delete(0,tk.END) # 내용 삭제
        display.insert(0,result) # 새 값 입력

def clear(event):            # C 버튼과 Esc 키를 위한 함수입니다.
    display.delete(0,tk.END) # 내용 삭제

display = tk.Entry(calc, width=20)
display.pack()

button_e = tk.Button(calc, text='=', width=5) # = 버튼 추가
button_e.bind('<Button-1>',calculate)
button_e.pack()

button_c =tk.Button(calc, text='c', width=5)
button_c.bind('<Button-1>',clear)
button_c.pack()

calc.bind('<Return>', calculate)
# calc.bind('<Escape>',clear) # Esc 키도 c버튼과 통일한 기능을 하도록 연결해줬다.

calc.bind('<Return>' ,calculate) #엔터키 이벤트를 func 함수로 연결
calc.mainloop()
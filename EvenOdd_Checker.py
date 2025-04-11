import tkinter as tk


app = tk.Tk()
app.title("EvenOdd_Checkerl")
app.geometry("200x200")


def check_answerx():
    user_answer = entry.get()

    try:
        number = int(user_answer)
        if number % 2 == 0:
            result_label.config(text="เป็นเลขคู่")
        else:
            result_label.config(text="เป็นเลขคี่")
    except ValueError:
        result_label.config(text="กรุณากรอกตัวเลขจำนวนเต็มนะครับ.")


entry = tk.Entry(app) #ช่องกรอกตัวเลข
entry.pack(pady=5)

check_button = tk.Button(app, text="ตรวจเลขคู่หรือคี่", command=check_answerx) #ปุ่มตรวจสอบเลขคู่คี่ 
check_button.pack(pady=5) 

result_label = tk.Label(app, text="") #ช่องแสดงผลลัพท์
result_label.pack(pady=5)

app.mainloop()

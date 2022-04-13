import schedule
import time
# from tkinter import *
# from tkinter import messagebox
import ctypes

# window = Tk()

# def Click():
#     messagebox.showinfo("알림창", "코드 종료 되었습니다.")


def message1():
    print("Hello")

def message2():
    print("10초 지났습니다.")

job1 = schedule.every(1).seconds.do( message1 )
job2 = schedule.every(10).seconds.do( message2 )

count = 0
while True:
    schedule.run_pending() # pending된 job을 실행
    time.sleep(1)

    count += 1

    if count > 11:
        schedule.cancel_job(job1)
        print("코드 종료되었습니다.")

        # Click_button = Button(text='클릭', command=Click)
        # Click_button.pack()
        # window.mainloop()
        break

msg = ctypes.windll.user32.MessageBoxW(None, '코드가 종료 되었습니다.', '알림', 0)
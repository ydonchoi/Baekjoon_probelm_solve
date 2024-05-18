## GUI source code: 기러기토마토....님(파이썬기초코딩inBAND)
import tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, master):
        self.master = master
        self.cnt=0
        self.cor_ans=0
        master.title("암산왕 퀴즈 v.0.1")
        master.geometry("300x300")
       
        self.label = tk.Label(master, text="암산왕 퀴즈 v.0.1")
        self.label.grid(row=0, column=0, columnspan=2)

        self.generator_button = tk.Button(master, text="Number Generate", borderwidth=4, relief="raised", highlightcolor="green", command=self.generate)
        self.generator_button.grid(row=1, column=0, columnspan=2)
           
        self.num1_label = tk.Label(master, text="num1")
        self.num1_label.grid(row=2, column=0)
        self.num1_entry = tk.Entry(master)
        self.num1_entry.grid(row=2, column=1)
        
        self.num2_label = tk.Label(master, text="num2")
        self.num2_label.grid(row=3, column=0)
        self.num2_entry = tk.Entry(master)
        self.num2_entry.grid(row=3, column=1)

        self.ans_label = tk.Label(master, text="The Answer is: ")
        self.ans_label.grid(row=4, column=0)
        self.ans_entry = tk.Entry(master)
        self.ans_entry.grid(row=4, column=1)
        self.ans_button = tk.Button(master, text="Is it Correct?")
        self.ans_button.grid(row=5, column=0, columnspan=2, relief="raised", borderwidth=4, command=self.answer)

        self.result_label = tk.Label(master, text="Result")
        self.result_label.grid(row=7, column=0)
        self.result_text = tk.Text(master, height=10, width=40)
        self.result_text.grid(row=8, column=0, columnspan=2,padx=10)

        self.clear_button = tk.Button(master, text="Clear", relief="raised", borderwidth=4, command=self.clear)
        self.clear_button.grid(row=9, column=0)
        
        self.close_button = tk.Button(master, text="Close", relief="raised", borderwidth=4, command=self.close)
        self.close_button.grid(row=9, column=1)
            
    def generate(self):
        self.cnt+=1
        num1 = randint(1,100)
        self.num1_entry.insert(0,num1)
        num2 = randint(1,100)
        self.num2_entry.insert(0,num2)
        ans = self.ans_entry.get()
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, f"암산 결과:\n{num1} + {num2} = {ans}")
        if num1 + num2 == int(ans):
            print("정답입니다!")
            self.cor_ans+=1
        else: print(f'정답이 아닙니다.\n정답은 {num1+num2}입니다.')
        
        print(f'지금까지 모두 {self.cnt}번 참여하였습니다.\n지금까지의 성적은 {self.cor_ans/self.cnt*100}점 입니다.')
    
    def clear(self):
        self.result_text.delete(0, tk.END)
        self.generate()

    def close(self):
        self.master.destroy()
root = tk.Tk()
my_app = MyApp(root)
root.mainloop()    

    
    def on_key_press(event):
        print(f'Key Pressed: {event.char}')
        self.entry.bind("<Key>", on_key_press)
    
    def on_mouse_click(event):
        item=self.listbox.nearsr(event.y)
        print(f'Item clicked: {self.listbox.get(item)}')
        self.listbox.bind("<Button-1>", on_mouse_click)




# 22일차 암산왕 퀴즈 v.0.1
print("암산왕 퀴즈 v.0.1")
cnt=0
cor_ans=0
while True:
    cnt+=1
    print(f'\n{cnt}번째 연습\n*두 정수 모두 숫자 0을 입력하면 종료됩니다.')
    print("첫번째 숫자를 입력하세요: ", end="")
    a=int(input())
    print(a)
    print("두번째 숫자를 입력하세요: ", end="")
    b=int(input())
    print(b)
    if a==b==0:
        print('\n암산왕 v.0.1 프로그램 종료')
        break
    else:
        print(f'{a}+{b}를 암산하면? ', end="")
        c=int(input())
        print(c)
        if a+b==c:
            print("맞았습니다!")
            cor_ans+=1
        else:
            print(f"틀렸습니다. 정답은 {a+b}입니다.")
print(f'총 {cnt-1}번 참여하였습니다.\n최종 성적은 {round(cor_ans/cnt*100)}점 입니다.\n오늘도 좋은 하루 보내요:)')


# 22일차 암산왕 퀴즈 프로그램을 GUI로 구현하려면? 스스로에게 부과하는 별도 실습 과제 :)
# 연습 GOGO!!

help(tk.grid)

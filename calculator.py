from tkinter import *
from math import sin, cos

root = Tk()
root.title("Your REALLY LOW QUALITY Calculator!!!")
root.geometry("10000x10000")

nums = []

class calculator:
    def __init__(self, constant):
        ipadx = 88
        ipady = 60

        self.one = Button(constant, text=1, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                          command=self.add_1)
        self.one.grid(row=1, column=1, ipadx=ipadx, ipady=ipady)

        self.two = Button(constant, text=2, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                          command=self.add_2)
        self.two.grid(row=1, column=2, ipadx=ipadx, ipady=ipady)

        self.three = Button(constant, text=3, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                            command=self.add_3)
        self.three.grid(row=1, column=3, ipadx=ipadx, ipady=ipady)

        self.four = Button(constant, text=4, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                           command=self.add_4)
        self.four.grid(row=1, column=4, ipadx=ipadx, ipady=ipady)

        self.five = Button(constant, text=5, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                           command=self.add_5)
        self.five.grid(row=2, column=1, ipadx=ipadx, ipady=ipady)

        self.six = Button(constant, text=6, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                          command=self.add_6)
        self.six.grid(row=2, column=2, ipadx=ipadx, ipady=ipady)

        self.seven = Button(constant, text=7, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                            command=self.add_7)
        self.seven.grid(row=2, column=3, ipadx=ipadx, ipady=ipady)

        self.eight = Button(constant, text=8, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                            command=self.add_8)
        self.eight.grid(row=2, column=4, ipadx=ipadx, ipady=ipady)

        self.nine = Button(constant, text=9, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                           command=self.add_9)
        self.nine.grid(row=3, column=1, ipadx=ipadx, ipady=ipady)

        self.zero = Button(constant, text=0, font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                           command=self.add_0)
        self.zero.grid(row=3, column=2, ipadx=ipadx, ipady=ipady)

        self.space = Label(constant)
        self.space.grid(row=0, ipady=100)

        self.delete = Button(constant, text="Del", font=("Bahnschrift Condensed", 15), bg="gray",
                             activebackground="#5f7a67", command=self.delete_num)
        self.delete.grid(row=3, column=3, ipadx=(ipadx - 6), ipady=ipady)

        self.clear = Button(constant, text="Clear", font=("Bahnschrift Condensed", 15), bg="gray",
                            activebackground="#5f7a67", command=self.clear_screen)
        self.clear.grid(row=3, column=4, ipadx=(ipadx - 14), ipady=ipady)

        self.plus = Button(constant, text="+", font=("Bahnschrift Condensed", 15), bg="gray",
                           activebackground="#5f7a67",
                           command=self.add_num)
        self.plus.grid(row=1, column=5, ipadx=ipadx, ipady=ipady)

        self.subtract = Button(constant, text="-", font=("Bahnschrift Condensed", 15), bg="gray",
                               activebackground="#5f7a67", command=self.subtract_nums)
        self.subtract.grid(row=2, column=5, ipadx=ipadx, ipady=ipady)

        self.multiply = Button(constant, text="*", font=("Bahnschrift Condensed", 15), bg="gray",
                               activebackground="#5f7a67", command=self.mult_nums)
        self.multiply.grid(row=3, column=5, ipadx=ipadx, ipady=ipady)

        self.divide = Button(constant, text="/", font=("Bahnschrift Condensed", 15), bg="gray",
                             activebackground="#5f7a67", command=self.div_nums)
        self.divide.grid(row=1, column=6, ipadx=ipadx, ipady=ipady)

        self.output=Label(constant, text="", font=("@Microsoft JhengHei", 20), bg="red", fg="navy")
        self.output.place(relwidth=1, relheight=.3)

        self.equal=Button(constant, text="=", font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                          command=self.answer)
        self.equal.grid(row=2, column=6, ipadx=ipadx, ipady=ipady)

        self.left_paren=Button(constant, text="(", font=("Bahnschrift Condensed", 15), bg="gray",
                               activebackground="#5f7a67", command=self.add_left_paren)
        self.left_paren.grid(row=3, column=6, ipadx=ipadx, ipady=ipady)

        self.right_paren=Button(constant, text=")", font=("Bahnschrift Condensed", 15), bg="gray",
                                activebackground="#5f7a67", command=self.add_right_paren)
        self.right_paren.grid(row=3, column=7, ipadx=ipadx, ipady=ipady, sticky="w")

        self.sin=Button(constant, text="sin", font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                        command=self.calculate_sin)
        self.sin.grid(row=1, column=7, ipadx=ipadx, ipady=ipady, sticky="nw")

        self.cos=Button(constant, text="cos", font=("Bahnschrift Condensed", 15), bg="gray", activebackground="#5f7a67",
                        command=self.calculate_cos)
        self.cos.grid(row=2, column=7, ipadx=ipadx, ipady=ipady, sticky="n")

    def add_1(self):
        nums.append(1)
        self.output.config(text=nums)

    def add_2(self):
        nums.append(2)
        self.output.config(text=nums)

    def add_3(self):
        nums.append(3)
        self.output.config(text=nums)

    def add_4(self):
        nums.append(4)
        self.output.config(text=nums)

    def add_5(self):
        nums.append(5)
        self.output.config(text=nums)

    def add_6(self):
        nums.append(6)
        self.output.config(text=nums)

    def add_7(self):
        nums.append(7)
        self.output.config(text=nums)

    def add_8(self):
        nums.append(8)
        self.output.config(text=nums)

    def add_9(self):
        nums.append(9)
        self.output.config(text=nums)

    def add_0(self):
        nums.append(0)
        self.output.config(text=nums)

    def delete_num(self):
        try:
            nums.pop(-1)
            self.output.config(text=nums)
        except IndexError:
            self.output.config(text="There are no more values to delete")

    def clear_screen(self):
        nums.clear()
        self.output.config(text=nums)

    def add_num(self):
        nums.append("+")
        self.output.config(text=nums)

    def subtract_nums(self):
        nums.append("-")
        self.output.config(text=nums)

    def mult_nums(self):
        nums.append("*")
        self.output.config(text=nums)

    def div_nums(self):
        nums.append("/")
        self.output.config(text=nums)

    def answer(self):
        ans = ""
        try:
            for i in self.output["text"]:
                if i == " ":
                    continue
                else:
                    ans += i
            ans = eval(ans)
            self.output.config(text=ans)

        except ValueError:
            self.output.config(text="Invalid input")
        except ZeroDivisionError:
            self.output.config(text="You can't divide by Zero")
        except SyntaxError as syntaxERROR:
            self.output.config(text=syntaxERROR)
        except Exception:
            self.output.config(text="Something went wrong")

    def add_left_paren(self):
        nums.append("(")
        self.output.config(text = nums)

    def add_right_paren(self):
        nums.append(")")
        self.output.config(text = nums)

    def calculate_sin(self):
        nums.append("sin(")
        self.output.config(text = nums)

    def calculate_cos(self):
        nums.append("cos(")
        self.output.config(text = nums)

def main():
    c = calculator(root)
    mainloop()

main()

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE = "students.json"
students = []

PROGRAMS = ["BS INFORMATION TECHNOLOGY", "BET CIVIL TECHNOLOGY", "BET AUTOMOTIVE TECHNOLOGY", "BET MECHANICAL TECHNOLOGY", "BET ELECTRICAL TECHNOLOGY", "BET DRAFTING TECHNOLOGY"]

def load():
    global students
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            try:
                students = json.load(f)
            except:
                students = []

def save():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

root = tk.Tk()
root.title("Student System")
root.geometry("1000x600")
root.config(bg="white")

def clear():
    for w in root.winfo_children():
        w.destroy()

def main_menu():
    clear()

    container = tk.Frame(root, bg="white", bd=1, relief="solid")
    container.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    tk.Label(container, text="STUDENT SYSTEM",
             font=("Arial", 20, "bold"),
             bg="white").pack(pady=25)

    tk.Button(container, text="ADD STUDENT", command=add_student,
              width=30, height=2, bg="white", bd=1).pack(pady=8)

    tk.Button(container, text="STUDENT LIST", command=student_list,
              width=30, height=2, bg="white", bd=1).pack(pady=8)

    tk.Button(container, text="UPDATE STUDENT", command=update_student,
              width=30, height=2, bg="white", bd=1).pack(pady=8)

    tk.Button(container, text="RESULT PAGE", command=result_page,
              width=30, height=2, bg="white", bd=1).pack(pady=8)
    
    tk.Button(container, text="DELETE STUDENT", command=delete_student,
            
              width=30, height=2, bg="white", bd=1).pack(pady=8)
    
    tk.Button(container, text="EXIT", command=root.quit,
              width=30, height=2, bg="white", bd=1).pack(pady=15)

def add_student():
    clear()

    frame = tk.Frame(root, bg="white", bd=1, relief="solid")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    tk.Label(frame, text="ADD STUDENT",
             font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    form = tk.Frame(frame, bg="white")
    form.pack()

    def row(label):
        r = tk.Frame(form, bg="white")
        r.pack(pady=2)
        tk.Label(r, text=label, bg="white", width=10, anchor="w").pack(side="left")
        e = tk.Entry(r, width=25)
        e.pack(side="left")
        return e

    name = row("Name:")
    sr = row("SR-Code:")

    pr = tk.Frame(form, bg="white"); pr.pack(pady=2)
    tk.Label(pr, text="Program:", bg="white", width=10, anchor="w").pack(side="left")
    program = ttk.Combobox(pr, values=PROGRAMS, state="readonly", width=22)
    program.pack(side="left")

    course = row("Course:")
    p = row("Prelim:")
    m = row("Midterm:")
    f = row("Finals:")

    msg = tk.Label(frame, text="", bg="white")
    msg.pack(pady=5)

    def save_student():
        if name.get()=="" or sr.get()=="" or program.get()=="" or course.get()=="":
            msg.config(text="Complete all fields", fg="black")
            return

        for s in students:
            if s["sr"] == sr.get():
                msg.config(text="SR exists", fg="black")
                return

        try:
            avg = (float(p.get()) + float(m.get()) + float(f.get())) / 3
        except:
            msg.config(text="Invalid grades", fg="black")
            return

        students.append({
            "name": name.get(),
            "sr": sr.get(),
            "program": program.get(),
            "course": course.get(),
            "prelim": float(p.get()),
            "midterm": float(m.get()),
            "finals": float(f.get()),
            "average": round(avg, 2)
        })

        save()
        msg.config(text="SAVED", fg="black")

    btns = tk.Frame(frame, bg="white")
    btns.pack(pady=10)

    tk.Button(btns, text="SAVE", command=save_student,
              width=12, bg="white", bd=1).pack(side="left", padx=5)

    tk.Button(btns, text="BACK", command=main_menu,
              width=12, bg="white", bd=1).pack(side="left", padx=5)
    
def student_list():
    clear()

    frame = tk.Frame(root, bg="white", bd=1, relief="solid")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    tk.Label(frame, text="STUDENT LIST",
             font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    cols = ("SR", "Name", "Program", "Course")

    tree = ttk.Treeview(frame, columns=cols, show="headings", height=12)
    tree.pack()

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=100)

    for s in students:
        tree.insert("", "end",
                    values=(s["sr"], s["name"], s["program"], s["course"]))

    btns = tk.Frame(frame, bg="white")
    btns.pack(pady=10)

    tk.Button(btns, text="BACK", command=main_menu,
              width=20, bg="white", bd=1).pack()
    
def update_student():
    clear()

    frame = tk.Frame(root, bg="white", bd=1, relief="solid")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    tk.Label(frame, text="UPDATE STUDENT",
             font=("Arial", 18, "bold"), bg="white").pack()

    tk.Label(frame, text="SR-Code:", bg="white").pack()
    sr = tk.Entry(frame)
    sr.pack()

    def find():
        for s in students:
            if s["sr"] == sr.get():
                messagebox.showinfo("FOUND",
                    f"{s['name']}\n{s['course']}\nAVG: {s['average']}")
                return
        messagebox.showerror("ERROR", "NOT FOUND")

    btns = tk.Frame(frame, bg="white")
    btns.pack(pady=10)

    tk.Button(btns, text="SEARCH", command=find,
              width=12, bg="white", bd=1).pack(side="left", padx=5)

    tk.Button(btns, text="BACK", command=main_menu,
              width=12, bg="white", bd=1).pack(side="left", padx=5)
    
def result_page():
    clear()

    frame = tk.Frame(root, bg="white", bd=1, relief="solid")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    tk.Label(frame, text="RESULT PAGE",
             font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    search_var = tk.StringVar()

    ttk.Combobox(frame, values=PROGRAMS,
                 textvariable=search_var,
                 state="readonly").pack()

    cols = ("SR", "Name", "Program", "Course", "Avg")

    tree = ttk.Treeview(frame, columns=cols, show="headings", height=10)
    tree.pack()

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=100)

    def load_all():
        tree.delete(*tree.get_children())
        for s in students:
            tree.insert("", "end",
                        values=(s["sr"], s["name"], s["program"], s["course"], s["average"]))

    load_all()

    def search():
        tree.delete(*tree.get_children())
        prog = search_var.get()

        if prog == "":
            load_all()
            return

        for s in students:
            if s["program"] == prog:
                tree.insert("", "end",
                            values=(s["sr"], s["name"], s["program"], s["course"], s["average"]))

    def view():
        sel = tree.selection()
        if not sel:
            return

        data = tree.item(sel)["values"]

        for s in students:
            if s["sr"] == data[0]:
                messagebox.showinfo("RESULT",
                    f"{s['name']}\n{s['sr']}\n{s['program']}\n{s['course']}\n"
                    f"{s['prelim']} {s['midterm']} {s['finals']}\nAVG {s['average']}")
                return

    btns = tk.Frame(frame, bg="white")
    btns.pack(pady=5)

    tk.Button(btns, text="SEARCH", command=search,
              width=10, bg="white", bd=1).pack(side="left", padx=5)

    tk.Button(btns, text="BACK", command=main_menu,
              width=10, bg="white", bd=1).pack(side="left", padx=5)

def delete_student():
    clear()

    frame = tk.Frame(root, bg="white", bd=1, relief="solid")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    tk.Label(frame, text="DELETE STUDENT",
             font=("Arial", 18, "bold"),
             bg="white").pack(pady=10)

    tk.Label(frame, text="Enter SR-Code:", bg="white").pack()
    sr = tk.Entry(frame)
    sr.pack()

    result = tk.Label(frame, text="", bg="white")
    result.pack(pady=10)

    def delete():
        for s in students:
            if s["sr"] == sr.get():

                confirm = messagebox.askyesno(
                    "CONFIRM DELETE",
                    f"Delete {s['name']}?"
                )

                if confirm:
                    students.remove(s)
                    save()
                    result.config(text="DELETED", fg="black")
                return

        result.config(text="NOT FOUND", fg="black")

    btns = tk.Frame(frame, bg="white")
    btns.pack(pady=10)

    tk.Button(btns, text="DELETE", command=delete,
              width=12, bg="white", bd=1).pack(side="left", padx=5)

    tk.Button(btns, text="BACK", command=main_menu,
              width=12, bg="white", bd=1).pack(side="left", padx=5)
load()
main_menu()
root.mainloop()
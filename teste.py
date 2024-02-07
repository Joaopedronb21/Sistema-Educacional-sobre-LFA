import tkinter as tk
from tkinter import messagebox


class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Automato a Pilha: Quiz")
        self.master.geometry("400x300")
        self.questions = questions
        self.score = 0
        self.current_question_index = 0
        self.correct_answers = []  
        self.wrong_answers = [] 

        self.label_pergunta = tk.Label(master, text="")
        self.label_pergunta.pack()

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(master, text="", variable=self.radio_var, value="", command=self.check_answer)
            radio_button.pack(anchor=tk.W)
            self.radio_buttons.append(radio_button)

        self.next_button = tk.Button(master, text="Próxima Pergunta", command=self.next_question)
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            current_question = self.questions[self.current_question_index]
            self.label_pergunta.config(text=current_question["question"])
            options = current_question["options"]
            for i in range(4):
                self.radio_buttons[i].config(text=f"{chr(65 + i)}. {options[i]}", value=chr(65 + i))
        else:
            self.show_result()

    def check_answer(self):
        if self.radio_var.get() == self.questions[self.current_question_index]["correct_option"]:
            self.score += 1
            self.correct_answers.append(self.current_question_index)
            self.next_button.config(text="Próxima Pergunta", command=self.next_question)
        else:
            correct_option = self.questions[self.current_question_index]["correct_option"]
            self.wrong_answers.append(self.current_question_index)
            #messagebox.showinfo("Resposta Incorreta", f"Ops! A resposta correta era {correct_option}.")
            self.next_button.config(text="Próxima Pergunta", command=self.next_question)

    def next_question(self):
        self.current_question_index += 1
        self.radio_var.set(None)
        self.show_question()

    def show_result(self):
        result_message = f"Sua pontuação final é: {self.score}/{len(self.questions)}\n"
        result_message += "Questões corretas:\n"
        for index in self.correct_answers:
            result_message += f"- {self.questions[index]['question']}\n"
        result_message += "\nQuestões erradas:\n"
        for index in self.wrong_answers:
            result_message += f"- {self.questions[index]['question']}\n"
        messagebox.showinfo("Resultado Final", result_message)
        self.master.destroy()
questions = [
    {
        "question": "Na descrição formal de um AP o 'q0' representa: ",
        "options": ["Estado Final", "Quantidade de estados", "Estado Inicial", "Alfabeto"],
        "correct_option": "C"
    },
    {
        "question": "Um AP possui 3 elementos, eles são:",
        "options": ["Fita/Cabeçote/Pilha","Alfabeto/Pilha/Memória","Controle finito de estados/Fita/Cabeçote",
                    "Controle finito de estados/Fita/Pilha"],
        "correct_option":"D"
    },
    {
       "question": "Quando um AP encerra a operação?",
       "options": ["Quando a pilha estiver vazia, independente do estado ","Quando o automato chega no estado final",
                   "Quando o cabeçote estiver na primeira posição e o AP no estado final",
                   "Quando a pilha estiver vazia, e o AP no estado final"],
       "correct_option": "A"
    },
    {
        "question": "Um AP possui estado final?",
        "options": ["Sim", "Não","Pode ter ou não, depende da necessidade","Apenas quando tem 4 letras no alfabeto"],
        "correct_option": "B"
    },
    {
        "question": "Qual palavra seria aceita para esse alfabeto: {a^n b^n| n > 0 }",
        "options": ["abb", "aaabbb", "aaab", "bba"],
        "correct_option": "B"
    },
    {
        "question": "Qual palavra seria aceita para esse alfabeto: {a^n b^m | n > 0, m > 0}",
        "options": ["bbaaa", "aab", "aaa", "bb"],
        "correct_option": "B"
    },
    {
        "question": "Qual palavra seria aceita para esse alfabeto: {a^i b^j c^k | i=j+k, j > 0, k > 0}",
        "options": ["abbcc", "aabbbbcc", "abcc", "aaabcc"],
        "correct_option": "D"
    },
    {
        "question": "Qual palavra seria aceita para esse alfabeto: {a^n b^m c^m | n > 0, m >= 0}",
        "options": ["bbcc", "aabb", "aaaaaa", "aaacc"],
        "correct_option": "C"
    },
    {
        "question": "Qual seria o alfabeto que essa palavra seria aceita 'aabbbbcc'",
        "options": ["{a^i b^j c^k | i=j+k, j > 0, k > 0}", "{a^i b^j c^k | i > 0, j = i+k, k > 0}", 
                    "{a^n b^m c^m | n > 0, m > 0}", "{a^n b^n c^n | n > 0}"],
        "correct_option": "B"
    },
    {
        "question":"Qual seria o alfabeto que essa palavra seria aceita 'aabbbcdddd'",
        "options":["{a^n b^3m c^m d^2n | n > 0, m > 0}","{a^n b^m c^n d^m+1 | n > 0, m > 0}",
                   "{a^n b^n c^m d^2m | n > 0, m > 0}","{a^n b^3n c^n d^2n | n > 0}"],
        "correct_option":"A"
    },
]   

with open('C:\\Users\\Usuario\\Sistema-Educacional-sobre-LFA\\sobre.txt', 'r') as arquivo:
    texto = arquivo.read()

class Sobre:
    def __init__(self, master):
        self.master = master
        self.master.title("Automato a Pilha: SOBRE")   
        self.master.geometry("700x500")
        self.master.configure(bg='lightgray')
        self.scrollbar = tk.Scrollbar(master, orient="vertical")

        self.canvas = tk.Canvas(master, bg='lightgray', width=800, height=800)
        self.canvas.pack(side="left", fill="both", expand= True)
        self.scrollbar.config(command=self.canvas.yview)
        

        self.exibir_conteudo()

    def exibir_conteudo(self):
        self.canvas.create_text(350, 120, text=texto, font=("Arial", 12), fill="black")

class TelaInicial:
    def __init__(self, master):
        self.master = master
        self.master.title("Automato a Pilha: Menu")
        self.master.geometry("400x300")
        self.master.configure(bg='lightgray')

        self.label = tk.Label(master, text="LFA PROJECT: AP")
        self.label.pack()
        self.label.config(font=("Arial", 20), foreground="white", background="grey",
                          anchor=tk.W, relief=tk.GROOVE, bd=10, padx=100, pady=10)

        self.botao1 = tk.Button(master, text="Quiz", command=self.iniciar_quiz)
        self.botao1.pack(pady=10)
        self.botao1.config(font=("Arial Black", 20), foreground="blue", background="lightblue", anchor='center')

        self.botao2 = tk.Button(master, text="SOBRE", command=self.acao_botao2)
        self.botao2.pack(pady=10)
        self.botao2.config(font=("Arial Black", 20), foreground="blue", background="lightblue", anchor='center')

    def iniciar_quiz(self):
        quiz_window = tk.Toplevel(self.master)
        quiz_app = Quiz(quiz_window)

    def acao_botao2(self):
        sobre_window = tk.Toplevel(self.master)
        sobre_app = Sobre(sobre_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()
from tkinter import*
import matplotlib.pyplot as plt
from functools import partial
import os
import pandas as pd
class analize:
    def __init__(self, root,file):
        self.root = root
        self.file=file
        self.clear_view();
        self.create_view()
    def set_diagram(self):
        plt.style.use('seaborn')
        file= "csv/" + str(self.file)
        df = pd.read_csv(file)
        dates = df.date
        y=df.new
        y2=df['new deads']
        y3 = df['curred']
        plt.plot_date(dates,y,linestyle='solid',color='y')
        plt.plot_date(dates, y2, linestyle='solid',color='r')
        plt.plot_date(dates, y3, linestyle='solid',color='g')
        plt.show()
    def get_data(self,index,key):
        plt.style.use('seaborn')
        file= "csv/" + str(self.file)
        df = pd.read_csv(file)
        return df[key][index];
    def create_view(self):
        self._generate_Form([
            ['Cantry', self.get_data(0,'data')],
            ['Top Cases 1M ', self.get_data(1,'data')],
            ['Top Deaths 1M ', self.get_data(2,'data')],
            ['Daily tests', self.get_data(0,'tests')],
            ['Total tests', self.get_data(1, 'tests')],
            ['Tests procent', self.tests_procents()]
        ])
        btn = Button(self.root, text='show diagram', command=self.set_diagram)
        btn.grid(column=0, row=100)
    def _generate_Form(self,from_List):
        colum=0
        row=0
        for item in from_List:
            form_elment = Label(self.root, text=item[0])
            form_elment.grid(column=colum, row=row)
            form_elment = Label(self.root, text=item[1])
            colum=colum+10
            form_elment.grid(column=colum, row=row)
            colum = colum - 10
            row=row+1
    def tests_procents(self):
        plt.style.use('seaborn')
        file= "csv/" + str(self.file)
        df = pd.read_csv(file)
        Infected= len(df['new']);
        last=df['new'][Infected-1];
        result=last/12500*100;
        result=round(result, 2)
        return  str(result)+'%'
    def clear_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
class Start:
    def __init__(self,root):
        self.run();
        self.root=root
        root.title("Corono Analizer")
        root.geometry('350x200')
    def clicked(self,file):
        analize(self.root,file)
    def run(self):
        lbl = Label(root, text="Chose File")
        lbl.grid(column=0, row=0)
        arr = os.listdir("csv")
        row=0;
        for item in arr:
            actionarguments = partial(self.clicked, item)
            btn = Button(root, text=item, command=actionarguments)
            btn.grid(column=0, row=row)
            row=row+1
if __name__=='__main__':
    root = Tk()
    application=Start(root)
    root.mainloop();
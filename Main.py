import tkinter as tk
import Searcher_lib as Cardmarket
from glob import glob

OP_EDITIONS = ["Romance-Dawn","Paramount-War","Pillars-of-Strength","Pillars-of-Strength-Japanese","Kingdoms-of-Intrigue","Kingdoms-of-Intrigue-Japanese","Awakening-of-the-New-Era-Japanese"]

class HomePage:

    

    def __init__(self,root):
        self.root = root
        self.frame = tk.Frame(self.root)

        self.frame.pack()
        

        self.card_List_Viewer = tk.Listbox(self.frame)
        self.card_List_Viewer.pack(side="left",anchor="n")

        self.edition_List_Viewer = tk.Listbox(self.frame)
        self.edition_List_Viewer.pack(side="left",anchor="n")

        for x in OP_EDITIONS:
            self.edition_List_Viewer.insert("end",x)

        self.card_List_Scrollbar = tk.Scrollbar(self.frame)
        self.card_List_Scrollbar.pack( side = "right", fill="y")

        self.update_Card_List = tk.Button(self.frame, text="Seleziona edizione", command=self.get_selected_edition)
        self.update_Card_List.pack()


    def empty_Card_List(self):    
        return self.card_List_Viewer.delete(0,"end")
    
    def set_Card_List(self,data):
       
        for x in data:
            self.card_List_Viewer.insert("end",x)
        return data
    
    def get_selected_edition(self):
        selected_indices = self.edition_List_Viewer.curselection()
        if(selected_indices):
            selected_index = selected_indices[0]
            selected_edition = self.edition_List_Viewer.get(selected_index)
            file_name = selected_edition + ".csv"
            self.empty_Card_List()
            self.set_Card_List(Cardmarket.read_csv_data(file_name))
            


if __name__=="__main__":
    root = tk.Tk()
    app = HomePage(root)
    
    root.mainloop()







#left_frame = Frame(root,width=400, height=600)
#left_frame.grid(row=0,column=0,padx=10,pady=5)

#Label(left_frame,text="GIAPPO").grid(row=0,column=0,padx=5,pady=5)
#j = 2
#jp_data_show_list = Listbox(root,yscrollcommand=scrollbar.set)
#for x in JP_List:
#    jp_data_show_list.insert(END,x)
#    j+=1

#Label(left_frame,text="BREEESH").grid(row=0,column=1,padx=5,pady=5)
#j = 2
#en_data_show_list = Listbox(root,yscrollcommand=scrollbar.set)
#for x in EN_List:
#    en_data_show_list.insert(END,x)
#    j+=1

#jp_data_show_list.pack( side = LEFT, fill = BOTH )
#en_data_show_list.pack( side = LEFT, fill = BOTH )
#scrollbar.config( command = jp_data_show_list.yview )

root.mainloop()
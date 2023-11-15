import tkinter as tk
import Searcher_lib as Cardmarket
from glob import glob

OP_EDITIONS = ["Romance-Dawn","Paramount-War","Pillars-of-Strength","Pillars-of-Strength-Japanese","Kingdoms-of-Intrigue","Kingdoms-of-Intrigue-Japanese","Awakening-of-the-New-Era-Japanese"]


class HomePage:

    

    def __init__(self,root):

        self.current_edition = ""

        self.root = root
        self.frame = tk.Frame(self.root)



        self.frame.pack()
        

        self.card_List_Viewer = tk.Listbox(self.frame,height=30)
        self.card_List_Viewer.pack(side="right")
        self.card_List_Viewer.bind("<<ListboxSelect>>",self.get_selected_card)

        self.edition_List_Viewer = tk.Listbox(self.frame,height=7)
        self.edition_List_Viewer.pack(side="right")
        self.edition_List_Viewer.bind("<<ListboxSelect>>",self.get_selected_edition)

        



        for x in OP_EDITIONS:
            self.edition_List_Viewer.insert("end",x)

        self.card_List_Scrollbar = tk.Scrollbar(self.frame)
        self.card_List_Scrollbar.pack( side = "right", fill="y")

        self.card_data_JP = tk.Text(self.frame)
        self.card_data_JP.pack(side = "left")

        self.card_data_EN = tk.Text(self.frame)
        self.card_data_EN.pack(side = "left")

    def empty_Card_List(self):    
        return self.card_List_Viewer.delete(0,"end")
    def empty_Card_Data_JP(self):    
        return self.card_data_JP.delete('1.0',"end")
    def empty_Card_Data_EN(self):    
        return self.card_data_EN.delete('1.0',"end")
    
    
    def set_Card_List(self,data):
       
        for x in data:
            self.card_List_Viewer.insert("end",x)
        return data
    
    def get_selected_edition(self,event=' '):
        selected_indices = self.edition_List_Viewer.curselection()
        if(selected_indices):
            selected_index = selected_indices[0]
            selected_edition = self.edition_List_Viewer.get(selected_index)
            file_name = selected_edition + ".csv"
            self.current_edition= selected_edition
            
            self.empty_Card_List()
            self.set_Card_List(Cardmarket.read_csv_data(file_name))

    def get_selected_card(self,event=' '):
        selected_indices = self.card_List_Viewer.curselection()
        if(selected_indices):
            selected_index = selected_indices[0]
            selected_card = self.card_List_Viewer.get(selected_index)
            
            JP_List, EN_List = Cardmarket.retrive_sellers_data_for_card(selected_card[0],self.current_edition)
            self.empty_Card_Data_JP()
            self.empty_Card_Data_EN()
            for x in JP_List:
                self.card_data_JP.insert("end",x)
            for x in EN_List:
                self.card_data_EN.insert("end",x)
            




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
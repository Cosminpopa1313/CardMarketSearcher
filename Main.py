from tkinter import *
import Searcher_lib as Iterator

print(Iterator.create_csv_from_Cardmarket(Iterator.retrive_cardname_fromedition("Awakening-of-the-New-Era-Japanese"),"Awakening-of-the-New-Era-Japanese.csv"))




root = Tk()
root.title("ONE PIECE CARDMARKET")

root.minsize(1920,1080)
root.config(bg="skyblue")





























"""
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y)

#left_frame = Frame(root,width=400, height=600)
#left_frame.grid(row=0,column=0,padx=10,pady=5)

#Label(left_frame,text="GIAPPO").grid(row=0,column=0,padx=5,pady=5)
j = 2
jp_data_show_list = Listbox(root,yscrollcommand=scrollbar.set)
for x in JP_List:
    jp_data_show_list.insert(END,x)
    j+=1

#Label(left_frame,text="BREEESH").grid(row=0,column=1,padx=5,pady=5)
j = 2
en_data_show_list = Listbox(root,yscrollcommand=scrollbar.set)
for x in EN_List:
    en_data_show_list.insert(END,x)
    j+=1

jp_data_show_list.pack( side = LEFT, fill = BOTH )
en_data_show_list.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = jp_data_show_list.yview )
"""
#root.mainloop()
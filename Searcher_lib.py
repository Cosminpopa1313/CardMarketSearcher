from urllib.request import Request,urlopen
import re
from tkinter import *
import csv



def retrive_sellers_data_for_card(url,language_filter):

    
    page_pattern = '<div id="articleRow.*?<div class="actions-container.*?</div></div></div>'

    extended_name_pattern = '<span class="seller-name d-flex".*?<a href=".*?</a>'
    name_pattern ='/Users/.*?"'

    offer_pattern = '<div class="price-container.*?</span>'
    price_container_pattern = '<span.*?<'
    price_pattern = '>.*?€'


    product_attributes_pattern = '<div class="product-attributes.*?<span style.*?</span></div>'
    language_pattern = 'data-original-title=".*?"'


    req = Request(
        url = "https://www.cardmarket.com/it/OnePiece/Products/Singles/Romance-Dawn/MonkeyDLuffy-OP01-024-V1",
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    page = urlopen(req).read()
    html = page.decode("utf-8")


    JP_List = []
    EN_List = []
    language_List=[]

    #dati di tutta la righa
    row_data = re.findall(page_pattern,html,re.IGNORECASE)


    for x in row_data:
        #dati degli attributi
        matches = re.search(product_attributes_pattern,x,re.IGNORECASE)
        attributes = matches.group()
        #lingua
        matches = re.search(language_pattern,attributes,re.IGNORECASE)
        language = matches.group()
        language = re.sub('data-original-title="',"",language)
        language = re.sub('"',"",language)
        language_List.append(language)
        #tag per il nome
        matches = re.search(extended_name_pattern,x,re.IGNORECASE)
        extended_name_data = matches.group()
        #il nome
        matches = re.search(name_pattern,extended_name_data,re.IGNORECASE)
        name = matches.group()
        #rimozione eccessi nome
        name = re.sub("/Users/","",name)
        name = re.sub('"',"",name)
        #dati del offerta/prezzo
        matches = re.search(offer_pattern,x,re.IGNORECASE)
        offer = matches.group()
        #contenitore del prezzo
        matches = re.search(price_container_pattern,offer,re.IGNORECASE)
        price_container = matches.group()
        #prezzo
        matches = re.search(price_pattern,price_container,re.IGNORECASE)
        price = matches.group()
        #rimozione eccessi prezzo
        price = re.sub("€","",price)
        price = re.sub('>',"",price)


        if(language == "Giapponese"):
            JP_List.append([name,price])
        elif (language =="Inglese"):
            EN_List.append([name,price])

    return JP_List,EN_List

    
def retrive_cardname_fromedition(edition):

    Card_List =[]
    Singles_url = "/Singles/"+edition+"/"
    for x in range(8):

        product_row_pattern = '<div id="productRow.*?Singles/.*?>'
        card_name_url_pattern = '/Singles/'+edition+'/.*"'        

        req = Request(
            url = "https://www.cardmarket.com/it/OnePiece/Products/Singles/"+edition+"?idRarity=0&sortBy=collectorsnumber_asc&site="+str(x+1),
            headers={'User-Agent': 'Mozilla/5.0'}
        )

        page = urlopen(req).read()
        html = page.decode("utf-8")
        print("Site Link Created!")
        #tira fuori le righe dei prodotti
        row_data = re.findall(product_row_pattern,html,re.IGNORECASE)
        for x in row_data:
            #tira fuori il nome con l'url
            matches = re.search(card_name_url_pattern,x,re.IGNORECASE)
            card_name_url = matches.group()
            card_name = re.sub(Singles_url,"",card_name_url)
            card_name = re.sub('"',"",card_name)
            Card_List.append(card_name)
    
    
    
    return Card_List

def create_csv_from_Cardmarket(data_origin,file_name):

    with open(file_name,'w',newline='') as file:
        writer = csv.writer(file)
        
        data = data_origin
        for x in data:

            writer.writerow([x])
        

    return "File creato!"
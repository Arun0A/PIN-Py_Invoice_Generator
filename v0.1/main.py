import tkinter as tk
from tkinter import ttk
from os import system
from pyautogui import alert, confirm
import verify
import saves

def upload():
    if bName.get() and bEmail.get() and bAddr.get() and bPhone.get() and bNum.get():
        with open('temp.py','w') as f:
            f.write(f"""eName = '{eName.get()}' 
date = '{datepick.get()}-{monthpick.get()}-{yearpick.get()}'
invoicenum = '{invoicenum.get()}'
bName = '{bName.get()}'
bEmail = '{bEmail.get()}'
bAddr = '{bAddr.get()}'
bState = '{bState.get()}'
bPhone = '{bPhone.get()}'
bNum = '{bNum.get()}'
color = '{colorpick.get()}'
btName = '{btName.get()}'
btAddr = '{btAddr.get()}'
btPhone = '{btPhone.get()}'
btEmail = '{btEmail.get()}'
stName = '{stName.get()}'
stAddr = '{stAddr.get()}'
stPhone = '{stPhone.get()}'
Discount = '{discount.get()}'
TaxRate = '{taxrate.get()}'
Shipping = '{shipping.get()}'
Info = '{info.get()}'
destPdf = r'{destpdf.get()}'\n""")
        alert('Uploaded')
    else:
        alert('Upload Error: All Values Not Provided; provide space if null')

def uploadsave():
    with open('saves.py','w') as f:
        f.write(f"""eName = '{eName.get()}' 
datepick = '{datepick.get()}'
monthpick = '{monthpick.get()}'
yearpick = '{yearpick.get()}'
invoicenum = '{invoicenum.get()}'
bName = '{bName.get()}'
bEmail = '{bEmail.get()}'
bAddr = '{bAddr.get()}'
bState = '{bState.get()}'
bPhone = '{bPhone.get()}'
bNum = '{bNum.get()}'
btName = '{btName.get()}'
btAddr = '{btAddr.get()}'
btPhone = '{btPhone.get()}'
btEmail = '{btEmail.get()}'
stName = '{stName.get()}'
stAddr = '{stAddr.get()}'
stPhone = '{stPhone.get()}'
Discount = '{discount.get()}'
TaxRate = '{taxrate.get()}'
Shipping = '{shipping.get()}'
Info = '{info.get()}'
destPdf = r'{destpdf.get()}'\n""")
    alert('Save Status Updated')

def impsave():
    eName.insert(0, saves.eName)
    datepick.insert(0, saves.datepick)
    monthpick.insert(0, saves.monthpick)
    yearpick.insert(0, saves.yearpick)
    invoicenum.insert(0, saves.invoicenum)
    bName.insert(0, saves.bName)
    bEmail.insert(0, saves.bEmail)
    bAddr.insert(0, saves.bAddr)
    bState.insert(0, saves.bState)
    bPhone.insert(0, saves.bPhone)
    btName.insert(0, saves.btName)
    btAddr.insert(0, saves.btAddr)
    btPhone.insert(0, saves.btPhone)
    btEmail.insert(0, saves.btEmail)
    stName.insert(0, saves.stName)
    stAddr.insert(0, saves.stAddr)
    stPhone.insert(0, saves.stPhone)
    discount.insert(0, saves.Discount)
    taxrate.insert(0, saves.TaxRate)
    shipping.insert(0, saves.Shipping)
    info.insert(0, saves.Info)
    destpdf.insert(0, saves.destPdf)

def warn():
    if verify.phone_check(bPhone.get()) and verify.phone_check(btPhone.get()) and verify.phone_check(stPhone.get()) and verify.phone_check(bNum.get()):
        if verify.email_check(bEmail.get()) and verify.email_check(btEmail.get()):
            if verify.name_check(eName.get()) and verify.name_check(bName.get()) and verify.name_check(btName.get()) and verify.name_check(stName.get()):
                upload()
    else:
        choice = confirm("Found Invalid Data", buttons=["Upload Anyway","Cancel"])
        if choice=='Upload Anyway':
            upload()

def openList():
    system('python -u "getItems.py"')

def build():
    choice = confirm("Proceed?", buttons=["Ok"])
    system('python -u "sub.py"')

master = tk.Tk()
master.title('Invoice Generator')
tk.Label(master, text="INVOICE DETAILS").grid(row=0,columnspan=6)

tk.Label(master, text="Entrier Name").grid(row=1,column=0)
tk.Label(master, text="Date").grid(row=1,column=2)

d = tk.StringVar()
m = tk.StringVar()
y = tk.StringVar()
datepick = ttk.Combobox(master, width = 2, textvariable = d, state="readonly")
datepick['values'] = tuple([str(i).zfill(2) for i in range(1,32)])
monthpick = ttk.Combobox(master, width = 2, textvariable = m, state="readonly")
monthpick['values'] = tuple([str(i).zfill(2) for i in range(1,13)])
yearpick = ttk.Combobox(master, width = 4, textvariable = y, state="readonly")
yearpick['values'] = tuple([str(i) for i in range(2000,2050)])

tk.Label(master, text="Invoice No.").grid(row=1,column=4)

tk.Label(master, text="Business Name").grid(row=3,column=0)
tk.Label(master, text="Business Email").grid(row=4,column=0)
tk.Label(master, text="Business Address").grid(row=5,column=0)
tk.Label(master, text="Business City/State").grid(row=6,column=0)
tk.Label(master, text="Business Phone").grid(row=7,column=0)
tk.Label(master, text="Business Number").grid(row=8,column=0)
ttk.Label(master, text = "Invoice Color").grid(row = 9, column = 0) 

eName = tk.Entry(master)
invoicenum = tk.Entry(master)

bName = tk.Entry(master)
bEmail = tk.Entry(master)
bAddr = tk.Entry(master)
bState = tk.Entry(master)
bPhone = tk.Entry(master)
bNum = tk.Entry(master)

tk.Label(master, text="Bill To Name").grid(row=3,column=2)
tk.Label(master, text="Bill To Address").grid(row=4,column=2)
tk.Label(master, text="Bill To Phone").grid(row=5,column=2)
tk.Label(master, text="Bill To Email").grid(row=6,column=2)

btName = tk.Entry(master)
btAddr = tk.Entry(master)
btPhone = tk.Entry(master)
btEmail = tk.Entry(master)

tk.Label(master, text="Ship To Name").grid(row=3,column=4)
tk.Label(master, text="Ship To Address").grid(row=4,column=4)
tk.Label(master, text="Ship To Phone").grid(row=5,column=4)

stName = tk.Entry(master)
stAddr = tk.Entry(master)
stPhone = tk.Entry(master)

tk.Label(master, text="Discount").grid(row=6,column=4)
tk.Label(master, text="Tax Rate (%)").grid(row=7,column=4)
tk.Label(master, text="Shipping Charges").grid(row=8,column=4)
tk.Label(master, text="Payment Info.").grid(row=9,column=4)

stName = tk.Entry(master)
stAddr = tk.Entry(master)
stPhone = tk.Entry(master)

discount = tk.Entry(master)
taxrate = tk.Entry(master)
shipping = tk.Entry(master)
info = tk.Entry(master)

n = tk.StringVar() 
colorpick = ttk.Combobox(master, width = 17, textvariable = n)
colorpick['values'] = ('Red',  
                          'Green', 
                          'Yellow', 
                          'Blue') 
colorpick.current(0) 

eName.grid(row=1, column=1, pady=20)
datepick.place(x=314, y=40)
monthpick.place(x=353, y=40)
yearpick.place(x=391, y=40)
invoicenum.grid(row=1, column=5, pady=4)

bName.grid(row=3, column=1, pady=4)
bEmail.grid(row=4, column=1, pady=4)
bAddr.grid(row=5, column=1, pady=4)
bState.grid(row=6, column=1, pady=4)
bPhone.grid(row=7, column=1, pady=4)
bNum.grid(row=8, column=1, pady=4)
colorpick.grid(row = 9, column = 1, pady=4) 

btName.grid(row=3, column=3, pady=4)
btAddr.grid(row=4, column=3, pady=4)
btPhone.grid(row=5, column=3, pady=4)
btEmail.grid(row=6, column=3, pady=4)

stName.grid(row=3, column=5, pady=4)
stAddr.grid(row=4, column=5, pady=4)
stPhone.grid(row=5, column=5, pady=4)

discount.grid(row=6, column=5, pady=4)
taxrate.grid(row=7, column=5, pady=4)
shipping.grid(row=8, column=5, pady=4)
info.grid(row=9, column=5, pady=4)

tk.Label(master, text="Save Location").grid(row=10,column=0)
destpdf = tk.Entry(master, width=60)
destpdf.place(x=106, y=308)

tk.Button(master, text='Upload', 
                        command=warn, width=10).grid(row=1,
                                            column=6,
                                            pady=4, padx=3)

tk.Button(master, text='Export Save', 
                        command=uploadsave, width=10).grid(row=3,
                                               column=6,
                                               pady=4, padx=3)

tk.Button(master, text='Import Save', 
                        command=impsave, width=10).grid(row=4,
                                               column=6,
                                               pady=4, padx=3)

tk.Button(master, text='Add Items', 
                        command=openList, width=10).grid(row=5,
                                               column=6,
                                               pady=4, padx=3)

tk.Button(master, text='Build',
          command=build, width=10).grid(row=6,
                                    column=6,
                                    pady=4, padx=3)

tk.Button(master, text='Cancel',
          command=master.quit, width=10).grid(row=7,
                                    column=6,
                                    pady=4, padx=3)



tk.mainloop()

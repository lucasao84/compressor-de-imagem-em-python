from tkinter  import *
from PIL import Image
from tkinter.filedialog import *



#Cores que usei :

co0 = "#000000"  # black
co1 = "#cc1d4e"  # red
co2 = "#feffff"  # white
co3 = "#0074eb"  # blue
co4 = "#435e5a"  # #435e5a
co5 = "#59b356"  # green
co6 = "#d9d9d9"  # grey


#configurando janela

janela = Tk()
janela.geometry('400x250')
janela.title('compressor de imagem')
janela.configure(background=co2)


# configurando frame

frame = Frame(janela, width=400, height=250, bg=co2, relief="flat")
frame.grid(row=0 , column=0, sticky=NSEW)


frame2 = Frame(janela, width=400, height=130, bg=co2, relief="flat")
frame2.grid(row=3 , column=0, sticky=NSEW)

app_name = Label(frame, text='Compressor de Imagem', width=24, height=1, anchor="center", pady=7, padx=10, relief="flat",font=('Courier 20 bold'), bg=co2, )
app_name.grid(row=0 , column=0, columnspan=2, sticky=NSEW, pady=1)




#butao

def novoArquivo():
    global e_altura, e_largura

# frame segunda parte



    # altura e largura


    l_altura = Label(frame2, width=25, anchor='center', text='Digite uma nova altura', bg=co2, fg='black', font=('Courier 9 bold'))
    l_altura.grid(row=0, column=0, sticky=NSEW, padx=7, pady=5)

    l_largura = Label(frame2, width=25, anchor='center', text='Digite uma nova largura', bg=co2, fg='black', font=('Courier 9 bold'))
    l_largura.grid(row=0, column=2, sticky=NSEW, padx=7, pady=5)

    # entry

    e_altura = Entry(frame2, width=15, justify='center',  font=('Ivy 12'))
    e_altura.grid(row=1, column=0, pady=10)

    e_largura = Entry(frame2, width=15, justify='center', font=('Ivy 12'))
    e_largura.grid(row=1,columnspan=2 , column=1, pady=10)



        # abrir imagem
    ficheiro = askopenfilename()
    img = Image.open(ficheiro)
    

    # tamanho original da iamgem original

    img_altura,img_largura = img.size

    app_altura = Label(frame, text=f'Altura e Largura Original {str(img_altura)}x{str(img_largura)}' , width=12, height=1, anchor="center", pady=7, padx=10, relief="flat",font=('Courier 12 bold'), bg=co2, fg=co3)
    app_altura.grid(row=2 , column=0, columnspan=2, sticky=NSEW, pady=1)

    def converter():

        # Obtendo valor da largura e altura

        altura = int(e_altura.get())
        largura =  int(e_largura.get())

        novo_valor = (altura, largura)
        nova_img= img.resize(novo_valor)

        #salva imagen
        img_salva = asksaveasfilename()

        nova_img.save(img_salva+".JPG")

    botao = Button(frame2, width=10,height=1 ,text='Converter', anchor='center', font=('Courier 11 bold'),bg=co5, fg=co2, relief='raised', command=converter)
    botao.grid(row=2, column=0,columnspan=3, pady=2)



botao = Button(frame, width=44,height=1 ,text=' + NOVO', anchor='center',font=('Courier 11 bold'),bg=co3, fg=co2, relief='raised',command=novoArquivo)
botao.grid(row=1, column=0, pady=2)


janela.mainloop()

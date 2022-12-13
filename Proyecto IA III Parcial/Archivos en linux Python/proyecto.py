
from Tkinter import *
import ttk
import os
import subprocess
import tkFont
import time
import tkMessageBox
import ScrolledText



#Ventana
v0=Tk()
v0.title("Menu GPIO")
v0.geometry("700x400+0+0")

# Fuente
text1=tkFont.Font(family="Cursive",size=12)

img_on=PhotoImage(file="on.gif")
img_off=PhotoImage(file="off.gif")

def limpiar():
            horaini.set("")
            minini.set("")
            minf.set("")
            horaf.set("")

def cerrar():
             v0.destroy()

def dialogo1():
               v1=Toplevel()
               v1.geometry("700x350+150+100")
               v1.title("GPIO 0")
               img_on=PhotoImage(file="on.gif")
               img_off=PhotoImage(file="off.gif")

               def aplicarC():
                              c=combo.get()
                              if (c=="ON"):
                                           print "Encendido GPIO0 con el control Combobox"
                                           os.system("sudo /./home/portillo/on0.sh")
                              if (c=="OFF"):
                                            print "Apagado GPIO0 con el control Combobox"
                                            os.system("sudo /./home/portillo/off0.sh")

               def aplicarCH():
                               c1=float(check1.get())
                               if (c1==1):
                                          print "Encendendido GPIO 0 con el control CheckButton"
                                          os.system("sudo /./home/portillo/on0.sh")
                         
                               if (c1==0):
                                          print "Apagado GPIO0 con el control CheckButton"
                                          os.system("sudo /./home/portillo/off0.sh")                             

               def aplicarR():
                              r=radio.get()
                              if (r==1):
                                        print "Encendido GPIO0 con el control radio"
                                        os.system("sudo /./home/portillo/on0.sh")
                              if (r==2):
                                        print "Apagado GPIO0 con el control radio"
                                        os.system("sudo /./home/portillo/off0.sh")

               def On():
                        print "Encendido GPIO0 con el control Button"
                        os.system("sudo /./home/portillo/on0.sh")
         
               def Off():
                         print "Apagado GPIO0 con el control Button"
                         os.system("sudo /./home/portillo/off0.sh")
          
               def actualizar0():
                                  os.system('sshpass -p "27072014" ssh -l uth 192.168.0.11 "sudo gpio read 0" > gpio0.txt')
                                  pf=open("/home/portillo/gpio0.txt","r")

                                  
                                  for linea in pf:
                                                  campo=linea.split("\n")
                                                  campof=campo[0]
                                                  if (campof=="1"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v1,text="1",font=text1).place(x=520,y=130)
                                                                   btn_on=Button(v1,image=img_on).place(x=400,y=150)
                                                                   v1.after(1000,actualizar0)
                                                  if (campof=="0"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v1,text="0",font=text1).place(x=520,y=130)
                                                                   btn_off=Button(v1,image=img_off).place(x=400,y=150)
                                                                   v1.after(1000,actualizar0)
               def guardarGPIO0():
                                    hi=horaini.get()
                                    mi=minini.get()
                                    hf=horaf.get()
                                    mf=minf.get()
                                    tab=" "
                                    dia="*"
                                    mes="*"
                                    anio="*"
                                    usuario="root"
                                    path1="/home/portillo/on0.sh"
                                    path2="/home/portillo/off0.sh"
                                    print "Configuracion del GPIO 0 guardada"

                                    # Asignamos los permisos de escritura y ejecuccion
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio0on")
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio0off")

                                    # Cadena
                                    cadenaon=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                                    cadenaoff=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                            
                                    # Abrimos el archivo
                                    pf=open("/etc/cron.d/procesogpio0on","w")            
                                    pf.write(cadenaon)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)

                                    pf=open("/etc/cron.d/procesogpio0off","w")            
                                    pf.write(cadenaoff)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)            

                                    #Revertimos los permiso
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio0on")
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio0off")

                                    #Reiniciamos el servicio
                                    os.system("sudo /etc/init.d/cron restart")

                                    #Limpiamos
                                    limpiar()
                                    tkMessageBox.showinfo("guardar",message="Horario Guardado Satisfactoriamente")

                                    
                                  
               def salir():
                                v1.destroy()
                                v1.update()

            
               #llamar funcion
               actualizar0()


               #Variables globales
               global minini
               global horaini
               global minf
               global horaf

               #Declaramos las label y cajas de texto
               minini=StringVar()
               horaini=StringVar()
               minf=StringVar()
               horaf=StringVar()
               label_horaini=Label(v1,text="Hora de inicio:", font=text1).place(x=100,y=150)
               txt_horaini=Entry(v1,textvariable=horaini,width=20).place(x=220,y=150)
               label_minini=Label(v1,text="Minuto de inicio:", font=text1).place(x=80,y=180)
               txt_minini=Entry(v1,textvariable=minini,width=20).place(x=220,y=180)

               label_horaf=Label(v1,text="Hora de finalizacion:", font=text1).place(x=50,y=210)
               txt_horaf=Entry(v1,textvariable=horaf,width=20).place(x=220,y=210)
               label_minf=Label(v1,text="Minuto de finalizacion:", font=text1).place(x=35,y=240)
               txt_minf=Entry(v1,textvariable=minf,width=20).place(x=220,y=240)                                

               #Creamos los botones para el gpio 0               
               btn_guardar0 = Button(v1,text="Guardar",command=guardarGPIO0).place(x=190, y=290)
               btn_volver = Button(v1,text="Volver",command=salir).place(x=300, y=290)

            

               global check1
               global combo
               global radio
               radio=IntVar()
               check1=IntVar()
               combo=StringVar()
               r1=Radiobutton(v1,text="ON",variable=radio,value=1).place(x=330,y=50)
               r2=Radiobutton(v1,text="OFF",variable=radio,value=2).place(x=380,y=50)
               btn_aplicarR=Button(v1,text="APLICAR",command=aplicarR).place(x=350,y=80)
               check1btn=ttk.Checkbutton(v1,text="ON/OFF",variable=check1)
               check1btn.place(x=230,y=50)
               btn_aplicarCH=Button(v1,text="APLICAR",command=aplicarCH).place(x=230,y=80)
               combo=ttk.Combobox(v1,state="readonly",values=["ON","OFF"])
               combo.place(x=10,y=50)
               btn_aplicarC=Button(v1,text="APLICAR",command=aplicarC).place(x=10,y=80)
               btn_On=Button(v1,text="ON",command=On).place(x=480,y=50)
               btn_Off=Button(v1,text="OFF",command=Off).place(x=530,y=50)

               v1.mainloop()

def dialogo2():
               v2=Toplevel()
               v2.geometry("700x350+150+100")
               v2.title("GPIO 02")
               img_on=PhotoImage(file="on.gif")
               img_off=PhotoImage(file="off.gif")

               def aplicarC():
                              c=combo.get()
                              if (c=="ON"):
                                           print "Encendido GPIO02 con el control Combobox"
                                           os.system("sudo /./home/portillo/on2.sh")
                              if (c=="OFF"):
                                            print "Apagado GPIO02 con el control Combobox"
                                            os.system("sudo /./home/portillo/off2.sh")

               def aplicarCH():
                               c1=float(check1.get())
                               if (c1==1):
                                          print "Encendendido GPIO 02 con el control CheckButton"
                                          os.system("sudo /./home/portillo/on2.sh")
                         
                               if (c1==0):
                                          print "Apagado GPIO02 con el control CheckButton"
                                          os.system("sudo /./home/portillo/off2.sh")                             

               def aplicarR():
                              r=radio.get()
                              if (r==1):
                                        print "Encendido GPIO02 con el control radio"
                                        os.system("sudo /./home/portillo/on2.sh")
                              if (r==2):
                                        print "Apagado GPIO02 con el control radio"
                                        os.system("sudo /./home/portillo/off2.sh")

               def On():
                        print "Encendido GPIO02 con el control Button"
                        os.system("sudo /./home/portillo/on2.sh")
         
               def Off():
                         print "Apagado GPIO02 con el control Button"
                         os.system("sudo /./home/portillo/off2.sh")
          
               def actualizar02():
                                  os.system('sshpass -p "27072014" ssh -l uth 192.168.0.11 "sudo gpio read 2" > gpio2.txt')
                                  pf=open("/home/portillo/gpio2.txt","r")

                                  
                                  for linea in pf:
                                                  campo=linea.split("\n")
                                                  campof=campo[0]
                                                  if (campof=="1"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v2,text="1",font=text1).place(x=520,y=130)
                                                                   btn_on=Button(v2,image=img_on).place(x=400,y=150)
                                                                   v2.after(1000,actualizar02)
                                                  if (campof=="0"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v2,text="0",font=text1).place(x=520,y=130)
                                                                   btn_off=Button(v2,image=img_off).place(x=400,y=150)
                                                                   v2.after(1000,actualizar02)
               def guardarGPIO02():
                                    hi=horaini.get()
                                    mi=minini.get()
                                    hf=horaf.get()
                                    mf=minf.get()
                                    tab=" "
                                    dia="*"
                                    mes="*"
                                    anio="*"
                                    usuario="root"
                                    path1="/home/portillo/on2.sh"
                                    path2="/home/portillo3/off2.sh"
                                    print "Configuracion del GPIO 02 guardada"

                                    # Asignamos los permisos de escritura y ejecuccion
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio2on")
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio2off")

                                    # Cadena
                                    cadenaon=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                                    cadenaoff=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                            
                                    # Abrimos el archivo
                                    pf=open("/etc/cron.d/procesogpio2on","w")            
                                    pf.write(cadenaon)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)

                                    pf=open("/etc/cron.d/procesogpio2off","w")            
                                    pf.write(cadenaoff)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)            

                                    #Revertimos los permiso
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio2on")
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio2off")

                                    #Reiniciamos el servicio
                                    os.system("sudo /etc/init.d/cron restart")

                                    #Limpiamos
                                    limpiar()
                                    tkMessageBox.showinfo("guardar",message="Horario Guardado Satisfactoriamente")

                                    
                                  
               def salir():
                                v2.destroy()
                                v2.update()

            
               #llamar funcion
               actualizar02()


               #Variables globales
               global minini
               global horaini
               global minf
               global horaf

               #Declaramos las label y cajas de texto
               minini=StringVar()
               horaini=StringVar()
               minf=StringVar()
               horaf=StringVar()
               label_horaini=Label(v2,text="Hora de inicio:", font=text1).place(x=100,y=150)
               txt_horaini=Entry(v2,textvariable=horaini,width=20).place(x=220,y=150)
               label_minini=Label(v2,text="Minuto de inicio:", font=text1).place(x=80,y=180)
               txt_minini=Entry(v2,textvariable=minini,width=20).place(x=220,y=180)

               label_horaf=Label(v2,text="Hora de finalizacion:", font=text1).place(x=50,y=210)
               txt_horaf=Entry(v2,textvariable=horaf,width=20).place(x=220,y=210)
               label_minf=Label(v2,text="Minuto de finalizacion:", font=text1).place(x=35,y=240)
               txt_minf=Entry(v2,textvariable=minf,width=20).place(x=220,y=240)                                

               #Creamos los botones para el gpio 0               
               btn_guardar02 = Button(v2,text="Guardar",command=guardarGPIO02).place(x=190, y=290)
               btn_volver = Button(v2,text="Volver",command=salir).place(x=300, y=290)

            

               global check1
               global combo
               global radio
               radio=IntVar()
               check1=IntVar()
               combo=StringVar()
               r1=Radiobutton(v2,text="ON",variable=radio,value=1).place(x=330,y=50)
               r2=Radiobutton(v2,text="OFF",variable=radio,value=2).place(x=380,y=50)
               btn_aplicarR=Button(v2,text="APLICAR",command=aplicarR).place(x=350,y=80)
               check1btn=ttk.Checkbutton(v2,text="ON/OFF",variable=check1)
               check1btn.place(x=230,y=50)
               btn_aplicarCH=Button(v2,text="APLICAR",command=aplicarCH).place(x=230,y=80)
               combo=ttk.Combobox(v2,state="readonly",values=["ON","OFF"])
               combo.place(x=10,y=50)
               btn_aplicarC=Button(v2,text="APLICAR",command=aplicarC).place(x=10,y=80)
               btn_On=Button(v2,text="ON",command=On).place(x=480,y=50)
               btn_Off=Button(v2,text="OFF",command=Off).place(x=530,y=50)

               v2.mainloop()

def dialogo3():
               v22=Toplevel()
               v22.geometry("700x350+150+100")
               v22.title("GPIO 22")
               img_on=PhotoImage(file="on.gif")
               img_off=PhotoImage(file="off.gif")

               def aplicarC():
                              c=combo.get()
                              if (c=="ON"):
                                           print "Encendido GPIO22 con el control Combobox"
                                           os.system("sudo /./home/portillo/on22.sh")
                              if (c=="OFF"):
                                            print "Apagado GPIO22 con el control Combobox"
                                            os.system("sudo /./home/portillo/off22.sh")

               def aplicarCH():
                               c1=float(check1.get())
                               if (c1==1):
                                          print "Encendendido GPIO 22 con el control CheckButton"
                                          os.system("sudo /./home/portillo/on22.sh")
                         
                               if (c1==0):
                                          print "Apagado GPIO22 con el control CheckButton"
                                          os.system("sudo /./home/portillo/off22.sh")                             

               def aplicarR():
                              r=radio.get()
                              if (r==1):
                                        print "Encendido GPIO22 con el control radio"
                                        os.system("sudo /./home/portillo/on22.sh")
                              if (r==2):
                                        print "Apagado GPIO22 con el control radio"
                                        os.system("sudo /./home/portillo/off22.sh")

               def On():
                        print "Encendido GPIO22 con el control Button"
                        os.system("sudo /./home/portillo/on22.sh")
         
               def Off():
                         print "Apagado GPIO22 con el control Button"
                         os.system("sudo /./home/portillo/off22.sh")
          
               def actualizar22():
                                  os.system('sshpass -p "27072014" ssh -l uth 192.168.0.11 "sudo gpio read 22" > gpio22.txt')
                                  pf=open("/home/portillo/gpio22.txt","r")

                                  
                                  for linea in pf:
                                                  campo=linea.split("\n")
                                                  campof=campo[0]
                                                  if (campof=="1"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v22,text="1",font=text1).place(x=520,y=130)
                                                                   btn_on=Button(v22,image=img_on).place(x=400,y=150)
                                                                   v22.after(1000,actualizar22)
                                                  if (campof=="0"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v22,text="0",font=text1).place(x=520,y=130)
                                                                   btn_off=Button(v22,image=img_off).place(x=400,y=150)
                                                                   v22.after(1000,actualizar22)
               def guardarGPIO22():
                                    hi=horaini.get()
                                    mi=minini.get()
                                    hf=horaf.get()
                                    mf=minf.get()
                                    tab=" "
                                    dia="*"
                                    mes="*"
                                    anio="*"
                                    usuario="root"
                                    path1="/home/portillo/on22.sh"
                                    path2="/home/portillo/off22.sh"
                                    print "Configuracion del GPIO 22 guardada"

                                    # Asignamos los permisos de escritura y ejecuccion
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio22on")
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio22off")

                                    # Cadena
                                    cadenaon=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                                    cadenaoff=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                            
                                    # Abrimos el archivo
                                    pf=open("/etc/cron.d/procesogpio22on","w")            
                                    pf.write(cadenaon)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)

                                    pf=open("/etc/cron.d/procesogpio22off","w")            
                                    pf.write(cadenaoff)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)            

                                    #Revertimos los permiso
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio22on")
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio22off")

                                    #Reiniciamos el servicio
                                    os.system("sudo /etc/init.d/cron restart")

                                    #Limpiamos
                                    limpiar()
                                    tkMessageBox.showinfo("guardar",message="Horario Guardado Satisfactoriamente")

                                    
                                  
               def salir():
                                v22.destroy()
                                v22.update()

            
               #llamar funcion
               actualizar22()


               #Variables globales
               global minini
               global horaini
               global minf
               global horaf

               #Declaramos las label y cajas de texto
               minini=StringVar()
               horaini=StringVar()
               minf=StringVar()
               horaf=StringVar()
               label_horaini=Label(v22,text="Hora de inicio:", font=text1).place(x=100,y=150)
               txt_horaini=Entry(v22,textvariable=horaini,width=20).place(x=220,y=150)
               label_minini=Label(v22,text="Minuto de inicio:", font=text1).place(x=80,y=180)
               txt_minini=Entry(v22,textvariable=minini,width=20).place(x=220,y=180)

               label_horaf=Label(v22,text="Hora de finalizacion:", font=text1).place(x=50,y=210)
               txt_horaf=Entry(v22,textvariable=horaf,width=20).place(x=220,y=210)
               label_minf=Label(v22,text="Minuto de finalizacion:", font=text1).place(x=35,y=240)
               txt_minf=Entry(v22,textvariable=minf,width=20).place(x=220,y=240)                                

               #Creamos los botones para el gpio 2               
               btn_guardar22 = Button(v22,text="Guardar",command=guardarGPIO22).place(x=190, y=290)
               btn_volver = Button(v22,text="Volver",command=salir).place(x=300, y=290)

            

               global check1
               global combo
               global radio
               radio=IntVar()
               check1=IntVar()
               combo=StringVar()
               r1=Radiobutton(v22,text="ON",variable=radio,value=1).place(x=330,y=50)
               r2=Radiobutton(v22,text="OFF",variable=radio,value=2).place(x=380,y=50)
               btn_aplicarR=Button(v22,text="APLICAR",command=aplicarR).place(x=350,y=80)
               check1btn=ttk.Checkbutton(v22,text="ON/OFF",variable=check1)
               check1btn.place(x=230,y=50)
               btn_aplicarCH=Button(v22,text="APLICAR",command=aplicarCH).place(x=230,y=80)
               combo=ttk.Combobox(v22,state="readonly",values=["ON","OFF"])
               combo.place(x=10,y=50)
               btn_aplicarC=Button(v22,text="APLICAR",command=aplicarC).place(x=10,y=80)
               btn_On=Button(v22,text="ON",command=On).place(x=480,y=50)
               btn_Off=Button(v22,text="OFF",command=Off).place(x=530,y=50)

               v22.mainloop()
               

def dialogo4():
               v24=Toplevel()
               v24.geometry("700x350+150+100")
               v24.title("GPIO 24")
               img_on=PhotoImage(file="on.gif")
               img_off=PhotoImage(file="off.gif")

               def aplicarC():
                              c=combo.get()
                              if (c=="ON"):
                                           print "Encendido GPIO24 con el control Combobox"
                                           os.system("sudo /./home/lportillo/on24.sh")
                              if (c=="OFF"):
                                            print "Apagado GPIO24 con el control Combobox"
                                            os.system("sudo /./home/portillo/off24.sh")

               def aplicarCH():
                               c1=float(check1.get())
                               if (c1==1):
                                          print "Encendendido GPIO 24 con el control CheckButton"
                                          os.system("sudo /./home/portillo/on24.sh")
                         
                               if (c1==0):
                                          print "Apagado GPIO24 con el control CheckButton"
                                          os.system("sudo /./home/portillo/off24.sh")                             

               def aplicarR():
                              r=radio.get()
                              if (r==1):
                                        print "Encendido GPIO24 con el control radio"
                                        os.system("sudo /./home/portillo/on24.sh")
                              if (r==2):
                                        print "Apagado GPIO24 con el control radio"
                                        os.system("sudo /./home/portillo/off24.sh")

               def On():
                        print "Encendido GPIO24 con el control Button"
                        os.system("sudo /./home/portillo/on24.sh")
         
               def Off():
                         print "Apagado GPIO24 con el control Button"
                         os.system("sudo /./home/portillo/off24.sh")
          
               def actualizar24():
                                  os.system('sshpass -p "27072014" ssh -l uth 192.168.0.11 "sudo gpio read 24" > gpio24.txt')
                                  pf=open("/home/portillo/gpio24.txt","r")

                                  
                                  for linea in pf:
                                                  campo=linea.split("\n")
                                                  campof=campo[0]
                                                  if (campof=="1"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v24,text="1",font=text1).place(x=520,y=130)
                                                                   btn_on=Button(v24,image=img_on).place(x=400,y=150)
                                                                   v24.after(1000,actualizar24)
                                                  if (campof=="0"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v24,text="0",font=text1).place(x=520,y=130)
                                                                   btn_off=Button(v24,image=img_off).place(x=400,y=150)
                                                                   v24.after(1000,actualizar24)
               def guardarGPIO24():
                                    hi=horaini.get()
                                    mi=minini.get()
                                    hf=horaf.get()
                                    mf=minf.get()
                                    tab=" "
                                    dia="*"
                                    mes="*"
                                    anio="*"
                                    usuario="root"
                                    path1="/home/portillo/on24.sh"
                                    path2="/home/lportillo/off24.sh"
                                    print "Configuracion del GPIO 24 guardada"

                                    # Asignamos los permisos de escritura y ejecuccion
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio24on")
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio24off")

                                    # Cadena
                                    cadenaon=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                                    cadenaoff=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                            
                                    # Abrimos el archivo
                                    pf=open("/etc/cron.d/procesogpio24on","w")            
                                    pf.write(cadenaon)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)

                                    pf=open("/etc/cron.d/procesogpio24off","w")            
                                    pf.write(cadenaoff)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)            

                                    #Revertimos los permiso
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio24on")
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio24off")

                                    #Reiniciamos el servicio
                                    os.system("sudo /etc/init.d/cron restart")

                                    #Limpiamos
                                    limpiar()
                                    tkMessageBox.showinfo("guardar",message="Horario Guardado Satisfactoriamente")

                                    
                                  
               def salir():
                                v24.destroy()
                                v24.update()

            
               #llamar funcion
               actualizar24()


               #Variables globales
               global minini
               global horaini
               global minf
               global horaf

               #Declaramos las label y cajas de texto
               minini=StringVar()
               horaini=StringVar()
               minf=StringVar()
               horaf=StringVar()
               label_horaini=Label(v24,text="Hora de inicio:", font=text1).place(x=100,y=150)
               txt_horaini=Entry(v24,textvariable=horaini,width=20).place(x=220,y=150)
               label_minini=Label(v24,text="Minuto de inicio:", font=text1).place(x=80,y=180)
               txt_minini=Entry(v24,textvariable=minini,width=20).place(x=220,y=180)

               label_horaf=Label(v24,text="Hora de finalizacion:", font=text1).place(x=50,y=210)
               txt_horaf=Entry(v24,textvariable=horaf,width=20).place(x=220,y=210)
               label_minf=Label(v24,text="Minuto de finalizacion:", font=text1).place(x=35,y=240)
               txt_minf=Entry(v24,textvariable=minf,width=20).place(x=220,y=240)                                

               #Creamos los botones para el gpio 24               
               btn_guardar24 = Button(v24,text="Guardar",command=guardarGPIO24).place(x=190, y=290)
               btn_volver = Button(v24,text="Volver",command=salir).place(x=300, y=290)

            

               global check1
               global combo
               global radio
               radio=IntVar()
               check1=IntVar()
               combo=StringVar()
               r1=Radiobutton(v24,text="ON",variable=radio,value=1).place(x=330,y=50)
               r2=Radiobutton(v24,text="OFF",variable=radio,value=2).place(x=380,y=50)
               btn_aplicarR=Button(v24,text="APLICAR",command=aplicarR).place(x=350,y=80)
               check1btn=ttk.Checkbutton(v24,text="ON/OFF",variable=check1)
               check1btn.place(x=230,y=50)
               btn_aplicarCH=Button(v24,text="APLICAR",command=aplicarCH).place(x=230,y=80)
               combo=ttk.Combobox(v24,state="readonly",values=["ON","OFF"])
               combo.place(x=10,y=50)
               btn_aplicarC=Button(v24,text="APLICAR",command=aplicarC).place(x=10,y=80)
               btn_On=Button(v24,text="ON",command=On).place(x=480,y=50)
               btn_Off=Button(v24,text="OFF",command=Off).place(x=530,y=50)

               v24.mainloop()

def dialogo5():
               v25=Toplevel()
               v25.geometry("700x350+150+100")
               v25.title("GPIO 25")
               img_on=PhotoImage(file="on.gif")
               img_off=PhotoImage(file="off.gif")

               def aplicarC():
                              c=combo.get()
                              if (c=="ON"):
                                           print "Encendido GPIO25 con el control Combobox"
                                           os.system("sudo /./home/portillo/on25.sh")
                              if (c=="OFF"):
                                            print "Apagado GPIO25 con el control Combobox"
                                            os.system("sudo /./home/portillo/off25.sh")

               def aplicarCH():
                               c1=float(check1.get())
                               if (c1==1):
                                          print "Encendendido GPIO 25 con el control CheckButton"
                                          os.system("sudo /./home/lportillo/on25.sh")
                         
                               if (c1==0):
                                          print "Apagado GPIO25 con el control CheckButton"
                                          os.system("sudo /./home/portillo/off25.sh")                             

               def aplicarR():
                              r=radio.get()
                              if (r==1):
                                        print "Encendido GPIO25 con el control radio"
                                        os.system("sudo /./home/portillo/on25.sh")
                              if (r==2):
                                        print "Apagado GPIO25 con el control radio"
                                        os.system("sudo /./home/portillo/off25.sh")

               def On():
                        print "Encendido GPIO25 con el control Button"
                        os.system("sudo /./home/portillo/on25.sh")
         
               def Off():
                         print "Apagado GPIO25 con el control Button"
                         os.system("sudo /./home/portillo/off25.sh")
          
               def actualizar25():
                                  os.system('sshpass -p "27072014" ssh -l uth 192.168.0.11 "sudo gpio read 25" > gpio25.txt')
                                  pf=open("/home/portillo/gpio25.txt","r")

                                  
                                  for linea in pf:
                                                  campo=linea.split("\n")
                                                  campof=campo[0]
                                                  if (campof=="1"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v25,text="1",font=text1).place(x=520,y=130)
                                                                   btn_on=Button(v25,image=img_on).place(x=400,y=150)
                                                                   v25.after(1000,actualizar25)
                                                  if (campof=="0"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v25,text="0",font=text1).place(x=520,y=130)
                                                                   btn_off=Button(v25,image=img_off).place(x=400,y=150)
                                                                   v25.after(1000,actualizar25)
               def guardarGPIO25():
                                    hi=horaini.get()
                                    mi=minini.get()
                                    hf=horaf.get()
                                    mf=minf.get()
                                    tab=" "
                                    dia="*"
                                    mes="*"
                                    anio="*"
                                    usuario="root"
                                    path1="/home/portillo/on25.sh"
                                    path2="/home/portillo/off25.sh"
                                    print "Configuracion del GPIO 25 guardada"

                                    # Asignamos los permisos de escritura y ejecuccion
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio25on")
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio25off")

                                    # Cadena
                                    cadenaon=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                                    cadenaoff=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                            
                                    # Abrimos el archivo
                                    pf=open("/etc/cron.d/procesogpio25on","w")            
                                    pf.write(cadenaon)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)

                                    pf=open("/etc/cron.d/procesogpio25off","w")            
                                    pf.write(cadenaoff)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)            

                                    #Revertimos los permiso
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio25on")
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio25off")

                                    #Reiniciamos el servicio
                                    os.system("sudo /etc/init.d/cron restart")

                                    #Limpiamos
                                    limpiar()
                                    tkMessageBox.showinfo("guardar",message="Horario Guardado Satisfactoriamente")

                                    
                                  
               def salir():
                                v25.destroy()
                                v25.update()

            
               #llamar funcion
               actualizar25()


               #Variables globales
               global minini
               global horaini
               global minf
               global horaf

               #Declaramos las label y cajas de texto
               minini=StringVar()
               horaini=StringVar()
               minf=StringVar()
               horaf=StringVar()
               label_horaini=Label(v25,text="Hora de inicio:", font=text1).place(x=100,y=150)
               txt_horaini=Entry(v25,textvariable=horaini,width=20).place(x=220,y=150)
               label_minini=Label(v25,text="Minuto de inicio:", font=text1).place(x=80,y=180)
               txt_minini=Entry(v25,textvariable=minini,width=20).place(x=220,y=180)

               label_horaf=Label(v25,text="Hora de finalizacion:", font=text1).place(x=50,y=210)
               txt_horaf=Entry(v25,textvariable=horaf,width=20).place(x=220,y=210)
               label_minf=Label(v25,text="Minuto de finalizacion:", font=text1).place(x=35,y=240)
               txt_minf=Entry(v25,textvariable=minf,width=20).place(x=220,y=240)                                

               #Creamos los botones para el gpio 25               
               btn_guardar25 = Button(v25,text="Guardar",command=guardarGPIO25).place(x=190, y=290)
               btn_volver = Button(v25,text="Volver",command=salir).place(x=300, y=290)

            

               global check1
               global combo
               global radio
               radio=IntVar()
               check1=IntVar()
               combo=StringVar()
               r1=Radiobutton(v25,text="ON",variable=radio,value=1).place(x=330,y=50)
               r2=Radiobutton(v25,text="OFF",variable=radio,value=2).place(x=380,y=50)
               btn_aplicarR=Button(v25,text="APLICAR",command=aplicarR).place(x=350,y=80)
               check1btn=ttk.Checkbutton(v25,text="ON/OFF",variable=check1)
               check1btn.place(x=230,y=50)
               btn_aplicarCH=Button(v25,text="APLICAR",command=aplicarCH).place(x=230,y=80)
               combo=ttk.Combobox(v25,state="readonly",values=["ON","OFF"])
               combo.place(x=10,y=50)
               btn_aplicarC=Button(v25,text="APLICAR",command=aplicarC).place(x=10,y=80)
               btn_On=Button(v25,text="ON",command=On).place(x=480,y=50)
               btn_Off=Button(v25,text="OFF",command=Off).place(x=530,y=50)

               v25.mainloop()


def dialogo6():
               v29=Toplevel()
               v29.geometry("700x350+150+100")
               v29.title("GPIO 29")
               img_on=PhotoImage(file="on.gif")
               img_off=PhotoImage(file="off.gif")

               def aplicarC():
                              c=combo.get()
                              if (c=="ON"):
                                           print "Encendido GPIO29 con el control Combobox"
                                           os.system("sudo /./home/portillo/on29.sh")
                              if (c=="OFF"):
                                            print "Apagado GPIO29 con el control Combobox"
                                            os.system("sudo /./home/portillo/off29.sh")

               def aplicarCH():
                               c1=float(check1.get())
                               if (c1==1):
                                          print "Encendendido GPIO 29 con el control CheckButton"
                                          os.system("sudo /./home/portillo/on29.sh")
                         
                               if (c1==0):
                                          print "Apagado GPIO29 con el control CheckButton"
                                          os.system("sudo /./home/portillo/off29.sh")                             

               def aplicarR():
                              r=radio.get()
                              if (r==1):
                                        print "Encendido GPIO29 con el control radio"
                                        os.system("sudo /./home/portillo/on29.sh")
                              if (r==2):
                                        print "Apagado GPIO29 con el control radio"
                                        os.system("sudo /./home/portillo/off29.sh")

               def On():
                        print "Encendido GPIO29 con el control Button"
                        os.system("sudo /./home/portillo/on29.sh")
         
               def Off():
                         print "Apagado GPIO29 con el control Button"
                         os.system("sudo /./home/portillo/off29.sh")
          
               def actualizar29():
                                  os.system('sshpass -p "27072014" ssh -l uth 192.168.0.11 "sudo gpio read 29" > gpio29.txt')
                                  pf=open("/home/portillo/gpio29.txt","r")

                                  
                                  for linea in pf:
                                                  campo=linea.split("\n")
                                                  campof=campo[0]
                                                  if (campof=="1"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v29,text="1",font=text1).place(x=520,y=130)
                                                                   btn_on=Button(v29,image=img_on).place(x=400,y=150)
                                                                   v29.after(1000,actualizar29)
                                                  if (campof=="0"):
                                                                   text1=tkFont.Font(family="Arial",size=100)
                                                                   label1=Label(v29,text="0",font=text1).place(x=520,y=130)
                                                                   btn_off=Button(v29,image=img_off).place(x=400,y=150)
                                                                   v29.after(1000,actualizar29)
               def guardarGPIO29():
                                    hi=horaini.get()
                                    mi=minini.get()
                                    hf=horaf.get()
                                    mf=minf.get()
                                    tab=" "
                                    dia="*"
                                    mes="*"
                                    anio="*"
                                    usuario="root"
                                    path1="/home/portillo/on29.sh"
                                    path2="/home/portillo/off29.sh"
                                    print "Configuracion del GPIO 29 guardada"

                                    # Asignamos los permisos de escritura y ejecuccion
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio29on")
                                    os.system("sudo chmod -R 777 /etc/cron.d/procesogpio29off")

                                    # Cadena
                                    cadenaon=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                                    cadenaoff=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(anio)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                            
                                    # Abrimos el archivo
                                    pf=open("/etc/cron.d/procesogpio29on","w")            
                                    pf.write(cadenaon)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)

                                    pf=open("/etc/cron.d/procesogpio29off","w")            
                                    pf.write(cadenaoff)
                                    pf.write("\n")
                                    pf.close()
                                    time.sleep(0.1)            

                                    #Revertimos los permiso
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio29on")
                                    os.system("sudo chmod -R 755 /etc/cron.d/procesogpio29off")

                                    #Reiniciamos el servicio
                                    os.system("sudo /etc/init.d/cron restart")

                                    #Limpiamos
                                    limpiar()
                                    tkMessageBox.showinfo("guardar",message="Horario Guardado Satisfactoriamente")

                                    
                                  
               def salir():
                                v29.destroy()
                                v29.update()

            
               #llamar funcion
               actualizar29()


               #Variables globales
               global minini
               global horaini
               global minf
               global horaf

               #Declaramos las label y cajas de texto
               minini=StringVar()
               horaini=StringVar()
               minf=StringVar()
               horaf=StringVar()
               label_horaini=Label(v29,text="Hora de inicio:", font=text1).place(x=100,y=150)
               txt_horaini=Entry(v29,textvariable=horaini,width=20).place(x=220,y=150)
               label_minini=Label(v29,text="Minuto de inicio:", font=text1).place(x=80,y=180)
               txt_minini=Entry(v29,textvariable=minini,width=20).place(x=220,y=180)

               label_horaf=Label(v29,text="Hora de finalizacion:", font=text1).place(x=50,y=210)
               txt_horaf=Entry(v29,textvariable=horaf,width=20).place(x=220,y=210)
               label_minf=Label(v29,text="Minuto de finalizacion:", font=text1).place(x=35,y=240)
               txt_minf=Entry(v29,textvariable=minf,width=20).place(x=220,y=240)                                

               #Creamos los botones para el gpio 29               
               btn_guardar29 = Button(v29,text="Guardar",command=guardarGPIO29).place(x=190, y=290)
               btn_volver = Button(v29,text="Volver",command=salir).place(x=300, y=290)

            

               global check1
               global combo
               global radio
               radio=IntVar()
               check1=IntVar()
               combo=StringVar()
               r1=Radiobutton(v29,text="ON",variable=radio,value=1).place(x=330,y=50)
               r2=Radiobutton(v29,text="OFF",variable=radio,value=2).place(x=380,y=50)
               btn_aplicarR=Button(v29,text="APLICAR",command=aplicarR).place(x=350,y=80)
               check1btn=ttk.Checkbutton(v29,text="ON/OFF",variable=check1)
               check1btn.place(x=230,y=50)
               btn_aplicarCH=Button(v29,text="APLICAR",command=aplicarCH).place(x=230,y=80)
               combo=ttk.Combobox(v29,state="readonly",values=["ON","OFF"])
               combo.place(x=10,y=50)
               btn_aplicarC=Button(v29,text="APLICAR",command=aplicarC).place(x=10,y=80)
               btn_On=Button(v29,text="ON",command=On).place(x=480,y=50)
               btn_Off=Button(v29,text="OFF",command=Off).place(x=530,y=50)

               v29.mainloop()



def cargar():
             ck=int(check.get())
             
             if (ck==1):
                          os.system('sshpass -p "27072014" ssh -l uth 192.168.0.11  "sudo gpio readall" > cargar.txt')
                          valor=subprocess.check_output("cat /home/portillo/cargar.txt",shell=True)
                          area=ScrolledText.ScrolledText(v0,width=80,height=20)
                          area.place(x=10,y=50)
                          area.insert(INSERT,valor)

             if (ck==0):
                         area=ScrolledText.ScrolledText(v0,width=80,height=20)
                         area.place(x=10,y=50)
                         area.delete("1.0",END)

        


global check
check=IntVar()
check1=ttk.Checkbutton(v0,text="Load",variable=check,command=cargar)
check1.place(x=10,y=10)


menubar=Menu(v0)


filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="GPIO0",command=dialogo1)
filemenu.add_command(label="GPIO02",command=dialogo2)
filemenu.add_command(label="GPIO22",command=dialogo3)
filemenu.add_command(label="GPIO24",command=dialogo4)
filemenu.add_command(label="GPIO25",command=dialogo5)
filemenu.add_command(label="GPIO29",command=dialogo6)
filemenu.add_command(label="SALIR",command=v0.destroy)
menubar.add_cascade(label="CONTROL",menu=filemenu)



v0.config(menu=menubar)

v0.mainloop()

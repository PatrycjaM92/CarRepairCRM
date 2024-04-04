import tkinter as tk
from tkinter import messagebox
import db_conf
from tkinter import ttk
from tkinter import scrolledtext
from datetime import datetime
from tkcalendar import Calendar


class App(tk.Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.start_window()
        self.c_id=None
        self.car_id=None
        self.function_control=0
        self.date_of_service=None

    def start_window(self):

        self.logFrame=tk.Frame(self.master)
        self.logFrame.grid()
       
        login_frame=tk.Frame(self.logFrame)
        login_frame.grid(padx=225)
        menuLab=tk.Label(login_frame,text= "Zaloguj się do systemu", font=("Arial", 22,))
        menuLab.grid(row=0,column=0,padx=30,pady=30)

        self.label_user = tk.Label(login_frame, text="Użytkownik:",font=("Arial", 14))
        self.label_user.grid(row=1,column=0,pady=5)

        self.entry_user = tk.Entry(login_frame)
        self.entry_user.grid(row=2,column=0,ipadx=30,ipady=3)

        self.label_password = tk.Label(login_frame, text="Hasło:",font=("Arial", 14))
        self.label_password.grid(row=3,column=0,pady=5)

        self.entry_password = tk.Entry(login_frame, show="*")
        self.entry_password.grid(row=4,column=0,ipadx=30,ipady=3)

        b1 = tk.Button(login_frame,
                    text="  Zaloguj", font=("Digital-font", 14), command=self.logintoDB)
        b1.grid(row=5,column=0,padx=30,pady=30)
     



        
    def logintoDB(self):
        host = "localhost"
        # user = self.entry_user.get()
        # password = self.entry_password.get()
        user=''
        password =""
        db_name = ''

        if  not user or not password:
            messagebox.showwarning("Błąd", "Wszystkie pola muszą być wypełnione.")
            return
        try: 
            self.db_handler = db_conf.DatabaseConnector(host=host, user=user, password=password,database=db_name)
            self.db_handler.connect()
           # self.db_conf.display_table(self.db_handler)
            #messagebox.showinfo("Info", "Logowanie przebiegło pomyślnie.")
            self.main_view()
        except:
            messagebox.showwarning("Błąd", "Sprawdź poprawność wprowadzonych danych")
        
 
    def main_view(self):
        self.clear_frame(self.logFrame)
        manage_frame=tk.LabelFrame(self.logFrame,text="Zarządzaj ")
        manage_frame.grid(row=0)
        self.add_customer_button = tk.Button(manage_frame, text="Dodaj klienta", command=self.add_client_view)
        self.add_customer_button.grid(row=0,column=0,padx=5,pady=10)
        self.add_car_button = tk.Button(manage_frame, text="Dodaj samochód", command=self.add_car_view)
        self.add_car_button.grid(row=0,column=1,padx=5,pady=10)
        self.add_service_button= tk.Button(manage_frame, text="Zarejestruj nową usługę", command=self.add_service_view)
        self.add_service_button.grid(row=0,column=2,padx=5,pady=10)

        search_frame=tk.LabelFrame(self.logFrame,text="Przeszukaj bazę")
        search_frame.grid(row=1,sticky=tk.W,ipadx=10,ipady=10)
        find=tk.Button(search_frame,text="Znajdź klienta")
        find.grid(pady=5)
    


    def add_client_view(self):
        add_customer_window = tk.Toplevel(self.master)
        add_customer_window.title("Dodawanie nowego klienta")
        f=tk.Frame(add_customer_window)
        f.grid(padx=100,pady=50)
        first_name_label = tk.Label(f, text="Imię:")
        first_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.first_name_entry = tk.Entry(f)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10)

        last_name_label = tk.Label(f, text="Nazwisko:")
        last_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.last_name_entry = tk.Entry(f)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=10)

        address_label = tk.Label(f, text="Adres:")
        address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_label_entry = tk.Entry(f)
        self.address_label_entry.grid(row=3, column=1, padx=10, pady=10)

        city_label = tk.Label(f, text="E-mail:")
        city_label.grid(row=4, column=0, padx=10, pady=10)
        self.city_label_entry = tk.Entry(f)
        self.city_label_entry.grid(row=4, column=1, padx=10, pady=10)
        

        phone_label = tk.Label(f, text="Telefon:")
        phone_label.grid(row=5, column=0, padx=10, pady=10)
        self.phone_label_entry = tk.Entry(f)
        self.phone_label_entry.grid(row=5, column=1, padx=10, pady=10)

        save_button = ttk.Button(f, text="Zapisz",width=50, command=self.save_customer)
        save_button.grid(row=6, column=0, columnspan=2, pady=10)     

    def add_car_view(self):
        self.function_control=0
        
        add_car_window = tk.Toplevel(self.master)
        add_car_window.title("Dodawanie nowego samochodu")
        
        client_frame=tk.LabelFrame(add_car_window,text="Szukaj klienta")
        client_frame.grid()
        inf_lab=tk.Label(client_frame,text="Wyszukaj klienta, do którego należy samochód")
        inf_lab.grid(row=0,column=0)     
        find_client_fname_label=tk.Label(client_frame,text='Imię')
        find_client_fname_label.grid(row=1,column=0,padx=5,pady=5)
        find_fclient_entry=tk.Entry(client_frame)
        find_fclient_entry.grid(row=1,column=1)

        find_client_lname_label=tk.Label(client_frame,text='Nazwisko')
        find_client_lname_label.grid(row=2,column=0,padx=5,pady=5)
        find_lclient_entry=tk.Entry(client_frame)
        find_lclient_entry.grid(row=2,column=1)
        find_client_button=tk.Button(client_frame,text='Znajdź',command=lambda:self.find_client(find_fclient_entry,find_lclient_entry))
        find_client_button.grid(row=3,column=1,columnspan=1)
        
        self.info_label=tk.Label(client_frame,text="Wybrany klient: ")
        self.info_label.grid()

        car_opt_frame=tk.LabelFrame(add_car_window,text="Wpisz szczegoły")
        car_opt_frame.grid()
        reg_no_label = tk.Label(car_opt_frame, text="Numer rejestracyjny:")
        reg_no_label.grid(row=5, column=0, padx=10, pady=10)
        self.reg_no_entry = tk.Entry(car_opt_frame)
        self.reg_no_entry.grid(row=5, column=1, padx=10, pady=10)

        make_label = tk.Label(car_opt_frame, text="Marka:")
        make_label.grid(row=6, column=0, padx=10, pady=10)
        self.make_entry = tk.Entry(car_opt_frame)
        self.make_entry.grid(row=6, column=1, padx=10, pady=10)

        model_label = tk.Label(car_opt_frame, text="Model:")
        model_label.grid(row=7, column=0, padx=10, pady=10)
        self.model_entry = tk.Entry(car_opt_frame)
        self.model_entry.grid(row=7, column=1, padx=10, pady=10)

        dist_label = tk.Label(car_opt_frame, text="Przebieg:")
        dist_label.grid(row=8, column=0, padx=10, pady=10)
        self.dist_entry = tk.Entry(car_opt_frame)
        self.dist_entry.grid(row=8, column=1, padx=10, pady=10)

        engin_label = tk.Label(car_opt_frame, text="Silnik:")
        engin_label.grid(row=9, column=0, padx=10, pady=10)
        self.engine_entry = tk.Entry(car_opt_frame)
        self.engine_entry.grid(row=9, column=1, padx=10, pady=10)
        

        year_prod_label = tk.Label(car_opt_frame, text="Rok produkcji:")
        year_prod_label.grid(row=10, column=0, padx=10, pady=10)
        self.year_prod_entry = tk.Entry(car_opt_frame)
        self.year_prod_entry.grid(row=10, column=1, padx=10, pady=10)

        savecar_but = tk.Button(car_opt_frame, text="Zapisz",command=self.save_car)
        savecar_but.grid(row=11, column=1,columnspan=1, pady=10) 
    
    def add_service_view(self):
        self.function_control=1
        ad_service_f=tk.Toplevel(self.master)
        ad_service_f.title("Rejestruj nową usługę")
        find_client_frame = tk.LabelFrame(ad_service_f,text="Poszukaj klienta,któremu zostanie wykonana usługa")
        find_client_frame.grid(padx=5,pady=10,ipadx=10,ipady=10,sticky=tk.W)

        find_f_name=tk.Label(find_client_frame,text="Imię: ")
        find_f_name.grid(row=0,column=0,pady=10)
        find_fclient_entry = tk.Entry(find_client_frame)
        find_fclient_entry.grid(row=0,column=1)
        
        find_n_name=tk.Label(find_client_frame,text="Nazwisko: ")
        find_n_name.grid(row=1,column=0,pady=10)
        find_lclient_entry= tk.Entry(find_client_frame)
        find_lclient_entry.grid(row=1,column=1)
        
        find_client_butt=tk.Button(find_client_frame,text="Szukaj",command=lambda:self.find_client(find_fclient_entry,find_lclient_entry))
        find_client_butt.grid(row=2,column=1,columnspan=1)
        self.info_label=tk.Label(find_client_frame,text="Wybrany klient: ")
        self.info_label.grid(row=3,column=0,pady=10)

        detail_frame=tk.LabelFrame(ad_service_f,text="Wpisz szczegóły usługi")
        detail_frame.grid(padx=5,pady=5,ipadx=10,ipady=10)

        date_label=tk.Label(detail_frame,text="Data wykonania usługi: ")
        date_label.grid(row=1,column=0)     
        self.date_entry=tk.Button(detail_frame,text="wybierz datę",command=self.choose_date)
        self.date_entry.grid(row=1,column=1,pady=15,sticky=tk.W)
        self.date_label = tk.Label(detail_frame, text=" Nie wybrano daty")
        self.date_label.grid(row=1,column=1,pady=10)

        cost_label=tk.Label(detail_frame,text="Koszt: ")
        cost_label.grid(row=2,column=0)     
        self.cost_entry=tk.Entry(detail_frame)
        self.cost_entry.grid(row=2,column=1,pady=10,sticky=tk.W)

        descr_label=tk.Label(detail_frame,text="Opis usługi: ")
        descr_label.grid(row=3,column=0)     
        self.descr_entry=scrolledtext.ScrolledText(detail_frame,wrap=tk.WORD,width=40,height=5)
        self.descr_entry.grid(row=3,column=1,pady=5)

        comment_label=tk.Label(detail_frame,text="Komentarz: ")
        comment_label.grid(row=4,column=0)     
        self.comment_entry=scrolledtext.ScrolledText(detail_frame,wrap=tk.WORD,width=40,height=5)
        self.comment_entry.grid(row=4,column=1,pady=5)

        add_serv_but=tk.Button(detail_frame,text="Zarejestruj usługę",command=self.save_service)
        add_serv_but.grid(row=5,column=0,columnspan=2,pady=15)

    def find_client(self,f_nam_entry,l_nam_entry):
            self.client_wind=tk.Toplevel(self.master)
            self.client_wind.title("Wybierz klienta")
            client_fname=f_nam_entry.get()
            client_lname=l_nam_entry.get()
            query = 'SELECT * FROM clients WHERE first_name = %s AND last_name =%s'
            clients =self.db_handler.cursor.execute(query,(client_fname,client_lname))
            result = self.db_handler.cursor.fetchall()
            print("result: ",result)
            client_list=[]
            for i in result:
                client_list.append(i)
            cl=tuple(client_list)    
            print(cl)
            var = tk.Variable(value=cl)
            def items_selected(event):
                # get all selected indices
                selected_indices = listbox.curselection()
                for i in selected_indices:
                    c=listbox.get(i)
                    self.c_id=c[0]
                    print(self.c_id)
                    return self.c_id
            if result:
                listbox = tk.Listbox(self.client_wind,listvariable=var,height=6,width=100,selectmode=tk.EXTENDED)
                listbox.grid()
                self.info_label.config(text=f"Wybrany klient: {client_fname} {client_lname}")
            else:
                messagebox.showwarning("Błąd","Brak w bazie klienta. Dodaj klienta do bazy")           
          
            listbox.bind('<<ListboxSelect>>', items_selected)
            

          
            if self.function_control==1:
                choose=tk.Label(self.client_wind,text="Wybierz klienta: ")
                choose.grid(row=1)
                choose_but=tk.Button(self.client_wind,text="Wybierz",command=self.find_car)
                choose_but.grid(row=2)
            else:
                choose=tk.Label(self.client_wind,text="Wybierz klienta: ")
                choose.grid(row=1)
                choose_but=tk.Button(self.client_wind,text="Wybierz",command=self.client_wind.destroy)
                choose_but.grid(row=2)

    def find_car(self):
        cars_wind=tk.Toplevel(self.master)
        cars_wind.title("Wybierz samochód")
        cID=[]
        cID.append(self.c_id)
        print(type(cID))
        query = 'SELECT * FROM cars WHERE client_id= %s'
        cars = self.db_handler.cursor.execute(query,(cID))
        result = self.db_handler.cursor.fetchall()
        print(result)
        car_list=[]
        for i in result:
            car_list.append(i)
            cl=tuple(car_list)    
            var = tk.Variable(value=cl)

        
                        
        def items_selected(event):
            selected_indices = listbox.curselection()
            for i in selected_indices:
                    c=listbox.get(i)
                    self.car_id=c[0]
                    print(self.car_id)
                    return self.car_id
            listbox.bind('<<ListboxSelect>>', items_selected)
        if result:
            listbox = tk.Listbox(cars_wind,listvariable=var,height=6,width=100,selectmode=tk.EXTENDED)
            listbox.grid()   
            choose_but=tk.Button(cars_wind,text="Wybierz",command=lambda : (cars_wind.destroy(),self.client_wind.destroy()))
            choose_but.grid(row=2)
        else:messagebox.showwarning("Błąd","Brak w bazie samochodu dla podanego klienta. Dodaj samochód dla tego klienta")

    def save_customer(self):
        firts_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        address = self.address_label_entry.get()
        city = self.city_label_entry.get()
        phone = self.phone_label_entry.get()

        if firts_name and last_name:
            self.db_handler.add_client(firts_name, last_name,address,city,phone)
            messagebox.showinfo("Info","Klient został dodany pomyslnie.")
            # self.name_entry.delete(0, tk.END)
            # self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Błąd", "Nie podano imienia oraz nazwiska")
    def save_car(self):
        reg_no = self.reg_no_entry.get()
        client_id=self.c_id
        make = self.make_entry.get()
        model = self.model_entry.get()
        dist=self.dist_entry.get()
        engine = self.engine_entry.get()
        prod_year = self.year_prod_entry.get()

        if reg_no:
            self.db_handler.add_car(reg_no, client_id,make,model,dist,engine,prod_year)
            messagebox.showinfo("Info","Samochód został dodany pomyslnie.") 
            # self.name_entry.delete(0, tk.END)
            # self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Błąd", "Samochód musi zawierać numer rejestracyjny")
    
    def save_service(self):
        client_id=self.c_id
        reg_no = self.car_id
        date = self.date_of_service
        serice_descr=self.descr_entry.get("1.0",tk.END)
        cost=self.cost_entry.get()
        comment=self.comment_entry.get("1.0",tk.END)
        print(client_id,reg_no,date,serice_descr,cost,comment)

        if date and cost:
            self.db_handler.add_service(client_id, reg_no, date,serice_descr, cost,comment )
            messagebox.showinfo("Info","Usługa została zarejestrowana w systemie!") 
        else:
            messagebox.showerror("Błąd", "Brakuje daty orazu ceny wykonanej usługi")
    
        
        
    def choose_date(self):
        def choose_date():
            choosen_date = calendar.get_date()
            
            self.date_label.config(text=f"Wybrana data: {choosen_date}")

            convert_date = datetime.strptime(str(choosen_date), '%m/%d/%y')
            self.date_of_service= convert_date.strftime("%Y-%m-%d")
            self.date_label.config(text=f"Wybrana data: {self.date_of_service}")
            

        date_wind=tk.Toplevel(self.master)
        date_wind.title("Wybierz datę wykonania usługi")
        calendar = Calendar(date_wind, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)

        calendar.pack(pady=20)

        butt = tk.Button(date_wind, text="Wybierz datę", command=lambda:(choose_date(),date_wind.destroy()))
        butt.pack(pady=10)

        

    def clear_frame(self,frame):
        # Destroy all widgets inside the frame
        
        for widget in frame.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Car Repair Shop Manager")
    root.geometry("850x450")
    window = App(root)

    root.mainloop()

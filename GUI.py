from tkinter import Button,Spinbox,Tk,Label,Checkbutton,IntVar,StringVar,Radiobutton,Frame,LEFT,RIGHT,TOP

class InitialSetupGUI:

    def __init__(self,title,root):
        self.data = None
        self.root = root
        self.root.title(title)
        gsettings_frame = Frame(root)
        gsettings_frame.grid(pady=10)#@.pack(side=TOP)#.pack(side=TOP)

        pso_settings_frame = Frame(root)
        pso_settings_frame.grid(pady=10)

        Label(gsettings_frame,text="Global Settings").grid(row=0,column=0)
        self.num_locs_label = Label(gsettings_frame,text="# Locations").grid(row=1,column=0)#.pack(side=TOP)
        self.num_locs = Spinbox(gsettings_frame,from_=2,to=50,width=10,textvariable=IntVar(value=16))
        self.num_locs.grid(row=2,column=0)#.pack(side=TOP)#(side=LEFT)

        self.num_vehc_label = Label(gsettings_frame,text="# Vehicles").grid(row=1,column=1)
        self.num_vehc = Spinbox(gsettings_frame,from_=1,to=10,width=10,textvariable=IntVar(value=4))
        self.num_vehc.grid(row=2,column=1)#.pack(side=TOP)#(side=LEFT)

        #PSO Paramaters
        Label(pso_settings_frame,text="PSO Settings").grid(row=0,column=0)
        self.pso_pop_label = Label(pso_settings_frame,text="Swarm Population").grid(row=1,column=0)#.pack(side=TOP)
        self.pso_pop = Spinbox(pso_settings_frame,from_=1,to=500,width=10,textvariable=IntVar(value=25))
        self.pso_pop.grid(row=2,column=0)#.pack(side=TOP)#(side=LEFT)

        self.pso_iter_label = Label(pso_settings_frame,text="# Iterations").grid(row=1,column=1)
        self.pso_iter = Spinbox(pso_settings_frame,from_=1,to=2000,width=10,textvariable=IntVar(value=250))
        self.pso_iter.grid(row=2,column=1)#.pack(side=TOP)#(side=LEFT)
        

        self.useGoogleData = IntVar()
        self.useGoogleDataCheck = Checkbutton(root,variable=self.useGoogleData,
                                        text="Use Google OR-Tools test data.",
                                        onvalue=True,offvalue=False)
        self.useGoogleDataCheck.select()
        self.useGoogleDataCheck.grid(row=3,column=0,pady=10)#.pack()


        methods_frame = Frame(root)

        SearchMethods = [
            ("ACO","aco","normal"),
            ("PSO W/Local improvement","pso_s1","normal"),
            ("PSO No Local Improvement","pso_s2","normal"),
            ("Testing (10-50 Locations)", "test", "normal")
        ]

        self.searchMethod = StringVar()
        self.searchMethod.set("pso_s2")

        for text,val,state in SearchMethods:
            temp = Radiobutton(methods_frame,variable=self.searchMethod,
                                            text=text,value=val,state=state,anchor='w').pack(fill='both')

        methods_frame.grid(row=4,column=0,pady=10)#.pack()

        Button(root,text="Done",width=10,command=self.__getData__).grid(row=5,column=0)
    
    def getData(self):
        return self.data

    def __getData__(self):
        self.data = {'num_locations': int(self.num_locs.get()),
                'num_vehicles' : int(self.num_vehc.get()),
                'useGoogleData': self.useGoogleData.get(),
                'method':self.searchMethod.get(),
                'pso_population':int(self.pso_pop.get()),
                'pso_iterations':int(self.pso_iter.get())
                }
            
        self.root.destroy()
        
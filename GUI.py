from tkinter import Button,Spinbox,Tk,Label,Checkbutton,IntVar,StringVar,Radiobutton,Frame

class InitialSetupGUI:

    def __init__(self,title,root):
        self.data = None
        self.root = root
        self.root.title(title)

        self.num_locs_label = Label(root,text="Number of Locations").pack()
        self.num_locs = Spinbox(root,from_=2,to=50,width=10,textvariable=IntVar(value=16))
        self.num_locs.pack()

        self.num_vehc_label = Label(root,text="Number of Vehicles").pack()
        self.num_vehc = Spinbox(root,from_=1,to=10,width=10,textvariable=IntVar(value=4))
        self.num_vehc.pack()

        self.useGoogleData = IntVar()
        self.useGoogleDataCheck = Checkbutton(root,variable=self.useGoogleData,
                                        text="Use Google OR-Tools test data.",
                                        onvalue=True,offvalue=False)
        self.useGoogleDataCheck.select()
        self.useGoogleDataCheck.pack()


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
                                            text=text,value=val,state=state).pack()

        methods_frame.pack()

        Button(root,text="Done",width=10,command=self.__getData__).pack()
    
    def getData(self):
        return self.data

    def __getData__(self):
        self.data = {'num_locations': int(self.num_locs.get()),
                'num_vehicles' : int(self.num_vehc.get()),
                'useGoogleData': self.useGoogleData.get(),
                'method':self.searchMethod.get()
                }
            
        self.root.destroy()
        
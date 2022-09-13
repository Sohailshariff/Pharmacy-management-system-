from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management Systems")
        self.master.geometry('1350x750')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text="Pharmacy Management Systems", font=('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(self.frame, width=1010, height=300, bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=20, relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(self.frame, width=1010, height=200, bd=20, relief='ridge')
        self.Loginframe3.grid(row=3, column=0, pady=2)

        # ==================================================================================================================
        self.lblUsername = Label(self.Loginframe1, text='Username', font=('arial', 30, 'bold'), bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1, font=('arial', 30, 'bold'), bd=22, textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.Loginframe1, text='Password', font=('arial', 30, 'bold'), bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1, font=('arial', 30, 'bold'), bd=22, textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1, padx=85)
        # ==================================================================================================================

        self.btnLogin = Button(self.Loginframe2, text="Login", width=17, font=('arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(self.Loginframe2, text="Reset", width=17, font=('arial', 20, 'bold'),
                               command=self.Reset)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.Loginframe2, text="Exit", width=17, font=('arial', 20, 'bold'),
                              command=self.iExit)
        self.btnExit.grid(row=0, column=2)

        # ==================================================================================================================

        self.btnRegistration = Button(self.Loginframe3, text="Patients Registration Systems",
                                      state=DISABLED, command=self.Registration_window, font=('arial', 30, 'bold'))
        self.btnRegistration.grid(row=0, column=0)

        self.btnHospital = Button(self.Loginframe3, text="Hospital Management Systems",
                                  state=DISABLED, command=self.Hospital_window, font=('arial', 30, 'bold'))
        self.btnHospital.grid(row=0, column=1)

    # ==================================================================================================================
    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if (user == str(1234)) and (pas == str(12345)):
            self.btnRegistration.config(state=NORMAL)
            self.btnHospital.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", "You have entered an invalid login details")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnHospital.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return

    # ==================================================================================================================

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient's Registraion System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        # ==================================================================================================================
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%y"))

        Var1 = StringVar()
        Var2 = StringVar()
        Var3 = StringVar()
        Var4 = IntVar()

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Telephone = StringVar()
        Ref = StringVar()
        Date = StringVar()

        Membership = StringVar()
        Membership.set("0")

        MainFrame = Frame(self.frame)
        MainFrame.grid()

        # ==================================================================================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno(" Patient's Registration System", "Confirm if you want to Exit")
            if iExit > 0:
                master.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Date.set("")

            Var1.set("")
            Var2.set("")
            Var3.set("")
            Var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)

        def iResetRecord():
            Reset()
            return

        def Ref_No():
            x = random.randint(10903, 600873)
            randomRef = str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,
                                   "%-15s" % Ref.get() + "%-17s" % Firstname.get() + "%-13s" % Surname.get() + "%-14s"
                                   % Address.get() + "%-12s" % DateofOrder.get() + "%-12s" % Telephone.get() + "%-10s" % Membership.get() + "\n")

        def Membership_Fees():
            if (Var4.get() == 1):
                self.txtMembership.configure(state=NORMAL)
                Item1 = float(50)
                Membership.set("E" + str(Item1))
                paid1 = Membership.get()

            elif (Var4.get() == 0):
                self.txtMembership.configure(state=DISABLED)
                Membership.set("0")

        # ==========================================Frame========================================================

        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=39, font=('arial', 20, 'bold'),
                              text="\tPatient's Registration System\t", padx=8)
        self.lblTitle.grid()

        # ======================================Lower Frames=====================================================

        MemberDetailsFrame = LabelFrame(MainFrame, bd=20, width=800, height=400, pady=20, relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10, width=800, height=400, padx=20, relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, width=350, height=400, font=('arial', 12, 'bold'),
                                   text='Customer Name', relief=RIDGE)
        MembersName_F.grid(row=0, column=0)

        Receipt_ButtonFrame = LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=400, relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)
        # =======================================================================================================
        self.lblReferenceNo = Label(MembersName_F, font=('arial', 12, 'bold'), text="Reference No", bd=7)
        self.lblReferenceNo.grid(row=0, column=0, sticky='w')

        self.txtReferenceNo = Entry(MembersName_F, font=('arial', 12, 'bold'), bd=7, textvariable=Ref, state=DISABLED,
                                    insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblFirstname = Label(MembersName_F, font=('arial', 12, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky='w')

        self.txtFirstname = Entry(MembersName_F, font=('arial', 12, 'bold'), bd=7, textvariable=Firstname,
                                  insertwidth=2)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(MembersName_F, font=('arial', 12, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=2, column=0, sticky='w')

        self.txtSurname = Entry(MembersName_F, font=('arial', 12, 'bold'), bd=7, textvariable=Surname, insertwidth=2)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(MembersName_F, font=('arial', 12, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=3, column=0, sticky='w')

        self.txtAddress = Entry(MembersName_F, font=('arial', 12, 'bold'), bd=7, textvariable=Address, insertwidth=2)
        self.txtAddress.grid(row=3, column=1)

        self.lblPostcode = Label(MembersName_F, font=('arial', 12, 'bold'), text="Post Code", bd=7)
        self.lblPostcode.grid(row=4, column=0, sticky='w')

        self.txtPostcode = Entry(MembersName_F, font=('arial', 12, 'bold'), bd=7, textvariable=Postcode, insertwidth=2)
        self.txtPostcode.grid(row=4, column=1)

        self.lblTelephone = Label(MembersName_F, font=('arial', 12, 'bold'), text="Telephone", bd=7)
        self.lblTelephone.grid(row=5, column=0, sticky='w')

        self.txtTelephone = Entry(MembersName_F, font=('arial', 12, 'bold'), bd=7, textvariable=Telephone,
                                  insertwidth=2)
        self.txtTelephone.grid(row=5, column=1)

        self.lblDate = Label(MembersName_F, font=('arial', 12, 'bold'), text="Date", bd=7)
        self.lblDate.grid(row=6, column=0, sticky='w')

        self.txtDate = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=DateofOrder, insertwidth=2)
        self.txtDate.grid(row=6, column=1)
        # =========================================Member Information============================================

        self.lblProve_of_ID = Label(MembersName_F, font=('arial', 14, 'bold'), text="Proof of ID", bd=7)
        self.lblProve_of_ID.grid(row=7, column=0, sticky='w')

        self.cboProve_of_ID = ttk.Combobox(MembersName_F, textvariable=Var1, state='readonly',
                                           font=('arial', 14, 'bold'), width=19)
        self.cboProve_of_ID['value'] = ('', 'Pilot Licence', 'Driving Licence', 'Passport', 'Student ID')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7, column=1)

        self.lblType_of_Member = Label(MembersName_F, font=('arial', 14, 'bold'), text="Type of Member", bd=7)
        self.lblType_of_Member.grid(row=8, column=0, sticky='w')

        self.cboType_of_Member = ttk.Combobox(MembersName_F, textvariable=Var2, state='readonly',
                                              font=('arial', 14, 'bold'), width=19)
        self.cboType_of_Member['value'] = ('', 'Full Member', 'Annual Membership', 'Pay As You Go', 'Honorary Member')
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8, column=1)

        self.lblMethod_of_Payment = Label(MembersName_F, font=('arial', 14, 'bold'), text="Method Of Payment", bd=7)
        self.lblMethod_of_Payment.grid(row=9, column=0, sticky='w')

        self.cboMethod_of_Payment = ttk.Combobox(MembersName_F, textvariable=Var3, state='readonly',
                                                 font=('arial', 14, 'bold'), width=19)
        self.cboMethod_of_Payment['value'] = ('', 'Visa Card', 'Master Card', 'Debit Card', 'Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9, column=1)

        # ====================================Check Buttons========================================================
        self.chckMembership = Checkbutton(MembersName_F, text="Membership", variable=Var4, onvalue=1, offvalue=0,
                                          font=('arial', 14, 'bold'), command=Membership_Fees).grid(row=10, column=0,
                                                                                                    sticky='w')

        self.txtMembership = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=Membership,
                                   insertwidth=2, state=DISABLED, justify=RIGHT)
        self.txtMembership.grid(row=10, column=1)

        # ==========================================Receipt=========================================================

        self.lblLabel = Label(Receipt_ButtonFrame, font=('arial', 10, 'bold'), pady=10,
                              text="Member Ref\t Firstname\t Surname\t Address\t\t Date\t Telephone\t Member Paid",
                              bd=7)
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(Receipt_ButtonFrame, width=65, height=14, font=('arial', 14, 'bold'), bd=7)
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        # =========================================Buttons=============================================================

        self.btnReceipt = Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13,
                                 text="Receipt", command=Receipt).grid(row=2, column=0)

        self.btnReset = Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13, text="Reset",
                               command=iResetRecord).grid(row=2, column=1)

        self.btnExit = Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13, text="Exit",
                              command=iExit).grid(row=2, column=2)

        # =============================================================================================================

    def close_windows(self):
        self.master.destroy

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(" Patient's Registration System", "Confirm if you want to Exit?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
            return


class Window3:

    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        cmbNameTablets = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssueDate = StringVar()
        ExpiryDate = StringVar()
        Dailydose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        HowToUseMedication = StringVar()
        PatientId = StringVar()
        NHSNumber = StringVar()
        PatientName = StringVar()
        DateOfBirth = StringVar()
        PatientsAddress = StringVar()
        Prescription = StringVar()

        MainFrame = Frame(self.frame)
        MainFrame.grid()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Hospital Management System", "Confirm if you want to Exit")
            if iExit > 0:
                root.destroy()
                return

        def iPrescription():
            self.txtPrescription.insert(END, 'Name of Tablets: \t\t\t\t' + cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END, 'Reference No: \t\t\t\t' + Ref.get() + "\n")
            self.txtPrescription.insert(END, 'Dose: \t\t\t\t' + Dose.get() + "\n")
            self.txtPrescription.insert(END, 'Number of Tablets: \t\t\t\t' + NumberTablets.get() + "\n")
            self.txtPrescription.insert(END, 'Lot: \t\t\t\t' + Lot.get() + "\n")
            self.txtPrescription.insert(END, 'Issued Date: \t\t\t\t' + IssueDate.get() + "\n")
            self.txtPrescription.insert(END, 'Expiry Date: \t\t\t\t' + ExpiryDate.get() + "\n")
            self.txtPrescription.insert(END, 'Daily dose: \t\t\t\t' + Dailydose.get() + "\n")
            self.txtPrescription.insert(END, 'Possible Side Effects: \t\t\t\t' + PossibleSideEffects.get() + "\n")
            self.txtPrescription.insert(END, 'Further Information: \t\t\t\t' + FurtherInformation.get() + "\n")
            self.txtPrescription.insert(END, 'Storage Advice: \t\t\t\t' + StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END, 'Driving Using Machines: \t\t\t\t' + DrivingUsingMachines.get() + "\n")
            self.txtPrescription.insert(END, 'How To Use Medication: \t\t\t\t' + HowToUseMedication.get() + "\n")
            self.txtPrescription.insert(END, 'Patient Id: \t\t\t\t' + PatientId.get() + "\n")
            self.txtPrescription.insert(END, 'NHS Number: \t\t\t\t' + NHSNumber.get() + "\n")
            self.txtPrescription.insert(END, 'Patient Name: \t\t\t\t' + PatientName.get() + "\n")
            self.txtPrescription.insert(END, 'Date of Birth: \t\t\t\t' + DateOfBirth.get() + "\n")
            self.txtPrescription.insert(END, 'Patients Address: \t\t\t\t' + PatientsAddress.get() + "\n")
            self.txtPrescription.insert(END, 'Prescription: \t\t\t\t' + Prescription.get() + "\n")
            return

        def iPrescriptionData():
            self.txtFrameDetail.insert(END,
                                       cmbNameTablets.get() + "\t\t" + Ref.get() + "\t" + Dose.get() + "\t\t" + NumberTablets.get() + "\t" + Lot.get() + "\t" + IssueDate.get() + "\t\t" + ExpiryDate.get() + "\t" + Dailydose.get() + "\t\t" + StorageAdvice.get() + "\t" + NHSNumber.get() + "\t\t" + PatientName.get() + "\t" + DateOfBirth.get() + "\t" + PatientsAddress.get() + "\n")

            return

        def iDelete():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            Dailydose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowToUseMedication.set("")
            PatientId.set("")
            NHSNumber.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientsAddress.set("")
            self.txtPrescription.delete("1.0", END)
            self.txtFrameDetail.delete("1.0", END)

            return

        def iReset():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            Dailydose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowToUseMedication.set("")
            PatientId.set("")
            NHSNumber.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientsAddress.set("")
            self.txtPrescription.delete("1.0", END)
            # self.txtFrameDetail.delete("1.0",END)

            return

        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=39, font=('arial', 40, 'bold'), text="\tHospital Management System\t",
                              padx=8)
        self.lblTitle.grid()

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Patient Information:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE,
                                    font=('arial', 12, 'bold'), text="Prescription:")
        DataFrameRIGHT.pack(side=RIGHT)

        self.lblNameofTablet = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Name of Tablet:", padx=2, pady=2)
        self.lblNameofTablet.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(DataFrameLEFT, textvariable=cmbNameTablets, font=('arial', 12, 'bold'),
                                          width=23)
        self.cboNameTablet['value'] = ('', 'Ibuprofin', 'Cocodamol', 'Paracetamol', 'Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        self.lblFurtherInfo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Further Information:", padx=2,
                                    pady=2)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=FurtherInformation,
                                    width=25)
        self.txtFurtherInfo.grid(row=0, column=3)

        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference No:", padx=2, pady=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column=1)

        self.lblStorage = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Storage Advice:", padx=2, pady=2)
        self.lblStorage.grid(row=1, column=2, sticky=W)
        self.txtStorage = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=StorageAdvice, width=25)
        self.txtStorage.grid(row=1, column=3)

        self.lblDose = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Dose:", padx=2, pady=2)
        self.lblDose.grid(row=2, column=0, sticky=W)
        self.txtDose = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Dose, width=25)
        self.txtDose.grid(row=2, column=1)

        self.lblDUseMachine = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Driving Machines:", padx=2, pady=2)
        self.lblDUseMachine.grid(row=2, column=2, sticky=W)
        self.txtDUseMachine = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DrivingUsingMachines,
                                    width=25)
        self.txtDUseMachine.grid(row=2, column=3)

        self.lblNoOfTablets = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="No. Of Tablets:", padx=2, pady=2)
        self.lblNoOfTablets.grid(row=3, column=0, sticky=W)
        self.txtNoOfTablets = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=NumberTablets, width=25)
        self.txtNoOfTablets.grid(row=3, column=1)

        self.lblUseMedication = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Medication:", padx=2, pady=2)
        self.lblUseMedication.grid(row=3, column=2, sticky=W)
        self.txtUseMedication = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=HowToUseMedication,
                                      width=25)
        self.txtUseMedication.grid(row=3, column=3)

        self.lblLot = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Lot:", padx=2, pady=2)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Lot, width=25)
        self.txtLot.grid(row=4, column=1)

        self.lblPatientID = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient ID:", padx=2, pady=2)
        self.lblPatientID.grid(row=4, column=2, sticky=W)
        self.txtPatientID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientId, width=25)
        self.txtPatientID.grid(row=4, column=3)

        self.lblIssuedDate = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Issued Date:", padx=2, pady=2)
        self.lblIssuedDate.grid(row=5, column=0, sticky=W)
        self.txtIssuedDate = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=IssueDate, width=25)
        self.txtIssuedDate.grid(row=5, column=1)

        self.lblNHSNumber = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="NHSNumber:", padx=2, pady=2)
        self.lblNHSNumber.grid(row=5, column=2, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=NHSNumber, width=25)
        self.txtNHSNumber.grid(row=5, column=3)

        self.lblExpDate = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Exp Date:", padx=2, pady=2)
        self.lblExpDate.grid(row=6, column=0, sticky=W)
        self.txtExpDate = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=ExpiryDate, width=25)
        self.txtExpDate.grid(row=6, column=1)

        self.lblPatientName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Name:", padx=2, pady=2)
        self.lblPatientName.grid(row=6, column=2, sticky=W)
        self.txtPatientName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientName, width=25)
        self.txtPatientName.grid(row=6, column=3)

        self.lblDailyDose = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Daily Dose:", padx=2, pady=2)
        self.lblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Dailydose, width=25)
        self.txtDailyDose.grid(row=7, column=1)

        self.lblDateOfBirth = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date Of Birth:", padx=2, pady=2)
        self.lblDateOfBirth.grid(row=7, column=2, sticky=W)
        self.txtDateOfBirth = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DateOfBirth, width=25)
        self.txtDateOfBirth.grid(row=7, column=3)

        self.lblSideEffects = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Side Effects:", padx=2, pady=2)
        self.lblSideEffects.grid(row=8, column=0, sticky=W)
        self.txtSideEffects = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PossibleSideEffects,
                                    width=25)
        self.txtSideEffects.grid(row=8, column=1)

        self.lblPatientsAddress = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient's Address:", padx=2,
                                        pady=2)
        self.lblPatientsAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientsAddress = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientsAddress,
                                        width=25)
        self.txtPatientsAddress.grid(row=8, column=3)

        self.txtPrescription = Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width=43, height=12, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        self.btnPrescription = Button(ButtonFrame, text='Prescription', font=('arial', 12, 'bold'), width=24, bd=4,
                                      command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)

        self.btnPrescriptionData = Button(ButtonFrame, text='Prescription Data', font=('arial', 12, 'bold'), width=24,
                                          bd=4, command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)

        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=24, bd=4, command=iDelete)
        self.btnDelete.grid(row=0, column=2)

        self.btnReset = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=24, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=3)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), width=24, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=4)

        self.lblLabel = Label(FrameDetail, font=('arial', 10, 'bold'), pady=8,
                              text="Name Of Tablets\tReference No.\t Dsage\tNo. Of Tabets\t Lot\t Issued Date\t Exp. Date\tDaily Dose\tStorage Adv.\t NHS Number\t Patients Name\t DOB\t Address")
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail = Text(FrameDetail, font=('arial', 12, 'bold'), width=141, height=4, padx=2, pady=4)
        self.txtFrameDetail.grid(row=1, column=0)


root = Tk()
app = Window1(root)

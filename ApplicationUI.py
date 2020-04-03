from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import datefinder
from datetime import timedelta
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas_datareader.data as web
# import pandas as pd
from Final_Calculation import *


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Portfolio Optimizer")
        self.minsize(1200, 850)
        self.maxsize(1200, 850)
        self.wm_iconbitmap("profits.ico")
        self.configure(height=850, width=1200)
        self.configure(background='#898B8B')

        self.windowWidth = self.winfo_reqwidth()
        self.windowHeight = self.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        self.positionRight = int(self.winfo_screenwidth() / 2 - self.windowWidth / 2)
        self.positionDown = int(self.winfo_screenheight() / 2 - self.windowHeight / 2)

        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(self.positionRight, self.positionDown))


        self.userInput = []
        self.input ={}


        # self.createWidget()
        self.initUI()
        self.assistInput()
        # self.createMenus()


    def matplotCanvas(self):

        self.run_progressBar()

        main_df = pd.DataFrame(self.input['df'])

        # Data cleaning
        to_impute = main_df.columns[main_df.isna().any()].tolist()

        for col in to_impute:
            main_df = impute(main_df, col, "mean")

        # Get monthly percentage change of assets
        main_df = main_df.pct_change().dropna()

        # Get mean returns and covariance matrix of assets within the given time frame
        mean_returns = main_df.mean()
        cov_matrix = main_df.cov()

        # Calculate efficient frontier based on risk-free rate and number of portfolios
        num_portfolios = 20000

        # Progress Bar
        self.progress_bar["maximum"] = num_portfolios
        risk_free_rate = 0.0152


        return simulate_ef_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate, self.progress_bar)

    def assistInput(self):
        assets = ['ACN', 'DIS', 'COST', 'INTC', 'JPM', 'V', 'XOM', 'JNJ', 'BSX', 'CPB']
        for i, ch in enumerate(assets):
            self.userInput[i].set(ch)

    def createInputWidets(self):
        global inputCount
        inputCount = 0
        for _ in range(20):
            self.userInput.append(StringVar())
            Label(self.innerInputFrame, bg="#5FDBDC").grid(row=inputCount*2, columnspan=3, sticky=EW)
            Label(self.innerInputFrame, text=str(inputCount + 1), bg="#5FDBDC", width=12, anchor=W).grid(row=inputCount*2 + 1, column=0)
            entry = Entry(self.innerInputFrame, width=30, textvariable=self.userInput[inputCount])
            entry.grid(row=inputCount*2 + 1, column=1)
            Label(self.innerInputFrame, width=20, bg="#5FDBDC").grid(row=inputCount*2 + 1, column=2, sticky=E)

            inputCount += 1

        Label(self.innerInputFrame, bg="#5FDBDC").grid(row=inputCount * 2, columnspan=3, sticky=EW)

    # Define scrolling region for inputCanvas so it uses innerInputFrame
    def myfunction(self, event):
        self.inputCanvas.configure(scrollregion=self.inputCanvas.bbox("all"), width=400, height=550)

    def initInputFrame(self):
        self.inputFrame = Frame(self, relief=GROOVE)
        self.inputFrame.place(x=0, y=100, relheight=8 / 16, relwidth=0.33)
        self.inputCanvas = Canvas(self.inputFrame, bg="#5FDBDC")
        self.innerInputFrame = ttk.Frame(self.inputCanvas)
        self.myscrollbar = ttk.Scrollbar(self.inputFrame, orient="vertical", command=self.inputCanvas.yview)
        self.inputCanvas.configure(yscrollcommand=self.myscrollbar.set)
        self.myscrollbar.pack(side="right", fill="y")
        self.inputCanvas.pack(side="left", fill="y")
        self.inputCanvas.create_window((0, 0), window=self.innerInputFrame, anchor=NW)
        self.innerInputFrame.bind("<Configure>", self.myfunction)
        self.createInputWidets()

    def initHeaderFrame(self):
        self.start = StringVar()
        self.end = StringVar()

        self.headerFrame = Frame(self, bg="#5FDBDC")
        Label(self.headerFrame, text='Portfolio Assets', bg="#5FDBDC").grid(row=0, columnspan=4, ipadx=146)
        Label(self.headerFrame, text='Start-Date: ', bg="#5FDBDC").grid(row=1, column=0)
        self.startDate = ttk.Entry(self.headerFrame, width=15, textvariable=self.start)
        self.startDate.grid(row=1, column=1)
        Label(self.headerFrame, text='End-Date: ', bg="#5FDBDC").grid(row=1, column=2)
        self.endDate = ttk.Entry(self.headerFrame, width=15, textvariable=self.end)
        self.endDate.grid(row=1, column=3, sticky=E)
        ttk.Separator(self.headerFrame).grid(row=2, sticky=E + W, columnspan=4, pady=7)

        self.photo = PhotoImage(file=r'dolar.png')
        self.photo = self.photo.subsample(17, 17)
        self.calculate_button = ttk.Button(self.headerFrame, text="Optimize Portfolio", width=20, image=self.photo, compound=LEFT, command=self.calculateResults)
        self.calculate_button.grid(row=3, column=1, columnspan=2)

        self.headerFrame.place(x=0, y=0, relheight=2 / 16, relwidth=0.33)

    def calculateResults(self):
        # Input validation
        if self.validateDates() and self.validateAssets():
            f, outputString = self.matplotCanvas()
            self.popup.destroy()
            self.displayResult.set(outputString)
            self.figureAnswer = f
            self.plotGraph()

    def validateDates(self):
        start_date_str = self.start.get()
        end_date_str = self.end.get()

        start_date_matches = list(datefinder.find_dates(start_date_str))
        end_date_matches = list(datefinder.find_dates(end_date_str))

        if len(start_date_matches) < 1 or len(end_date_matches) < 1:
            self.invalidDateError()
            return False

        start_date = start_date_matches[0]
        end_date = end_date_matches[0]

        if end_date < start_date + timedelta(days=31):
            self.apartDateError()
            return False

        self.input['start'] = start_date
        self.input['end'] = end_date

        return True


    def validateAssets(self):
        proper_inputs = []
        for userinput in self.userInput:
            input = userinput.get()
            if input.strip() is not "":
                proper_inputs.append(input)
        if len(proper_inputs) < 1:
            self.insufficientTickerInputError()
            return False
        data_fetch_response = extractData(proper_inputs, self.input['start'], self.input['end'])
        if type(data_fetch_response) == str:
            self.invalidTickerError(data_fetch_response)
            return False

        self.input['df'] = data_fetch_response
        return True


    def initDisplayFrame(self):
        self.displayResult = StringVar()
        self.displayResult.set("Currently no results to display")

        self.displayFrame = ttk.Frame(self)
        self.displayFrame.place(x=0, y=522, relheight=6 / 16, relwidth=0.33)
        self.displayLabel = Label(self.displayFrame, textvariable=self.displayResult)
        self.displayLabel.pack(fill=BOTH, expand=True)
        self.displayLabel.configure(bg="#5FDBDC", fg="#455757", borderwidth=2, relief="ridge")

    def initCanvasFrame(self):
        self.canvasFrame = Frame(self, bg="#558F8F")
        self.canvasFrame.place(x=400, y=0, relheight=1, relwidth=0.665)
        self.introductionCanvas = Canvas(self.canvasFrame, bg="white")
        self.introductionCanvas.pack(expand=YES, fill=BOTH)
        filename = PhotoImage(file='introductionCanvas.PNG')
        self.filename = filename
        self.introductionCanvas.create_image(400, 400, anchor='center', image=self.filename)

    def createCanvasImage(self):
        canvas = Canvas(bg="white", height=250, width=300)
        canvas.pack(expand=YES, fill=BOTH)
        filename = PhotoImage(file='profits.gif')
        self.filename = filename
        canvas.create_image(50, 50, anchor=NW, image=self.filename)

    def plotGraph(self):
        is_first_time = True
        if hasattr(self, 'matplotcanvas'):
            self.matplotcanvas.get_tk_widget().pack_forget()
            is_first_time = False
        else:
            self.introductionCanvas.delete("all")
        f = self.figureAnswer
        self.matplotcanvas = FigureCanvasTkAgg(f, self.introductionCanvas)
        self.matplotcanvas.draw()
        self.matplotcanvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        if is_first_time == True:
            toolbar = NavigationToolbar2Tk(self.matplotcanvas, self)
            self.matplotcanvas.tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    def initUI(self):
        self.initHeaderFrame()
        self.initInputFrame()
        self.initDisplayFrame()
        self.initCanvasFrame()


    # Error Messages
    def invalidDateError(self):
        msg.showerror("Date Error", "You have tried to input an invalid Date")

    def apartDateError(self):
        msg.showerror("Date Error", "Specified start and end date must be at least 1 month apart")

    def invalidTickerError(self, ticker):
        msg.showerror("Ticker Value Error", ticker + " is not a valid ticker symbol")

    def insufficientTickerInputError(self):
        msg.showerror("Ticker Value Error", "Not enough assets were added, please input at least 2 assets")

    # Progress bar
    def run_progressBar(self):
        self.popup = Toplevel()
        self.popup.geometry("%dx%d%+d%+d" % (400, 100, 800, 500))
        Label(self.popup, text="Optimizing Portfolio Please Wait...").pack(expand=True, fill=BOTH)
        self.progress_bar = ttk.Progressbar(self.popup, orient='horizontal', length=286, mode="determinate")
        self.progress_bar.pack(expand=True, fill=BOTH)

    # def createMenus(self):
    #     menubar = Menu(self)
    #     self.config(menu=menubar)
    #
    #     file_menu = Menu(menubar, tearoff=0)
    #     menubar.add_cascade(label="File", menu=file_menu)
    #
    #     # file_menu.add_command(label="New")
    #     # file_menu.add_command(label="Save")
    #     # file_menu.add_separator()
    #     file_menu.add_command(label="Exit", command=self.closeWindow)
    #
    #     help_menu = Menu(menubar, tearoff=0)
    #     menubar.add_cascade(label="Help", menu=help_menu)
    #     help_menu.add_command(label="About Us")
    #
    # def closeWindow(self):
    #     self.quit()
    #     self.destroy()
    #     exit()


root = Root()
root.mainloop()

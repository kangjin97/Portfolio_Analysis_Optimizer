# Portfolio_Analysis_Optimizer

Steps to make any changes:

1. Use QT Designer to edit portfolio_analysis_UI.ui 
(Qt Designer can be downloaded through command prompt "pip install pyqt5-tools"

2. use command "pyuic5 -x portfolio_analysis_UI.ui -o [New File Name]" using command prompt to create new copy of python file for portfolio UI 
NOTE: YOU MUST BE IN SAME DIRECTORY AS UI FILE FOR IT TO WORK!
  
portfolio1.py makes use of object oriented programming! 
  
User-created Functions:

1. pushButton1(self) - pushes the calculate button to run calculate() function
2. calculate() - Makes use of algorithm to calculate annual returns and standard deviation (NOTE: this is a static method)
   
This is an experimental version and we should use it to consult Dr. Z to gain more insight. 

HOW TO RUN:

1. Run portfolio1.py on an IDE or from command prompt 
2. Input ticker symbol (I.E. GOOGL) and percentage (I.E. 0.5) of each share in designated columns
3. Adjust Time Period with Start Date and End Date
4. Hit Calculate! 

portfolio1.py is not designed to handle any errors!

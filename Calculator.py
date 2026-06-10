from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout

app= QApplication([])
w=QWidget()
w.setWindowTitle("Calculator")
display= QLineEdit()
layout= QGridLayout()
layout.addWidget(display, 0, 0, 1, 4)

def click(t):
    if t=='C':
            display.clear()
    elif t=='=':
        try:
            display.setText(str(eval(display.text())))    
        except:
                display.setText("Error")
    else:
        display.setText(display.text()+ t)      

#Buttons
buttons=['1', '2', '3', '+',
         '4', '5', '6', '-',
         "7", '8', '9', '*',
         'C', '0', '=', '/'
        ] 

for i, text in enumerate(buttons):
    btn= QPushButton(text)
    btn.clicked.connect(lambda checked, t=text: click(t))
    layout.addWidget(btn, i//4 +1, i%4)
    
w.setLayout(layout)
w.show()
app.exec_()                    

                                                                   #START

'''ИМПОРТИРУЕ НУЖНЫЕ НАМ ИНСТРУМЕНТЫ'''

import sys 

from PyQt5 import uic 

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QCheckBox, QTextEdit, QLabel

from PyQt5.QtCore import Qt

#-------------------------------------------------------------------------------

'''ПРОСЧИТЫВАЕМ ПРАВИЛЬНЫЙ ОТВЕТ'''

import random

def humanrange (size):
   
    if size//(1024**3)>0:
   
        k=' Гб'
   
    elif size//(1024**2)>0:
   
        k=' Мб'
   
    elif size//1024>0:
   
        k=' Кб'
   
    else:
   
        k=' Байт'
    
    return k
def humanrange1 (size):
    
    if size//(1024**3)>0:
        
        j=size//(1024**3)
    
    elif size//(1024**2)>0:
        
        j=size//(1024**2)
    
    elif size//1024>0:
        
        j=size//1024
    
    else:
        
        j=size
    
    return j   

#-------------------------------------------------------------------------------

'''ФОРМИРУЕМ ОКНО С КОТОРЫМ БУДЕТ РАБОТАТЬ ПОЛЬЗОВАТЕЛЬ'''

class MyWidget(QMainWindow):
    
    def __init__(self):
        
        super().__init__()

        self.initUI()
     
#-------------------------------------------------------------------------------    
    
    def initUI(self): 
        
        '''ФОРМИРУЕМ ОКНО'''
        
        self.setGeometry(300, 300, 900, 500)
        
        self.setWindowTitle('YANDEX_PROJECT') 
        
        
        '''ОТКРЫВАЕМ, ЧИТАЕМ И ВЫВОДИМ НА ЭКРАН СТРОКУ ИЗ ТЕКСТОВОГО ФАЙЛА С ДАННЫМИ ДЛЯ УСЛОВИЯ ЗАДАЧИ'''
        
        handle = open('test.txt', 'rt', encoding='utf-8').read().split('\n')
        
        x=random.choice(handle)
        
        y=random.randint(1,2)
        
        sp=[(str(humanrange1(len(x))),humanrange(len(x))),(str(humanrange1(len(x)//2)),humanrange(len(x)//2)),(str(humanrange1(len(x)*2)),humanrange(len(x)*2)),(str(humanrange1(len(x)**2)),humanrange(len(x)**2))]
        
        if y==2:
            
            self.vvv = (' Определите размер следующего предложения в кодировке Unicode:',x)
            
            self.g=sp[2]
        
        else:
            
            self.vvv= (' Определите размер следующего предложения в кодировке КОИ-8:',x)
            
            self.g=sp[0]

#-------------------------------------------------------------------------------    
    
        '''ФОРМИРОВАНИЕ ВАРИАНТОВ ОТВЕТА'''
        
        self.h=sp.pop(random.randint(0,len(sp)-1))
        self.hh=sp.pop(random.randint(0,len(sp)-1))
        self.hhh=sp.pop(random.randint(0,len(sp)-1))
        self.hhhh=sp.pop(random.randint(0,len(sp)-1))
              
#-------------------------------------------------------------------------------
             
        '''ИНИЦИАЛИЗАЦИЯ ТЕКСТОВЫХ ПОЛЕЙ - LABEL'''
        
        self.l1 = QLabel(self)
        self.l1.resize(900,50)
        self.l1.move(100, 152)
 
        self.l2 = QLabel(self)
        self.l2.move(700,430)
        self.l2.resize(400,50)
        
        self.l3 = QLabel(self)
        self.l3.move(700, 400)
        self.l3.resize(400,50)
        
        self.l4 = QLabel(self)
        self.l4.move(150, 240)
        self.l4.resize(400,50) 
        
        self.l5 = QLabel(self)
        self.l5.move(150, 290)
        self.l5.resize(400,50)         
        
        
        self.l6 = QLabel(self)
        self.l6.move(150, 340)
        self.l6.resize(400,50)         
      
        
        self.l7 = QLabel(self)
        self.l7.move(150, 390)
        self.l7.resize(400,50)                 

#-------------------------------------------------------------------------------        
        
        '''ИНИЦИАЛИЗАЦИЯ КНОПОК - BUTTON'''
        
        self.button_1 = QPushButton('Начать испытание',self) 
        self.button_1.resize(150,50)
        self.button_1.move(70,20)
        self.button_1.clicked.connect(self.run) 
        
        self.button_2 = QPushButton('Проверить ответ',self)
        self.button_2.resize(100,20)
        self.button_2.move(700, 295)
        self.button_2.clicked.connect(self.otvet2)
        
        self.button_3 = QPushButton('Проверить ответ',self)
        self.button_3.resize(100,20)
        self.button_3.move(700,245)
        self.button_3.clicked.connect(self.otvet)
        
        self.button_4 = QPushButton('Проверить ответ',self)
        self.button_4.resize(100,20)
        self.button_4.move(700,345)
        self.button_4.clicked.connect(self.otvet3)
        
        self.button_5 = QPushButton('Проверить ответ',self)
        self.button_5.resize(100,20)
        self.button_5.move(700,395)
        self.button_5.clicked.connect(self.otvet4)

#-------------------------------------------------------------------------------        

    '''ПРОВЕРКА ВВЕДЕННОГО ОТВЕТА'''      
    
    def otvet(self):
        
        self.a = 1
        
        if self.h==self.g:
            
            if self.a == 1:
                
                self.l3.setText('Excelent!') 
        else:
            
            self.l3.setText('Wrong answer!')
            
            self.l2.setText(" ".join(self.g)) 
        
   
    def otvet2(self):  
        
        self.a = 2
        
        if self.hh==self.g:
            
            if self.a == 2:
                
                self.l3.setText('Excelent!') 
        
        else:
            
            self.l3.setText('Wrong answer!')
            
            self.l2.setText(" ".join(self.g))        


    
    def otvet3(self):
        
        self.a = 3
        
        if self.hhh==self.g:
            
            if self.a == 3:
                
                self.l3.setText('Excelent!') 
        
        else:
            
            self.l3.setText('Wrong answer!')
            
            self.l2.setText(" ".join(self.g))         

    
    
    def otvet4(self):
        
        self.a = 4
        
        if self.hhhh==self.g:
            
            if self.a == 4:
                
                self.l3.setText('Excelent!') 
        
        else:
            
            self.l3.setText('Wrong answer!')
            
            self.l2.setText(" ".join(self.g))

#-------------------------------------------------------------------------------             

    '''ФУНКЦИЯ ЗАПУСКА'''
        
    def run(self): 
        
        self.l1.setText('.'.join(self.vvv))
        self.l4.setText(" ".join(self.h))
        self.l5.setText(" ".join(self.hh))
        self.l6.setText(" ".join(self.hhh))
        self.l7.setText(" ".join(self.hhhh))
        self.button_1.clicked.connect(self.initUI)        
    
#-------------------------------------------------------------------------------

app = QApplication(sys.argv)

ex = MyWidget()

ex.show()

sys.exit(app.exec_())
                             
                             #THE END
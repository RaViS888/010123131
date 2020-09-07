import PySimpleGUI as sg    

# Layout                                                         # Creat GUI
layout = [[sg.Txt(''  * 10)],                      
          [sg.Text('', size=(100, 1), font=('Helvetica', 18), text_color='black', key='input',background_color='white')],
          [sg.Txt(''  * 10)],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3')],
          [sg.ReadFormButton('0'), sg.ReadFormButton('=',button_color=('black', '#8CE82F')), sg.ReadFormButton('c',button_color=('white', '#D74323'))]
          ]

# Set PySimpleGUI
form = sg.FlexForm('0-9',size=(400,500) ,default_button_element_size=(10, 5), auto_size_buttons=False,auto_size_text=20 , grab_anywhere=False)
form.Layout(layout)

# Set Process
Equal = ''

# Loop
while True:
    button, value = form.Read()                            # call GUI
    
    # Press Button
    if button is 'c':
        Equal = ''
        form.FindElement('input').Update(Equal)
    elif len(Equal) == 50 :
        pass
    elif str(button) in '1234567890':
        Equal += str(button)
        form.FindElement('input').Update(Equal) 
    elif button == '=':
        print('You entered ', Equal)
    elif button is 'Quit'  or button == sg.WIN_CLOSED :                            # QUIT Program
        break

form.close()

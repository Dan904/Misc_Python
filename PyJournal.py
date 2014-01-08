from tkinter.filedialog import askopenfile
 
date = input('Please enter the date:')
time = input('Please enter the time:')
entry = input('Please share your thoughts:')
 
select_file = askopenfile(mode='a', title='Select the journal file.')
select_file.write(str(('-------------' +
                       '\n' + date + ' ' + time + '\n' +
                       '-------------' +
                       '\n\n' + entry + '\n\n\n')))
select_file.close()
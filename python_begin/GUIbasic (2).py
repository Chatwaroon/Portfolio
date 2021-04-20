from tkinter import *
from tkinter import ttk, messagebox # ttk is theme of tk
import random
import csv

# CSV File
def WritetoCSV(data):
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('บันทึกไฟล์สำเร็จ')

def ReadCSV():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file) #fr = file reader
		data = list(fr)
	#print(data)
	return data #return คือ การส่งข้อมูลไปใช้งานต่อ

# เครื่องหมาย # คือการคอมเมนท์

# main program
GUI = Tk() # Tk() คือหน้าจอหลักโปรแกรม
GUI.title('โปรแกรมของฉัน')
GUI.geometry('700x700') # 500 = กว้าง, 300= สูง

# font
FONT1 = ('Angsana New', 20, 'bold')
FONT2 = ('Angsana New', 20)


# Tab Menu
Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)

Tab.add(T1,text='Add')
Tab.add(T2,text='Flash Card')

Tab.pack(fill=BOTH, expand=1)


# title
L1 = ttk.Label(T1,text='หัวข้อ', font=FONT1,foreground='green')
L1.pack() #นำ L1 ไปติดกับโปรแกรมหลัก

# L1 = Label(GUI,text='หัวข้อ', font=FONT1,fg='green',bg='red')

# text box 1
v_title = StringVar() # StringVar() เป็นตัวแปรพิเศษ ไว้เก็บข้อมูลใน GUI
E1 = ttk.Entry(T1, textvariable=v_title, font=FONT2, width=30)
E1.pack()

# detail
L2 = ttk.Label(T1,text='รายละเอียด', font=FONT1,foreground='green')
L2.pack()

# text box 2
v_detail = StringVar()
E2 = ttk.Entry(T1, textvariable=v_detail,  font=FONT2, width=40)
E2.pack()


# สร้างฟังชั่นชื่อ update table
def UpdateTable():
	table.delete(*table.get_children()) #clear ข้อมูลชุดเก่าแล้วจึงอัพเดตชุดใหม่เข้าไป
	alldata = ReadCSV() #เรียกฟังชั่นอ่าน csv จากด้านบนมา
	for row in alldata:
		table.insert('','end',value=row)

# Button Save
def SaveButton(event=None):
	title = v_title.get() # .get() ดึงข้อมูลจากตัวแปร v_title
	detail = v_detail.get()
	print(title)
	print(detail)
	dt = [title,detail] #dt = data
	WritetoCSV(dt)
	print('กำลังบรรทึกข้อมูล...')
	# clear ข้อมูล
	v_title.set('') #สั่งเคลียร์ข้อมูลให้ว่าง
	v_detail.set('') #เคลียร์ข้อมูลให้ว่าง
	E1.focus() #ทำให้เคอร์เซอร์ไปอยู่ตำแหน่งช่องกรอกแรก
	UpdateTable() #อัพเดตข้อมูลทุกครั้งที่มีการบันทึก
	global allquestion
	allquestion = ReadCSV()
	

E2.bind('<Return>',SaveButton)
E2.bind('<Control-s>',SaveButton)
# E2.bind() เช็คในช่องกรอกที่ 2 ว่ามีการกดปุ่ม enter หรือไม่ หากกดให้ทำการเรียกฟังชั่น SaveButton

B1 = ttk.Button(T1,text='Save',command=SaveButton)
B1.pack(ipadx=30,ipady=20,pady=20)

# ipadx = ระยะห่างภายในปุ่ม แนวแกน x
# pady = ระยะห่างด้านนอกปุ่ม ทั้งบนและล่างแนวแกน y


# table

# Setting font for Table
style = ttk.Style()
style.configure('Treeview.Heading',font=('Angsana New',20))
style.configure('Treeview',font=('Angsana New',18),rowheight=30)


header = ['Title','Detail']

table = ttk.Treeview(T1,height=10,column=header, show='headings')
table.place(x=20,y=300)

table.heading('Title',text='หัวข้อ') #โชว์คำว่าหัวข้อที่คอลัมน์ Title
table.column('Title',width=200) #ปรับความกว้าง
table.heading('Detail',text='รายละเอียด') #โชว์คำว่ารายละเอียดที่คอลัมน์ Title
table.column('Detail',width=460) #ปรับความกว้าง


# ทดลองใส่ข้อมูล
'''
row = ['GUI คืออะไร?','GUI : Graphical User Interface']
table.insert('','end',value=row)
row = ['GUI คืออะไร?','GUI : Graphical User Interface']
table.insert('','end',value=row)
row = ['GUI คืออะไร?','GUI : Graphical User Interface']
table.insert('','end',value=row)
row = ['.insert()','คือการใส่ข้อมูลเข้าไป']
table.insert('',2,value=row)
'''
#print(help(ttk.Treeview))


def DeleteQuestion(event=None):
	select = table.selection() # ช่วยดูหน่อยว่ามีการเลือกคำถามข้อไหน?
	data = table.item(select)
	print(data['values'])
	allquestion.remove(data['values'])
	print('Count:',len(allquestion))

	# กรณีที่ต้องการลบเฉพาะค่าในโปรแกรม
	table.delete(*table.get_children()) #clear ข้อมูลชุดเก่าแล้วจึงอัพเดตชุดใหม่เข้าไป
	alldata = allquestion #เรียกฟังชั่นอ่าน csv จากด้านบนมา
	for row in alldata:
		table.insert('','end',value=row)

table.bind('<Delete>',DeleteQuestion)


def SaveQuestion(event=None):
	check = messagebox.askquestion('ยืนยันการบันทึกข้อมูล','คุณต้องการบันทึกข้อมูลล่าสุดใช่หรือไม่? ข้อมูลเก่าจะหายหมด!')
	print(check)
	if check == 'yes':
		with open('data.csv','w',newline='',encoding='utf-8') as file:
			# 'w' replace to current file
			fw = csv.writer(file) # fw = file writer
			fw.writerows(allquestion) # allquestion ล่าสุดจะถูกบันทึกแทน [['1+1=?','2'],['2+2=?','4']]
		print('บันทึกไฟล์สำเร็จ')
		# from tkinter import ttk, messagebox # ต้องการโชว์ป็อปอัพต้องดึง messagebox
		messagebox.showinfo('Saving...','บันทึกข้อมูลสำเร็จ')

GUI.bind('<F1>',SaveQuestion)
L = ttk.Label(T1,text='หากต้องการบันทึกค่าล่าสุด กรุณากดปุ่ม <F1>')
L.pack()


######################TAB 2########################
v_question = StringVar() #ใช้สำหรับเก็บคำถาม
v_question.set('--------คำถาม (กดปุ่ม Next เพื่อเริ่ม)--------')
R1 = ttk.Label(T2,textvariable=v_question,font=FONT1)
R1.pack(pady=20)

v_answer = StringVar()
v_answer.set('------กดปุ่ม Show เพื่อแสดงคำตอบ-------')
R2 = ttk.Label(T2,textvariable=v_answer,font=FONT1)
R2.pack(pady=20)

## BUTTON
BF1 = Frame(T2) # BF Button Frame
BF1.pack(pady=100)


allquestion = ReadCSV() # [['1+1=?','2'],['2+2=?','4']]


v_current_ans = StringVar() #คำตอบที่ซ่อนอยู่
def Next():
	# import random
	v_answer.set('------กดปุ่ม Show เพื่อแสดงคำตอบ-------') #reset คำตอบ
	q = random.choice(allquestion) # q = ['1+1=?','2']
	v_question.set(q[0])
	v_current_ans.set(q[1])
	BC3['state'] = 'enabled'

def Show():
	v_answer.set(v_current_ans.get()) #ดึงคำตอบล่าสุดที่ซ่อนอยู่ไปโชว์ที่ตำแหน่ง v_answer


# โชว์คะแนนที่ได้
score = 0
v_score = StringVar()
v_score.set('Score: {}'.format(score))
Score = ttk.Label(T2,textvariable=v_score,font=('Impact',30))
Score.place(x=20,y=20)

def ScoreUp():
	global score
	score += 1 # score = score + 1
	v_score.set('Score: {}'.format(score))
	BC3['state'] = 'disabled'




BC1 = ttk.Button(BF1,text='Next',command=Next)
BC2 = ttk.Button(BF1,text='Show',command=Show)
BC3 = ttk.Button(BF1,text='Score +1',command=ScoreUp)
BC1.grid(row=0,column=0,ipadx=20,ipady=30)
BC2.grid(row=0,column=1,ipadx=20,ipady=30)
BC3.grid(row=0,column=2,ipadx=20,ipady=30)




# โหลดข้อมูลจาก csv เข้าไปในโปรแกรม
UpdateTable()
  

GUI.mainloop()
# GUI.mainloop() จาก GUI จะทำให้โปรแกรมรันตลอด

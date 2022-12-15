import time
import re
import urllib
import string
from datetime import date, time, datetime, timedelta
import requests
from lxml import html
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
API_TOKEN = '5888106586:AAGAG1wZjtHvhKFfrKcJK144TN9KPAvlQ2A'
bot = Bot(token=API_TOKEN)
wkstart = 0
def datafun():
   tdt = datetime.today()
   wk = tdt.isoweekday()
   td = datetime.date(tdt)
   ddec = timedelta(days=1)
   ddec1 = timedelta(days=2)
   ddec2 = timedelta(days=3)
   ddec3 = timedelta(days=4)
   if wk == 1:
      wkstart = td
   elif wk == 2:
      wkstart = (td - (ddec))
   elif wk == 3:
      wkstart = (td - (ddec + ddec))
   elif wk == 4:
      wkstart = (td - (ddec1 + ddec))
   elif wk == 5:
      wkstart = (td - (ddec2 + ddec))
   wks = str(wkstart)
   data = {
   'faculty': 'Лингвистический факультет',
   'speciality': 'Белорусский язык и литература. Иностранный язык (английский)',
   'groups': 'БИЯ21',
   'weekbegindate': wks, 
   'go': 'Показать'
   }



   return data
data=datafun()

def wkfun():
   tdt = datetime.today()
   wk = tdt.isoweekday()
   td = datetime.date(tdt)
   ddec = timedelta(days=1)
   ddec1 = timedelta(days=2)
   ddec2 = timedelta(days=3)
   ddec3 = timedelta(days=4)
   if wk == 1:
      wkstart = td
   elif wk == 2:
      wkstart = (td - (ddec))
   elif wk == 3:
      wkstart = (td - (ddec + ddec))
   elif wk == 4:
      wkstart = (td - (ddec1 + ddec))
   elif wk == 5:
      wkstart = (td - (ddec2 + ddec))


   return wk
wk=wkfun()

dp = Dispatcher(bot=bot)

wks = str(wkstart)

s = requests.post('http://rasp.barsu.by/stud.php', data=data, files=data)
bs = BeautifulSoup(s.text,"html.parser")
table = bs.find('table', class_='table table-bordered')
table_body = table.find('tbody')
avs = str(table)
my_file = open("table.html", "w+")
my_file.write(avs)
my_file.close()
sch = str((html.fromstring(avs).text_content()))
sch = sch.replace('10.05-11.25', '')
sch = sch.replace('19.30-20.50', '')
sch = sch.replace('8.30-9.50', '')
sch = sch.replace('13.25-14.45', '')
sch = sch.replace('14.55-16.15', '')
sch = sch.replace('16.30-17.50', '')
sch = sch.replace('18.00-19.20', '')
sch = sch.replace('11.55-13.15', '')

#sch = sch.replace('ПЗ', 'СЗ\n')
sch = sch.replace('\n\n', '\n')
lines = []
lines = sch.split('\n')
l = 0

while l < len(lines):
   if lines[l].find('ПЗ') > 0:
      lines[l] = lines[l].replace(' ПЗ  ', ' ')
      lines[l] = ' ПЗ,' + lines[l]
      lines[l] = lines[l].replace('  ', ' ')
   if lines[l].find('СЗ') > 0:
      lines[l] = lines[l].replace(' СЗ  ', ' ')
      lines[l] = ' СЗ,' + lines[l]
      lines[l] = lines[l].replace('  ', ' ')
   if lines[l] == ' 14.55-16.15  ':
      lines[l] = ''
   if lines[l] == ' 16.30-17.50  ':
      lines[l] = ''
   if lines[l] == ' 18.00-19.20  ':
      lines[l] = ''
   l += 1
   
pns = str('  ПН  -----------------' + '\n' + '1️⃣ ' + lines[10] + '\n') + str('2️⃣ ' + lines[11] + '\n') + str('3️⃣ ' + lines[12] + '\n') + str('4️⃣ ' + lines[13] + '\n') + str('5️⃣ ' + lines[14])
pn1 = str(lines[10])
pn2 = str(lines[11])
pn3 = str(lines[12])
pn4 = str(lines[13])
pn5 = str(lines[14])

vt1 = str(lines[20])
vt2 = str(lines[21])
vt3 = str(lines[22])
vt4 = str(lines[23])
vt5 = str(lines[24])

sr1 = str(lines[30])
sr2 = str(lines[31])
sr3 = str(lines[32])
sr4 = str(lines[33])
sr5 = str(lines[34])

ct1 = str(lines[40])
ct2 = str(lines[41])
ct3 = str(lines[42])
ct4 = str(lines[43])
ct5 = str(lines[44])

pt1 = str(lines[50])
pt2 = str(lines[51])
pt3 = str(lines[52])
pt4 = str(lines[53])
pt5 = str(lines[54])
print(lines)
vts = str('  ВТ  -----------------' + '\n' + '1️⃣ ' + lines[20] + '\n') + str('2️⃣ ' + lines[21] + '\n') + str('3️⃣ ' + lines[22] + '\n') + str('4️⃣ ' + lines[23] + '\n') + str('5️⃣ ' + lines[24])
srs = str('  СР  -----------------' + '\n' + '1️⃣ ' + lines[30] + '\n') + str('2️⃣ ' + lines[31] + '\n') + str('3️⃣ ' + lines[32] + '\n') + str('4️⃣ ' + lines[33] + '\n') + str('5️⃣ ' + lines[34])
cts = str('  ЧТ  -----------------' + '\n' + '1️⃣ ' + lines[40] + '\n') + str('2️⃣ ' + lines[41] + '\n') + str('3️⃣ ' + lines[42] + '\n') + str('4️⃣ ' + lines[43] + '\n') + str('5️⃣ ' + lines[44])
pts = str('  ПТ  -----------------' + '\n' + '1️⃣ ' + lines[50] + '\n') + str('2️⃣ ' + lines[51] + '\n') + str('3️⃣ ' + lines[52] + '\n') + str('4️⃣ ' + lines[53] + '\n') + str('5️⃣ ' + lines[54])
pnss = ''.join(pns)  
vtss = ''.join(vts)  
srss = ''.join(srs)  
ctss = ''.join(cts)  
ptss = ''.join(pts)  
print(pn1)
pn = pnss
vt = vtss
sr = srss
ct = ctss
pt = ptss
x = 1
nice = []

for x in lines:
        g = 8
        lines[g] = '--------------------------------------'
        nice.append(x)
        g += 7
sgh = ('\n'.join(lines))


button_td = KeyboardButton('На сегодня')
button_tm = KeyboardButton('На завтра')
button_wk = KeyboardButton('На всю неделю')
wek = '\n' + pn + '\n' + vt + '\n' + sr + '\n' + ct + '\n' + pt

lk = ''
print(sr5)
if len(pn1) > 3:
   pn1 = '1️⃣ ' + '11.55-13.15' + '\n' + pn1
if len(pn2) > 3:  
   pn2 = '2️⃣ ' + '13.25-14.45' + '\n' +pn2
if len(pn3) > 3:   
   pn3 = '3️⃣ ' + '14.55-16.15' + '\n' +pn3
if len(pn4) > 3: 
   pn4 = '4️⃣ ' + '16.30-17.50' + '\n' +pn4
if len(pn5) > 3:
   pn5 = '5️⃣ ' + '18.00-19.20' + '\n' + pn5

if len(vt1) > 3:
   vt1 = '1️⃣ ' + '11.55-13.15' + '\n' + vt1
if len(vt2) > 3:  
   vt2 = '2️⃣ ' + '13.25-14.45' + '\n' +vt2
if len(vt3) > 3:   
   vt3 = '3️⃣ ' + '14.55-16.15' + '\n' +vt3
if len(vt4) > 3: 
   vt4 = '4️⃣ ' + '16.30-17.50' + '\n' +vt4
if len(vt5) > 3:
   vt5 = '5️⃣ ' + '18.00-19.20' + '\n' + vt5

if len(sr1) > 3:
   sr1 = '1️⃣ ' + '11.55-13.15' + '\n' + sr1
if len(sr2) > 3:  
   sr2 = '2️⃣ ' + '13.25-14.45' + '\n' +sr2
if len(sr3) > 3:   
   sr3 = '3️⃣ ' + '14.55-16.15' + '\n' +sr3
if len(sr4) > 3: 
   sr4 = '4️⃣ ' + '16.30-17.50' + '\n' +sr4
if len(sr5) > 3:
   sr5 = '5️⃣ ' + '18.00-19.20' + '\n' + sr5

if len(ct1) > 3:
   ct1 = '1️⃣ ' + '11.55-13.15' + '\n' + ct1
if len(ct2) > 3:  
   ct2 = '2️⃣ ' + '13.25-14.45' + '\n' +ct2
if len(ct3) > 3:   
   ct3 = '3️⃣ ' + '14.55-16.15' + '\n' +ct3
if len(ct4) > 3: 
   ct4 = '4️⃣ ' + '16.30-17.50' + '\n' +ct4
if len(ct5) > 3:
   ct5 = '5️⃣ ' + '18.00-19.20' + '\n' + ct5

if len(pt1) > 3:
   pt1 = '1️⃣ ' + '11.55-13.15' + '\n' + pt1
if len(pt2) > 3:  
   pt2 = '2️⃣ ' + '13.25-14.45' + '\n' +pt2
if len(pt3) > 3:   
   pt3 = '3️⃣ ' + '14.55-16.15' + '\n' +pt3
if len(pt4) > 3: 
   pt4 = '4️⃣ ' + '16.30-17.50' + '\n' +pt4
if len(pt5) > 3:
   pt5 = '5️⃣ ' + '18.00-19.20' + '\n' + pt5

markup3 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button_td).add(button_tm).add(button_wk)

markup4 = ReplyKeyboardMarkup(resize_keyboard=True).row(
    button_td, button_tm, button_wk
)

@dp.message_handler(text=['На всю неделю'])
async def process_start_command(message: types.Message):
    datafun()
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    await message.reply(wek, reply_markup=markup4)

@dp.message_handler(text=['На след. неделю'])
async def process_start_command(message: types.Message):
    datafun()
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    await message.reply(wek, reply_markup=markup4)    

@dp.message_handler(text=['На завтра'])
async def process_start_command(message: types.Message):
    datafun()
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    if wk == 7:
      if len(pn1) > 3: 
        await message.answer(pn1, reply_markup=markup4)
      if len(pn2) > 3:   
        await message.answer(pn2, reply_markup=markup4)
      if len(pn3) > 3:  
        await message.answer(pn3, reply_markup=markup4)
      if len(pn4) > 3:   
        await message.answer(pn4, reply_markup=markup4)
      if len(pn5) > 3:   
        await message.answer(pn5, reply_markup=markup4)
  
    if wk == 1:
      if len(vt1) > 3:
         await message.answer(vt1, reply_markup=markup4)
      if len(vt2) > 3: 
         await message.answer(vt2, reply_markup=markup4) 
      if len(vt3) > 3:
         await message.answer(vt3, reply_markup=markup4) 
      if len(vt4) > 3:
         await message.answer(vt4, reply_markup=markup4) 
      if len(vt5) > 3:
         await message.answer(vt5, reply_markup=markup4) 

    if wk == 2:
      if len(sr1) > 3:
         await message.answer(sr1, reply_markup=markup4)  
      if len(sr2) > 3: 
         await message.answer(sr2, reply_markup=markup4)  
      if len(sr3) > 3:
         await message.answer(sr3, reply_markup=markup4)  
      if len(sr4) > 3:
         await message.answer(sr4, reply_markup=markup4)  
      if len(sr5) > 3: 
         await message.answer(sr5, reply_markup=markup4) 

    if wk == 3:
      if len(ct1) > 3: 
       await message.answer(ct1, reply_markup=markup4)
      if len(ct2) > 3:  
       await message.answer(ct2, reply_markup=markup4)  
      if len(ct3) > 3:
       await message.answer(ct3, reply_markup=markup4)  
      if len(ct4) > 3:
       await message.answer(ct4, reply_markup=markup4)  
      if len(ct5) > 3: 
       await message.answer(ct5, reply_markup=markup4)     
    
    if wk == 4:
      if len(pt1) > 3: 
       await message.answer(pt1, reply_markup=markup4)    
      if len(pt2) > 3:  
       await message.answer(pt2, reply_markup=markup4)    
      if len(pt3) > 3:   
       await message.answer(pt3, reply_markup=markup4)    
      if len(pt4) > 3: 
       await message.answer(pt4, reply_markup=markup4)    
      if len(pt5) > 3:  
       await message.answer(pt5, reply_markup=markup4)

  





@dp.message_handler(text=['На сегодня'])
async def process_start_command(message: types.Message):
    datafun()
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    
    if wk == 1:
      if len(pn1) > 3: 
        await message.answer(pn1, reply_markup=markup4)
      if len(pn2) > 3:   
        await message.answer(pn2, reply_markup=markup4)
      if len(pn3) > 3:  
        await message.answer(pn3, reply_markup=markup4)
      if len(pn4) > 3:   
        await message.answer(pn4, reply_markup=markup4)
      if len(pn5) > 3:   
        await message.answer(pn5, reply_markup=markup4)
    elif wk == 2:
      if len(vt1) > 3:
         await message.answer(vt1, reply_markup=markup4)
      if len(vt2) > 3: 
         await message.answer(vt2, reply_markup=markup4) 
      if len(vt3) > 3:
         await message.answer(vt3, reply_markup=markup4) 
      if len(vt4) > 3:
         await message.answer(vt4, reply_markup=markup4) 
      if len(vt5) > 3:
         await message.answer(vt5, reply_markup=markup4) 
    elif wk == 3:
      if len(sr1) > 3:
         await message.answer(sr1, reply_markup=markup4)  
      if len(sr2) > 3: 
         await message.answer(sr2, reply_markup=markup4)  
      if len(sr3) > 3:
         await message.answer(sr3, reply_markup=markup4)  
      if len(sr4) > 3:
         await message.answer(sr4, reply_markup=markup4)  
      if len(sr5) > 3: 
         await message.answer(sr5, reply_markup=markup4)  
    elif wk == 4:
      if len(ct1) > 3: 
       await message.answer(ct1, reply_markup=markup4)
      if len(ct2) > 3:  
       await message.answer(ct2, reply_markup=markup4)  
      if len(ct3) > 3:
       await message.answer(ct3, reply_markup=markup4)  
      if len(ct4) > 3:
       await message.answer(ct4, reply_markup=markup4)  
      if len(ct5) > 3: 
       await message.answer(ct5, reply_markup=markup4)  
    elif wk == 5:
      if len(pt1) > 3: 
       await message.answer(pt1, reply_markup=markup4)    
      if len(pt2) > 3:  
       await message.answer(pt2, reply_markup=markup4)    
      if len(pt3) > 3:   
       await message.answer(pt3, reply_markup=markup4)    
      if len(pt4) > 3: 
       await message.answer(pt4, reply_markup=markup4)    
      if len(pt5) > 3:  
       await message.answer(pt5, reply_markup=markup4)    

executor.start_polling(dp)
print(sr5)

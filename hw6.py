subj = {}
with open("text_6.txt", "r", encoding="utf-8") as load_file:
   for line in load_file:
      subject, lecture, practice, lab = line.split()
      if lecture == '-':
         lecture = 0
      elif len(lecture)>2:
         lecture = lecture.replace('(л)', '')
      if practice == '-':
         practice = 0
      elif len(practice)>2:
         practice = practice.replace('(пр)', '')
      if lab == '-':
         lab = 0
      elif  len(lab)>2:
         lab = lab.replace('(лаб)', '')

      subj[subject] = int(lecture)+int(practice)+int(lab)
   print(subj)
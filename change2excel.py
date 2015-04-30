# coding=utf-8
import xlwt
content = raw_input("Please enter your filename: ").strip()
print content
f = open(content, "r")  
book=xlwt.Workbook(encoding='gbk',style_compression=0)
sheet=book.add_sheet('Data',cell_overwrite_ok=True)
i = 0
while True:  
	line = f.readline()  
	if line:  
		pass    
		strl = line.strip()
		sline = strl.split('|')
		j=0
		for sdata in sline:
			sheet.write(i,j,sdata)
			j=j+1
		i=i+1
	else:  
		break
f.close()
save_addr = raw_input("Please enter a save address &name: ").strip()
book.save(save_addr)


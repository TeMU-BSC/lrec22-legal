import pdftotext
import re

# Load your PDF
with open("procesos_penales_es.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# with open("procesos_penales_es.txt", "w") as f:
# 	for page in pdf:
# 		f.write(page)

#s'ha danar linia per linia
count = 1
last_f = "index.txt"
# Iterate over all the pages
# Each page is treated as a string
lines_to_remove = ["ESCRITO DEL MINISTERIO FISCAL","ESCRITO DE LA DEFENSA","JUICIO ORAL","SENTENCIA",""]
regex_pattern = "(\[Nº de palabras: *\])|#?[0-9]+"

for page in pdf:
	for line in page.split("\n"):
			line = re.sub('^ *[0-9]* ','',line)
			if "ESCRITO DEL MINISTERIO FISCAL" in line:
				f = str(count)+"_ministerio_fiscal.txt"
			elif "ESCRITO DE LA DEFENSA" in line:
				f = str(count)+"_defensa.txt"
			elif "JUICIO ORAL" in line:
				f = str(count)+"_juicio_oral.txt"
			elif "SENTENCIA" in line:
				f = str(count)+"_sentencia.txt"
				count += 1
			else:
				f = last_f
			if re.sub(regex_pattern,'',line) not in lines_to_remove:
				fwrite = open(f,"a")
				fwrite.write(line)
				fwrite.write("\n")
			else:
				print(line)
			last_f = f
# How many pages?
# Read all the text into one string
#print("\n\n".join(pdf))

#1 ministeriofiscal, dfemsa, juicio oral, sntenc

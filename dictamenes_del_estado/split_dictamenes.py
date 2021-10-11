index = 0
with open('dictamenes_consejo_estado_es_22012021.txt','r') as file:
	fr = file.read()
	file_split = fr.split("TEXTO DEL DICTAMEN\n")
	for doc_content in file_split:
		with open("dictamenes_split/dictamenes_"+str(index)+'.txt', 'w') as write_doc:
			write_doc.write(doc_content)
			index += 1

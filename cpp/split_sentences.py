from sentence_splitter import SentenceSplitter, split_text_into_sentences
import glob
import re

splitter = SentenceSplitter(language='es')

for val_file in glob.iglob('txt_val/*'):
    if 'juicio_oral' not in val_file:
        filename = re.sub('val','sentence_split',val_file)
        with open(filename,'w') as ss_file:
            with open(val_file,'r') as vl_file:
                doc = vl_file.read()
                ss_file.write('\n'.join(splitter.split(text=doc)))
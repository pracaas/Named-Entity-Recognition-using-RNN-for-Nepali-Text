
# coding: utf-8
# @ author : Prakash Poudel
# In[13]:

def readfilen(filename,frm,to):
    import xlrd
    wb = xlrd.open_workbook(filename) 
    sentences = []
    sentence = []
    # this part is  for checking
    osent =[]
    osents=[]
    sent = []
    sents=[]
    # this part is for checking end items
    endwo = []
    sencount = 0
    mysheet = []
    endwos = []
    #addr = "/Users/prakash/nepali_stopwords.txt"
    
    #with open(addr, 'r') as test:
    #    filee=test.readlines()
    #    stpwords = [[stpwrd.replace('\n', '')] for stpwrd in filee]
    #    #print(stpwords)
    #    stpwords = ["".join(stpword) for stpword in stpwords]
    #    #print(stpwords)
        
    
    for j in range(frm,to):
        sheet = wb.sheet_by_index(j)
        
        mysheet.append(sencount)
        for i in range(sheet.nrows):
            
            
            word = sheet.cell_value(i, 1)
            
            word = str(word)
            
            label = sheet.cell_value(i,2)
            
            #if word in stpwords:
            #    word=""
            word = word.replace('"','')
            word=word.replace('\n', '')
            word=word.replace('’', '')
            word=word.replace(',', '')
            word=word.replace('\t', '')
            word=word.replace("'", '')
            word=word.replace("‘", '')
            word=word.replace(":", '')
            word=word.replace("¥", '')
            word=word.replace("…", '')
            word=word.replace("\u200d", '')
            word=word.replace(":", '')
            word=word.replace("(", '')
            word=word.replace(")", '')
            word=word.replace("\ufeff", '')
            word=word.replace("-", '')
            word=word.replace("?", '।')
            
            '''
            if i == sheet.nrows:
                a = 0
            else:
                wordnx = sheet.cell_value(i+1,0)
                if '।' in wordnx or '|' in wordnx:
                    endwos.append(word)
            '''
            #  \ufeff \n \ .,-_[]{}!?;#'\"/\\%$`&=*+@^~|":
            
            
            if '।' in word or '|' in word:
                sencount=sencount +1
                if '\n' in word:
                    word=word.replace('\n', '')
                word = str(word)
                osent.append(word)
                osents.append(osent)
                
                osent=[]
                if word == '।' or word == '|' and len(word)==1:
                    #print(word)
                    endwo.append(word)
                    #print(word)
                    sent.append(str(word)+"-End only ।")
                    sentences.append(sentence)
                    sents.append(sent)
                    sent = []
                    sentence=[]
                    
                elif word[0]== '।' or word[0]== '|':
                    ab = str(len(word))
                    
                    #print(word+"-"+ab+"--under 1st--End")
                    
                    endwo.append(word[0])
                    
                    sentences.append(sentence)
                    sentence=[]
                    
                    sent.append(word[0]+"-।End")
                    sents.append(sent)
                    sent=[]
                    
                    sent.append(word[1:])
                    sentence.append([word[1:],label])
                    '''
                    if word[1:] in stpwords:
                        word=""
                        
                    else:
                        sent.append(word[1:])
                        sentence.append([word[1:],label])
                    '''
                
                elif word[-1]== '।' or word[-1]== '|':
                    
                    ab = str(len(word))
                    #print(word+"-"+ab+"--under last--End")
                    
                    endwo.append(word[-1])
                    
                    #sentence.append([word[:-1],label])
                    endwos.append(word[:-1])
                    
                    #sentences.append(sentence)
                    #sentence=[]
                    
                    sent.append(word[:-1])
                    sent.append(word[-1]+"-End।")
                    sents.append(sent)
                    sent=[]
                    label="O"
                    sentence.append([word[:-1],label])
                    sentences.append(sentence)
                    sentence =[]
                    '''
                    if word[:-1] in stpwords:
                            word=""
                    else:
                        sentence.append([word[:-1],label])
                        sentences.append(sentence)
                        sentence =[]
                    '''
                    
                else:
                    
                    ab = str(len(word))
                    #print(word+"-"+ab+"--under last--End")
                    if '।' in word:
                        var='।'
                    elif '|' in word:
                        var = '|'
                    splt = word.split(var)
                    if len(splt) < 3:
                        
                        #sentence.append([splt[0],"O"])
                        #sentences.append(sentence)
                        #sentence=[]
                        
                        endwo.append('।')
                        
                        sent.append(splt[0] + "-En।d")
                        sents.append(sent)
                        sent=[]
                        sent.append(splt[1])
                        
                        endwos.append(splt[0])
                        
                        sentence.append([splt[0],"O"])
                        sentences.append(sentence)
                        sentence=[]
                        
                        sentence.append([splt[1],label])
                        
                        
                        '''
                        if splt[1] in stpwords:
                            word=""
                        else:
                            sentence.append([splt[1],label])
                        '''
                        
                    else:
                        print("Multiple '।' in a word "+word+" Length "+str(splt))
                    
                
            elif str(word) == "" and label !="":
                #print(str(label)+" Empty word with label found")
                a = 0
                
                #print(str(j+1)+"Sheet and Row - "+str(i+1)+" Both word and label is blank") 
            #if label == "":
                
            elif str(label) is "":
                if word == "":
                    a=0
                else:
                    label = "O"
                    osent.append(str(word))
                    word=str(word).rstrip('\n')
                    sentence.append([word,label])     
                    sent.append(str(word))
                    #print(str(j)+" "+str(i)+" Empty label of word"+word)

            else:
                
                osent.append(str(word))
                word=str(word).rstrip('\n')
                sentence.append([word,label])     
                sent.append(str(word))
            if label == "" and word != "":
                a = 0
                #print(str(j)+" "+str(i)+word+" this word label is empty -"+label)
                
                #print(word+label+"ok")
    return sentences
    #return sentences,sents,osents,mysheet
    #mysheet,sents,osents


#addrsrc ="/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/data2.xlsx"
#NSentences,sento,ori,sht = readfilen(addrsrc,0,8)
#NSentences = readfilen(addrsrc,0,8)
# Type here to limit the data

#print(sento[115:117])
#print(NSentences[111:117])
#NSentences = NSentences[:2]


#for i in NSentences:
#    sn = "" p
#    for j in i:
   

#allWords = [[wod[0] for wod in sen] for sen in nee]

'''
bo = []
a = 0
so = []

for i in range(2500,3000):
    ds=sento[i]
    os=ori[i]
    #for i in ori[:3]:
    #    print(i)
    oa = ' '.join(os)
    da = ' '.join(ds)
    opin = str(i)+" "+oa
    pin =str(i)+" "+da
    print(opin)
    print(pin)
    
    so.append(pin)
    a = a+1
allWords = []
allTags = []
siz = []

'''


'''
for i in  NSentences:
    Sen = ""
    print("\n")
    siz.append(len(i))
    for wod in i:
        allWords.append(wod[0])        
        allTags.append(wod[1])
        Sen = Sen+str(wod[0])+" "
    print(Sen)
sz=max(siz)
'''


def fltrxl(filename,j):
    import xlrd
    import xlsxwriter

    wb = xlrd.open_workbook(filename)     
    
    
    addrdes ="/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/allinone test1.xlsx"
    workbook = xlsxwriter.Workbook(addrdes)
    name = 'Filtered'
    worksheet = workbook.add_worksheet(name)
    
    
    sheet = wb.sheet_by_index(j)
    
    
    count = 0
    for i in range(sheet.nrows):
        
        
        word = sheet.cell_value(i, 1)
        word = str(word)
        
        label = sheet.cell_value(i,2)
        
        #if word in stpwords:
        #    word=""
        word = word.replace('"','')
        word=word.replace('\n', '')
        word=word.replace('’', '')
        word=word.replace(',', '')
        word=word.replace('\t', '')
        word=word.replace("'", '')
        word=word.replace("‘", '')
        word=word.replace(":", '')
        word=word.replace("¥", '')
        word=word.replace("…", '')
        word=word.replace("\u200d", '')
        word=word.replace("\u200c", '')
        word=word.replace(":", '')
        word=word.replace("(", '')
        word=word.replace(")", '')
        word=word.replace("\ufeff", '')
        word=word.replace("-", '')
        word=word.replace("?", '।')
        
        if '।' in word or '|' in word:
            if word == '।' or word == '|':
                
                wod = word
                label = label
                oword = sheet.cell_value(i, 0)
                
                worksheet.write(count,2,wod)
                worksheet.write(count,3,label)
                worksheet.write(count,0,oword)
                count += 1
                
            elif word[0]== '।' or word[0]== '|':
                
                wod = word[0]
                label = "O"
                oword = sheet.cell_value(i, 0)
                
                worksheet.write(count,2,wod)
                worksheet.write(count,3,label)
                worksheet.write(count,0,oword)
                count += 1
                
                
                wod = word[1:]
                label = sheet.cell_value(i,3)
    
                worksheet.write(count,2,wod)
                worksheet.write(count,3,label)
                worksheet.write(count,0,oword)
                count += 1
                
            elif word[-1]== '।' or word[-1]== '|':
                
                wod = word[:-1]
                label = label
                
                oword = sheet.cell_value(i, 0)
                
                worksheet.write(count,2,wod)
                worksheet.write(count,3,label)
                worksheet.write(count,0,oword)
                count += 1
                
                wod = word[-1]
                label = "O"
                
                worksheet.write(count,2,wod)
                worksheet.write(count,3,label)
                worksheet.write(count,0,oword)
                count += 1                
                
            else:
                
                if '।' in word:
                    var='।'
                elif '|' in word:
                    var = '|'
                splt = word.split(var)
                if len(splt) < 3:
                    
                    wod = splt[0]
                    label = "O"
                    oword = sheet.cell_value(i, 0)
                    
                    worksheet.write(count,2,wod)
                    worksheet.write(count,3,label)
                    worksheet.write(count,0,oword)
                    count += 1
                        
                    wod = var
                    label = "O"
                    
                    worksheet.write(count,2,wod)
                    worksheet.write(count,3,label)
                    worksheet.write(count,0,oword)
                    count += 1
                    
                    wod = splt[1]
                    label = sheet.cell_value(i,3)
                    
                    worksheet.write(count,2,wod)
                    worksheet.write(count,3,label)
                    worksheet.write(count,0,oword)
                    count += 1
                    
                else:
                    print("Multiple '।' in a word "+word+" Length "+str(splt))
        else:
                
            oword = sheet.cell_value(i, 0)
            worksheet.write(count,2,word)
            worksheet.write(count,3,label)
            worksheet.write(count,0,oword)
            count += 1
        
    workbook.close()
            
#addrsss = "/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/allinone test .xlsx"
#fltrxl(addrsss,1)
      
def readxl_write(filename,j):
    import xlrd
    import xlsxwriter

    addrdes ="/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/allinone backup.xlsx"
    workbook = xlsxwriter.Workbook(addrdes)
    name = 'Bam tag2'
    worksheet = workbook.add_worksheet(name)
    
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(j)
    allword = []
    
    allper,allloc,allorg,allmisc = checktxt()
    
    for i in range(sheet.nrows):
        
        word = sheet.cell_value(i, 1)
        olabel = sheet.cell_value(i,2)
        word = str(word)
        if olabel == "O":
            if word in allper:
                label = "B-PER"
            elif word in allloc:
                label = "B-LOC"
            elif word in allorg:
                label = "B-ORG"
            #elif word in allmisc:
                #label = "MISC"
            else:
                label = "O"
        else:
            label = olabel
        
        worksheet.write(i,0,word)
        worksheet.write(i,3,label)
        worksheet.write(i,2,olabel)
        
        
        allword.append(word)
        
    workbook.close()

#adds="/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/allinone test1.xlsx"
#readxl_write(adds,1)

def checktxt():
    loc = "/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/Bam Dataset/Final dictionary/2_location.txt"
    per = "/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/Bam Dataset/Final dictionary/1_person.txt"
    org = "/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/Bam Dataset/Final dictionary/3_organization.txt"
    misc = "/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/Bam Dataset/Final dictionary/4_misc.txt"
    
    allloc = []
    allper = []
    allorg = []
    allmisc = []
    with open(loc, encoding='utf-8') as istr:
        ss =istr.readlines()
        for word in ss:
            word = word.replace('\n','')
            word = word.replace('\t','')
            word = word.replace('\u200d','')
            word = word.replace('\u200c','')
            word = word.replace('\ufeff','')
            allloc.append(word)
        #print(allloc)
    
    with open(per, encoding='utf-8') as istr:
        ss =istr.readlines()
        for word in ss:
            word = word.replace('\n','')
            word = word.replace('\t','')
            word = word.replace('\u200d','')
            word = word.replace('\u200c','')
            word = word.replace('\ufeff','')
            allper.append(word)
        #print(allper)
        
    with open(org, encoding='utf-8') as istr:
        ss =istr.readlines()
        for word in ss:
            word = word.replace('\n','')
            word = word.replace('\t','')
            word = word.replace('\u200d','')
            word = word.replace('\u200c','')
            word = word.replace('\ufeff','')
            allorg.append(word)
        #print(allorg)
        
    with open(misc, encoding='utf-8') as istr:
        ss =istr.readlines()
        for word in ss:
            word = word.replace('\n','')
            word = word.replace('\t','')
            word = word.replace('\u200d','')
            word = word.replace('\u200c','')
            word = word.replace('\ufeff','')
            allmisc.append(word)
        #print(allmisc)
    
    
    
    return allper,allloc,allorg,allmisc
        #ss.replace('\ufeff','\n')
        #line=re.split(' ',ss)
        #print(line)


def readfile(filename):
    import xlrd
    wb = xlrd.open_workbook(filename) 
    sheet = wb.sheet_by_index(0) 
    '''
    read file
    return format :
    [ ['EU', 'B-ORG'], ['rejects', 'O'], ['German', 'B-MISC'], ['call', 'O'], ['to', 'O'], ['boycott', 'O'], ['British', 'B-MISC'], ['lamb', 'O'], ['.', 'O'] ]
    '''
    sentences = []
    sentence = []
    for i in range(sheet.nrows):
        word = sheet.cell_value(i, 1)
        label = sheet.cell_value(i,2)

        if '।' in str(word):
            if len(sentence) >0:
                sentences.append(sentence)
                #print(sentence)
                #print('stop word'+ str(word)+" "+ str(label))
                sentence=[]
        else:
            sentence.append([word,label])
            #print(sentence)
        #print(sentence)
        
        #sentence.append(str(word)+" "+str(label))
    
    #print(sentences)
    return sentences

def readcol(addrsrc,col):
    import xlrd
    wb = xlrd.open_workbook(addrsrc) 
    sheet = wb.sheet_by_index(0) 
    colm = []
    for i in range(sheet.nrows):
        word = sheet.cell_value(i, col)
        colm.append(word)
    return colm

# In[14]:


# SAMPLE CALL
#addrsrc ="/Users/prakash/Google Drive/live/Study/WRC/MSCK IV Sem/Thesis/Named Entity Recognition/Dataset/Tagged Work/conversion/data.xlsx"
#readfile(addrsrc)




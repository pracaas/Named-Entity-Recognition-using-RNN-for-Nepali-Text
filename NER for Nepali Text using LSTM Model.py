from keras.models import InputLayer
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Activation
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers.normalization import BatchNormalization
from time import time
import os
import keras
import xlrd
import random
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split


def readfilen(filename, frm, to):
    wb = xlrd.open_workbook(filename)
    sentences = []
    sentence = []
    # this part is  for checking
    osent = []
    osents = []
    sent = []
    sents = []
    # this part is for checking end items
    endwo = []
    sencount = 0
    mysheet = []
    endwos = []

    for j in range(frm, to):
        sheet = wb.sheet_by_index(j)

        mysheet.append(sencount)
        for i in range(sheet.nrows):

            word = sheet.cell_value(i, 1)

            word = str(word)

            label = sheet.cell_value(i, 2)

            # if word in stpwords:
            #    word=""
            word = word.replace('"', '')
            word = word.replace('\n', '')
            word = word.replace('’', '')
            word = word.replace(',', '')
            word = word.replace('\t', '')
            word = word.replace("'", '')
            word = word.replace("‘", '')
            word = word.replace(":", '')
            word = word.replace("¥", '')
            word = word.replace("…", '')
            word = word.replace("\u200d", '')
            word = word.replace(":", '')
            word = word.replace("(", '')
            word = word.replace(")", '')
            word = word.replace("\ufeff", '')
            word = word.replace("-", '')
            word = word.replace("?", '।')

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
                sencount = sencount + 1
                if '\n' in word:
                    word = word.replace('\n', '')
                word = str(word)
                osent.append(word)
                osents.append(osent)

                osent = []
                if word == '।' or word == '|' and len(word) == 1:
                    # print(word)
                    endwo.append(word)
                    # print(word)
                    sent.append(str(word) + "-End only ।")
                    sentences.append(sentence)
                    sents.append(sent)
                    sent = []
                    sentence = []

                elif word[0] == '।' or word[0] == '|':
                    ab = str(len(word))

                    # print(word+"-"+ab+"--under 1st--End")

                    endwo.append(word[0])

                    sentences.append(sentence)
                    sentence = []

                    sent.append(word[0] + "-।End")
                    sents.append(sent)
                    sent = []

                    sent.append(word[1:])
                    sentence.append([word[1:], label])
                    '''
                    if word[1:] in stpwords:
                        word=""
                        
                    else:
                        sent.append(word[1:])
                        sentence.append([word[1:],label])
                    '''

                elif word[-1] == '।' or word[-1] == '|':

                    ab = str(len(word))
                    # print(word+"-"+ab+"--under last--End")

                    endwo.append(word[-1])

                    # sentence.append([word[:-1],label])
                    endwos.append(word[:-1])

                    # sentences.append(sentence)
                    # sentence=[]

                    sent.append(word[:-1])
                    sent.append(word[-1] + "-End।")
                    sents.append(sent)
                    sent = []
                    label = "O"
                    sentence.append([word[:-1], label])
                    sentences.append(sentence)
                    sentence = []
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
                    # print(word+"-"+ab+"--under last--End")
                    if '।' in word:
                        var = '।'
                    elif '|' in word:
                        var = '|'
                    splt = word.split(var)
                    if len(splt) < 3:

                        # sentence.append([splt[0],"O"])
                        # sentences.append(sentence)
                        # sentence=[]

                        endwo.append('।')

                        sent.append(splt[0] + "-En।d")
                        sents.append(sent)
                        sent = []
                        sent.append(splt[1])

                        endwos.append(splt[0])

                        sentence.append([splt[0], "O"])
                        sentences.append(sentence)
                        sentence = []

                        sentence.append([splt[1], label])

                        '''
                        if splt[1] in stpwords:
                            word=""
                        else:
                            sentence.append([splt[1],label])
                        '''

                    else:
                        print("Multiple '।' in a word " + word + " Length " + str(splt))


            elif str(word) == "" and label != "":
                # print(str(label)+" Empty word with label found")
                a = 0

                # print(str(j+1)+"Sheet and Row - "+str(i+1)+" Both word and label is blank")
            # if label == "":

            elif str(label) == "":
                if word == "":
                    a = 0
                else:
                    label = "O"
                    osent.append(str(word))
                    word = str(word).rstrip('\n')
                    sentence.append([word, label])
                    sent.append(str(word))
                    # print(str(j)+" "+str(i)+" Empty label of word"+word)

            else:

                osent.append(str(word))
                word = str(word).rstrip('\n')
                sentence.append([word, label])
                sent.append(str(word))
            if label == "" and word != "":
                a = 0
                # print(str(j)+" "+str(i)+word+" this word label is empty -"+label)

                # print(word+label+"ok")
    return sentences
    # return sentences,sents,osents,mysheet
    # mysheet,sents,osents


def preprocess(listdata):
    print("not")

class RNN_Model:
    def __init__(self):
        self.LEARNING_RATE = 0.002
        self.EPOCHS = 2
        self.DROPOUT_RECURRENT = 0.1
        self.EMBEDDING = 102
        self.LSTM_Units = 15
        self.LEARNING_RATE = 0.002
        self.BATCH_SIZE = 10
        self.opti = Adam(self.LEARNING_RATE)
        self.Dense_layer1 = 76
        self.DROPOUT1 = 0.5
        self.test_size = 0.1
        self.MAX_LEN = 0
        self.NSentences = []
        self.all_sentences_only = []
        self.all_sentences_tag_only = []
        self.word2idx = {}
        self.idx2word = {}
        self.tag2idx = {}
        self.idx2tag = {}
        self.length_distinct_tags = 0
        self.length_distinct_words = 0


    def get_parsed_senteces_tags(self,new=None):
        sentence = []
        sentencesonly = []
        sentencetag = []
        sentencestagonly = []
        if new == None:
            NSentencesv = self.NSentences
        else:
            NSentencesv = new

        for Nsentence in NSentencesv:
            for word in Nsentence:
                sentence.append(word[0])
                sentencetag.append(word[1])
            sentencesonly.append(sentence)
            sentencestagonly.append(sentencetag)
            sentence = []
            sentencetag = []
        return sentencesonly,sentencestagonly

    def build_bag(self):
        distinct_bag_words, distinct_bag_tags = find_bagword_bagtags(self.NSentences)

        distinct_bag_words.insert(0, "PAD")
        distinct_bag_words.insert(1, "UNK")

        self.word2idx = {w: i for i, w in enumerate(distinct_bag_words)}

        # Vocabulary Key:token_index -> Value:word
        self.idx2word = {i: w for w, i in self.word2idx.items()}

        # Vocabulary Key:Label/Tag -> Value:tag_index
        # The first entry is reserved for PAD
        distinct_bag_tags.insert(0, "PAD")
        self.length_distinct_tags = len(distinct_bag_tags)
        self.tag2idx = {t: i for i, t in enumerate(distinct_bag_tags)}

        # Vocabulary Key:tag_index -> Value:Label/Tag
        self.idx2tag = {i: w for w, i in self.tag2idx.items()}

        # For checking the index of a word in dataset
        print("The word सरकारलाई is identified by the index: {}".format(self.word2idx["सरकारलाई"]))
        print("The word सरकारलाई is identified by the index: {}".format(self.idx2word[19795]))
        print("The labels B-PER(which defines Person Name) is identified by the index: {}".format(self.tag2idx["B-PER"]))
        self.length_distinct_tags = len(distinct_bag_tags)
        self.length_distinct_words = len(distinct_bag_words)


    def preprocess_input_data(self,sentences):
        X = [[float(self.word2idx[w]) for w in s] for s in sentences]
        X = pad_sequences(maxlen=self.MAX_LEN, sequences=X, padding="post", value=self.word2idx["PAD"])
        return np.array(X)

    def preprocess_output_data(self,tags):
        # Convert Tag/Label to tag_index
        y = [[self.tag2idx[w] for w in s] for s in tags]
        # Padding each sentence to have the same length
        y = pad_sequences(maxlen=self.MAX_LEN, sequences=y, padding="post", value=self.tag2idx["PAD"])
        # One-Hot encoding
        y = [to_categorical(i, num_classes=self.length_distinct_tags) for i in y]
        return np.array(y)

    def main(self):
        time_callback = TimeHistory()
        addrsrc = "Dataset/Nepali Text Named Entity Dataset.xlsx"

        # After Preprocessing all dataset with Tagged Entity are stored into Sentences variable.
        self.NSentences = readfilen(addrsrc, 0, 1)

        self.MAX_LEN = max([len(sen) for sen in self.NSentences])
        self.NSentences = limitSentence(self.NSentences)
        self.all_sentences_only,self.all_sentences_tag_only = self.get_parsed_senteces_tags()
        self.build_bag()
        X = self.preprocess_input_data(self.all_sentences_only)
        y = self.preprocess_output_data(self.all_sentences_tag_only)


        # Opposite of One Hot Encoding.
        def revrcatgry(y):  # It takes 3D matrix
            y = list(y)
            z = [np.argmax(i, -1) for i in y]
            return np.array(z)

        # Splitting Data into Train and Test Data
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=self.test_size)

        # Model 1 definition

        model = Sequential()
        model.add(InputLayer(input_shape=(self.MAX_LEN,)))
        model.add(Embedding(input_dim=self.length_distinct_words, output_dim=self.EMBEDDING,
                            input_length=self.MAX_LEN, mask_zero=True))

        model.add(LSTM(units=self.LSTM_Units, return_sequences=True, recurrent_dropout=self.DROPOUT_RECURRENT, activation='relu'))
        model.add(BatchNormalization())

        model.add(Dense(self.Dense_layer1, activation="relu"))
        model.add(BatchNormalization())
        model.add(Dropout(self.DROPOUT1))

        model.add(TimeDistributed(Dense(self.length_distinct_tags)))
        model.add(Activation('softmax'))

        model.compile(optimizer=self.opti, loss='categorical_crossentropy', metrics=['accuracy'])

        ## Print The Summary of the Model
        print(model.summary())

        history = model.fit(X_tr, y_tr, batch_size=self.BATCH_SIZE, epochs=self.EPOCHS, validation_data=(X_te, y_te),
                            verbose=1, callbacks=[time_callback])
        for i in range(0,20):
            self.test(self.NSentences,self.MAX_LEN,self.word2idx,model,self.idx2tag)

    def test(self,NSentences,MAX_LEN,word2idx,model,idx2tag):
        test_sentence,test_tag = getsentence(NSentences, random.randrange(0, len(NSentences), 1), False)
        print(test_sentence)
        test_data = self.preprocess_input_data([test_sentence])
        p = model.predict(test_data)
        p = np.argmax(p, axis=-1)
        # Visualization
        print("{:15}||{}".format("Word", "Prediction"))
        print(30 * "=")
        for w,t, pred in zip(test_sentence,test_tag, p[0]):
            print("{:15}: {:5}".format(w+" "+t, idx2tag[pred]))

def limitSentence(NSentences):
    dl = []
    for i in range(0, len(NSentences)):
        if len(NSentences[i]) < 5:
            dl.append(i)
        elif len(NSentences[i]) > 51:
            dl.append(i)

    for index in sorted(dl, reverse=True):
        del NSentences[index]

    print("Random Dataset sample 1 :\n")
    print(random.choice(NSentences))
    print(getsentence(NSentences, random.randrange(0, len(NSentences), 1)))
    print("\nRandom Dataset sample 2 :\n")
    print(random.choice(NSentences))

    return NSentences


def find_bagword_bagtags(NSentences):
    allWords = []
    allTags = []

    for i in NSentences:
        for wod in i:
            allWords.append(wod[0])
            allTags.append(wod[1])

    alldTags = list(set(allTags))
    alldWords = list(set(allWords))
    return alldWords, alldTags


class TimeHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.times = []

    def on_epoch_begin(self, batch, logs={}):
        self.epoch_time_start = time()

    def on_epoch_end(self, batch, logs={}):
        self.times.append(time() - self.epoch_time_start)


def getsentence(NSentences, num, original=False):
    sentence = []
    NSentence = NSentences[num]
    tag = []
    if original:
        sentence = NSentence
        return sentence
    else:
        for word in NSentence:
            sentence.append(word[0])
            tag.append(word[1])
        return sentence,tag



if __name__ == "__main__":
    print(RNN_Model().main())

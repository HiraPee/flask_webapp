#coding: utf-8
from matplotlib import pyplot as plt
import wordcloud
import MeCab
import os

def create_wordcloud_ja(pk,text):
    current_dir = os.getcwd()
    pk = 0
    #analyzer = oseti.Analyzer()
    #fontpath = '~/../usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
    fontpath = './SourceHanSerifK-Light.otf'
    #fontpath = './Yasashisa.ttf'
    stop_words_ja = ['もの', 'こと', 'とき', 'そう', 'たち', 'これ', 'よう', 'これら', 'それ', 'すべて', 'さん','の', 'さ','い']

    #形態素解析
    tagger = MeCab.Tagger()
    tagger.parse('')
    node = tagger.parseToNode(text)


    word_list = []
    while node:
        word_type = node.feature.split(',')[0]
        word_surf = node.surface.split(',')[0]
        if word_type == '名詞' and word_surf not in stop_words_ja:
            word_list.append(node.surface)
        node = node.next

    word_chain = ' '.join(word_list)
    #pdb.set_trace()

    wc = wordcloud.WordCloud(font_path=fontpath,
                          width=500,
                          height=300,
                          stopwords=set(stop_words_ja)).generate(word_chain)


    wc.to_file("images/" + str(pk)+ ".png")
    print('generate :'+ str(pk)+ ".png")

    #return word_cloud_image
    #return wc


def proccess_word_rstrip(text):
  text = text.replace('\n',' ')
  text = text.replace('\r',' ')
  return text

# テキスト読み込み
#with open('ja.txt', 'r', encoding='utf-8') as fi:
#   text = fi.read()

#create_wordcloud_ja(text)



def create_spa_wordcloud_ja(text):
    current_dir = os.getcwd()
    #fontpath = '~/../usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
    fontpath = './SourceHanSerifK-Light.otf'
    #fontpath = './Yasashisa.ttf'
    stop_words_ja = ['もの', 'こと', 'とき', 'そう', 'たち', 'これ', 'よう', 'これら', 'それ', 'すべて', 'さん', 'の', 'さ','い']

    #形態素解析
    tagger = MeCab.Tagger()
    tagger.parse('')
    node = tagger.parseToNode(text)

    word_list = []
    while node:
        word_type = node.feature.split(',')[0]
        word_surf = node.surface.split(',')[0]
        if word_type == '名詞' and word_surf not in stop_words_ja:
            word_list.append(node.surface)
        node = node.next

    word_chain = ' '.join(word_list)
    #pdb.set_trace()
    wc = wordcloud.WordCloud(font_path=fontpath,
                          width=500,
                          height=300,
                          stopwords=set(stop_words_ja)).generate(word_chain)

    wc.to_file("./templates/spa.png")  # 画像保存
    print('generate :'+ "spa"+ ".png")

    img_path = "/templates/spa.png" #保存先のパス
    return img_path

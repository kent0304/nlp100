# 41. 係り受け解析結果の読み込み（文節・係り受け）
'''
0に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）
のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）
をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

import CaboCha
import re



class Morph:
    '''
    形態素クラス
    表層形（surface）、基本形（base）、品詞（pos）、品詞細分類1（pos1）を
    メンバー変数に持つ
    '''
    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        return 'surface[{}] base[{}] pos[{}] pos1[{}]'.format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    '''
    文節クラス
    形態素（Morphオブジェクト）のリスト（morphs）、係り先文節インデックス番号（dst）、
    係り元文節インデックス番号のリスト（srcs）をメンバー変数に持つ
    '''

    def __init__(self):
        '''初期化'''
        # 形態素のリスト
        self.morphs = []
        # 係り元文節のインデックス
        self.srcs = []
        # 係り先節文節のインデックス
        self.dst = -1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{} srcs{} dst[{}]'.format(surface, self.srcs, self.dst)


def neco_lines():
    '''「吾輩は猫である」の係り受け解析結果のジェネレータ
    「吾輩は猫である」の係り受け解析結果を順次読み込んで、
    1文ずつChunkクラスのリストを返す

    戻り値：
    1文のChunkクラスのリスト
    '''
    with open("neko.txt.cabocha") as file_parsed:

        chunks = dict()     # idxをkeyにChunkを格納
        idx = -1

        for line in file_parsed:

            # 1文の終了判定
            if line == 'EOS\n':

                # Chunkのリストを返す
                if len(chunks) > 0:

                    # chunksをkeyでソートし、valueのみ取り出し
                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
                    yield list(zip(*sorted_tuple))[1]
                    chunks.clear()

                else:
                    yield []

            # 先頭が*の行は係り受け解析結果なので、Chunkを作成
            elif line[0] == '*':

                # Chunkのインデックス番号と係り先のインデックス番号取得
                cols = line.split(' ')
                idx = int(cols[1])
                dst = int(re.search(r'(.*?)D', cols[2]).group(1))

                # Chunkを生成（なければ）し、係り先のインデックス番号セット
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                # 係り先のChunkを生成（なければ）し、係り元インデックス番号追加
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            # それ以外の行は形態素解析結果なので、Morphを作りChunkに追加
            else:

                # 表層形はtab区切り、それ以外は','区切りでバラす
                cols = line.split('\t')
                res_cols = cols[1].split(',')

                # Morph作成、リストに追加
                chunks[idx].morphs.append(
                    Morph(
                        cols[0],        # surface
                        res_cols[6],    # base
                        res_cols[0],    # pos
                        res_cols[1]     # pos1
                    )
                )

        raise StopIteration


# 1文ずつリスト作成
for i, chunks in enumerate(neco_lines(), 1):

    # 8文目を表示
    if i == 8:
        for j, chunk in enumerate(chunks):
            print('[{}]{}'.format(j, chunk))
        break

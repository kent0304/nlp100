import CaboCha


def parse_neko():
    '''「吾輩は猫である」を係り受け解析
    「吾輩は猫である」(neko.txt)を係り受け解析してneko.txt.cabochaに保存する
    '''
    with open('neko.txt') as data_file, open('neko.txt.cabocha', mode='w') as out_file:

        cabocha = CaboCha.Parser()
        for line in data_file:
            # プログラム的にわかりやすいフォーマット
            out_file.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))
            # 視覚的にわかりやすいフォーマット
            # out_file.write(cabocha.parseToString(line))


# 係り受け解析
parse_neko()

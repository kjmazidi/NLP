# Sentence class

import config

class Sentence:
    def __init__(self, sentence_lines):
        self.text = ''              # Mike is my brother and he lives in Texas.
        self.text_list = []         # ['Mike', 'is', ...]
        self.pos = []               # ['NNP', 'VBZ', ...]
        self.chunk = []             # ['S-NP', 'S-VP', ...]
        self.ner = []               # ['S-PER', 'O', ...]
        self.pred_idx = []          # [1, 6]
        self.srls = {}              # {1: {'A1': [[0, 0], [2, 3]]}   6: {'A0': [5, 5], 'LOC': [7, 8]}
        self.tree = []              # ['(S1(S(S(NP*)', '(VP*', ...]
        self.num_tokens = 0

        first_line = True
        srl_cols = []
        for i, line in enumerate(sentence_lines):
            col = line.split()
            (txt, pos, chnk, ner, pred) = (col[0], col[1], col[2], col[3], col[4])
            if first_line and ner == "O":
                txt = txt.lower()
            self.text_list.append(txt)
            self.pos.append(pos)
            self.chunk.append(chnk)
            self.ner.append(ner)
            t = col[-1]
            self.tree.append(t)
            srl_cols.append(col[5:-1])
            if pred != "-":
                self.pred_idx.append(i)

        self.num_tokens = i
        self.text = ' '.join(self.text_list)

        # get srls for each pred
        # storing indices so text, pos, can be retrieved
        # Mike is my brother and he lives in Texas.
        #  is -->  {1: {'A1': [[0, 0], [2, 3]]}
        # lives ->  6: {'A0': [5, 5], 'LOC': [7, 8]}
        for i, idx in enumerate(self.pred_idx):
            for p in range(len(self.pred_idx)):
                srls = {}
                row = 0
                while row < self.num_tokens:
                    label = srl_cols[row][p]
                    if label.startswith('S-V'):
                        pass
                    elif label.startswith('S-'):
                        if label.startswith('S-AM'):
                            label = label[5:]
                        else:
                            label = label[2:]
                        if label in srls:
                            srls[label].append([row, row])
                        else:
                            srls[label] = [[row, row]]
                    elif label.startswith('B-'):
                        if label.startswith('B-AM'):
                            label = label[5:]
                        else:
                            label = label[2:]
                        start_i = row
                        row += 1
                        complete_BIE = False
                        while row < self.num_tokens:
                            if srl_cols[row][p].startswith('E'):
                                if label in srls:
                                    srls[label].append([start_i, row])
                                else:
                                    srls[label] = [[start_i, row]]
                                complete_BIE = True
                                break
                            row += 1
                        if config.debug and not complete_BIE:
                            print('Possible problem in B-I-E parse', row, p, self.text_list[0])

                    row += 1
                self.srls[self.pred_idx[p]] = srls





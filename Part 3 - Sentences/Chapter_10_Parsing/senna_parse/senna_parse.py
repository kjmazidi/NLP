#!/usr/bin/env python3
__author__ = "Karen Mazidi"

"""senna_parse.py

This script:
  - reads a text file
  - segments text into sentences
  - runs the sentences through the senna parser
  - parses the output

Before running, modify config.py for your system

  run like this: $python3 senna_parse.py

"""
import config
import subprocess
from textblob import TextBlob
from Classes import Sentence

if __name__ == "__main__":
    # read input text
    with open(config.infile) as f:
        raw_text = f.read()

    # segment input text into sentences
    # save it to a file so we can manually inspect segmentation
    blob = TextBlob(raw_text)
    sentences = blob.sentences
    f_sent = 'sentences.txt'
    with open(f_sent,'w') as f:
        for sentence in sentences:
            f.write(sentence.raw + '\n')

    # run senna on sentences
    infile = open(f_sent)
    outfile = open(config.outfile, 'w')

    # use the following for mac or linux
    p = subprocess.Popen([config.senna] + ['-posvbs'], stdin=infile, stdout=outfile, cwd=config.senna_dir)
    # use the following for windows, it needs the shell=True
    #p = subprocess.Popen([config.senna] + ['-posvbs'], stdin=infile, stdout=outfile, cwd=config.senna_dir, shell=True)
    p.wait()
    outfile.flush()

    # read in senna file
    with open(config.outfile) as f:
        in_lines = list(f.read().splitlines())

    # gather sentences and create Sentence objects
    sentences = []      # list of Sentence objects
    sentence_lines = []
    for line in in_lines:
        if not line:     # empty line
            s = Sentence(sentence_lines)
            sentences.append(s)
            sentence_lines = []
        else:
            sentence_lines.append(line)

    # access select elements of each sentence
    for s in sentences:
        print(s.text)
        pos = ' '.join(s.pos)
        print(pos)
        for d in s.srls:
            print(d, s.srls[d])
        print()


import ast
import json

import pandas as pd

def bionic_my_text(story_bolded, round_up=False):
    words = story_bolded.split()
    bolded_words = []

    for word in words:
        half_length = len(word) // 2
        if half_length == 0:
            continue
        bolded_word = f"<b>{word[:half_length]}</b>{word[half_length:]}"
        bolded_words.append(bolded_word)

    bolded_text = ' '.join(bolded_words)
    return bolded_text
    #print(bolded_text)


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)

    my_csv = pd.read_table('output.tsv')

    my_csv['para_bold'] = my_csv['para']
    my_csv['para_bold'] = my_csv['para_bold'].apply(bionic_my_text)
    """
    newdoc = pd.DataFrame(columns=['item_id', 'para', 'para_bold', 'question', 'opt1', 'opt2', 'opt3', 'opt4', 'correct_answer'])
    newdoc['item_id'] = my_csv.index
    newdoc['para'] = my_csv['story']
    newdoc['para_bold'] = my_csv['story_bolded']
    newdoc['question'] = my_csv['question']

    print(newdoc['item_id'])
    print(my_csv['answer_options'].iloc[2])
    print(type(ast.literal_eval(my_csv['answer_options'].iloc[2])))
    """
    my_csv.to_csv('output_with_bolds.csv')
   # bionic_my_text(inpt)

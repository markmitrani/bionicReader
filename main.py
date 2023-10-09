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


    # Replace \newline with actual newlines and \tab with actual tabs in the DataFrame
    # subtask: replace \newline with space or empty string based on surrounding whitespace:
    # first erase newlines surrounded by whitespace. then for the remaining, directly erase.
    my_csv['para'] = my_csv['para'].str.replace(r'(\S)\\newline(\S)', r'\1\2').str.replace(r'\newline', ' ').str.replace(r'\tab', '')

    #test print(my_csv['para'][8])

    my_csv['para_bold'] = my_csv['para']
    my_csv['para_bold'] = my_csv['para_bold'].apply(bionic_my_text)
    my_csv.to_csv('output_with_bolds.csv')
   # bionic_my_text(inpt)

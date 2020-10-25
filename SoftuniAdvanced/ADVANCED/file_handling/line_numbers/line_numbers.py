result_text = ""
with open("text.txt", "r") as file1:
    for idx, line in enumerate(file1):
        letters_count = len([x for x in line if x.isalpha()])
        punc_marks_count = len([x for x in line if x in "!-?.,':;"])
        result_text += f'Line {idx}: {line[:-2]} ({letters_count}) ({punc_marks_count})\n'
        print(f'Line {idx}: {line[:-2]} ({letters_count}) ({punc_marks_count})')

with open("second_text.txt", "w") as file2:
    file2.write(result_text)
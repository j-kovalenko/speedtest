import markovify


def generator():
    text = open("potter.txt",  encoding="utf8").read()

    # Build the model.
    text_model = markovify.Text(text)

    # Print five randomly-generated sentences
    txt = ''
    for i in range(5):
        sent = text_model.make_sentence()
        if sent != None:
            if 300 >= len(txt + sent + ' ') <= 340:
                txt += sent + ' '
            else:
                break
    return txt[:-1]


# print(generator())
# # Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))
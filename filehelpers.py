def read_message_archive(filename):
    file = open(filename, "r", encoding="utf8")
    data = file.read()
    file.close()
    return data


def output_html(filename, value):
    output_file = open(filename, "w", encoding="utf8")
    output_file.write(value)
    output_file.close()

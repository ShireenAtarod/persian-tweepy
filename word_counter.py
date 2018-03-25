import os
import os.path

from analysis import countTextWords

if __name__ == '__main__':
    output = ''
    with open('shila-test.txt', 'r') as text_file:
        content = text_file.read()
        comments = content.split('\n\n')

        for comment in comments:
            if len(comment) > 0:
                output += comment + '\n'
                output += 'Words: ' + str(countTextWords(comment)) + '\n'
                output += '\n'

        with open('shila-test-output.txt', 'w') as output_file:
            output_file.write(output)
            output_file.close()

        text_file.close()

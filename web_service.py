from flask import Flask, jsonify

app = Flask(__name__)


dictionary_of_anagrams1 = ['foobar', 'aabb', 'baba', 'boofar', 'test']
#dictionary_of_anagrams = '''foobar, aabb, baba, boofar, test'''
#keywords = list(map(str.lower, dictionary_of_anagrams.split()))


@app.route('/load', methods=['GET'])
def get_dictionary_of_an():
    return jsonify({'dictionary_of_anagrams': dictionary_of_anagrams1})


'''def sorted_string(s):
    return ''.join(sorted(s))'''
'''@app.route('/show', methods=['GET'])
def serach_anagram():
    anagram = {}
    for word in keywords:
        sorted_word = sorted_string(word)
        anagram.setdefault(sorted_word, [])
        anagram[sorted_word].append(word)
    return jsonify(anagram)'''


@app.route('/foobar', methods=['GET'])
def show_foobar():
    anagram_of_foobar = {}
    word = sorted('raboof')
    for i in dictionary_of_anagrams1:
        if word == sorted(i):
            anagram_of_foobar.setdefault(i)
    return jsonify(anagram_of_foobar)


@app.route('/raboof', methods=['GET'])
def show_raboof():
    anagram_of_raboof = {}
    word = sorted('raboof')
    for i in dictionary_of_anagrams1:
        if word == sorted(i):
            anagram_of_raboof.setdefault(i)
    return jsonify(anagram_of_raboof)


@app.route('/abba', methods=['GET'])
def show_abba():
    anagram_of_abba = {}
    word = sorted('abba')
    for i in dictionary_of_anagrams1:
        if word == sorted(i):
            anagram_of_abba.setdefault(i)
    return jsonify(anagram_of_abba)


@app.route('/test', methods=['GET'])
def show_test():
    anagram_of_test = {}
    word = sorted('test')
    for i in dictionary_of_anagrams1:
        if word == sorted(i):
            anagram_of_test.setdefault(i)
    return jsonify(anagram_of_test)


@app.route('/qwerty', methods=['GET'])
def show_qwerty():
    anagram_of_qwerty = {}
    word = sorted('qwerty')
    for i in dictionary_of_anagrams1:
        if word == sorted(i):
            anagram_of_qwerty.setdefault(i)
            return jsonify(anagram_of_qwerty)
        else:
            return jsonify("Null")


if __name__ == '__main__':
    app.run(debug=False)

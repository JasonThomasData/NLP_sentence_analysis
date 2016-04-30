#!/usr/bin/env python

import os, requests, re
import unicodecsv as csv
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
from bs4 import BeautifulSoup

java_path = "usr/bin/java"
os.environ['JAVAHOME'] = java_path
current_dir = os.path.dirname(__file__)

stanford_parser_dir = current_dir + '/stanford_NLP/stanford-parser-full-2015-04-20'
eng_model_path = stanford_parser_dir + "/edu/stanford/nlp/models/lexparser/englishRNN.ser.gz"
my_path_to_models_jar = stanford_parser_dir + "/stanford-parser-3.5.2-models.jar"
my_path_to_jar = stanford_parser_dir + "/stanford-parser.jar"

parser = StanfordParser(model_path = eng_model_path, path_to_models_jar = my_path_to_models_jar, path_to_jar = my_path_to_jar)
dependency_parser = StanfordDependencyParser(path_to_jar = my_path_to_jar, path_to_models_jar = my_path_to_models_jar)

#Not part of the main program. Called from another function. Put this in another file
def test_single_sentence(sentence_to_test):
    result = dependency_parser.raw_parse(sentence_to_test)
    dep = result.next()
    parsed_result = list(dep.triples())
    print parsed_result

#This uses unicodecsv not standard csv module, check the imports line if there's an error
def save_csv_file(this_text_data, database_location):
    with open(database_location , 'wb') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter = ',',encoding='utf-8')
        for n in range(0, len(this_text_data)):
            csvWriter.writerow(this_text_data[n])

def parse_sentence(sentence):
    print sentence
    #Code below detects relations (passive voice and active voice)
    result = dependency_parser.raw_parse(sentence)
    dep = result.next()
    parsed_result = list(dep.triples())
    print parsed_result
    passive_clause = False
    active_clause = False
    #These two were meant to detect passive and active clauses, but were unreliable
    #if "u'nsubj'" in str(parsed_result):
    #    active_clause = True
    #if "u'nsubjpass'" in str(parsed_result):
    #    passive_clause = True

    #So far, the auxpass has been the only one that detected passive voice reliably 
    if "u'auxpass'" in str(parsed_result):
        passive_clause = True
    number_of_passive = str(parsed_result).count("u'auxpass'")
    #Other statisics
    of_the = False
    if 'of the' in sentence:
        of_the = True
    words_in_sentence = word_tokenize(sentence)
    sentence_length_in_characters = len(sentence) #this includes spaces
    sentence_length_in_words = len(words_in_sentence)
    longest_word = max(words_in_sentence, key=len)
    longest_word_length = len(longest_word)
    punctuation = re.sub('[\s0-9a-zA-Z]', '', sentence)
    punctuation_length = len(punctuation)
    return [sentence,active_clause,passive_clause,number_of_passive,of_the,sentence_length_in_characters,sentence_length_in_words,longest_word,longest_word_length, punctuation, punctuation_length]

def extract_sentences(page_content):
    this_text_data = []
    #ensure this corresponds to the data you're constructing in the parse_sentence function
    this_text_data.append(['sentence','active_clause','passive_clause','number_of_passive','of_the','sentence_length_in_characters','sentence_length_in_words','longest_word','longest_word_length', 'punctuation', 'punctuation_length'])
    sentences_to_parse = sent_tokenize(page_content)
    for sentence in sentences_to_parse:
        new_data_row = parse_sentence(sentence)
        this_text_data.append(new_data_row)
    return this_text_data

def get_soup_from_request(page_request):
    soup = BeautifulSoup(page_request, "html.parser")
    language_area = soup.find('div', {'class': 't_txt'})
    text_without_html = language_area.text
    return text_without_html
    
def get_text_from_site(url):
    r = requests.get(url)
    page_content = r.content
    #print page_content
    return get_soup_from_request(page_content)

def get_text_from_dir(location):
    with open(location, 'r') as local_file:
        file_content = local_file.read()
        return file_content

def run_prog(dictionary_array):
    for dictionary in dictionary_array:
        print 'Processing %s from %s' %(dictionary['type'], dictionary['location']) 
        if dictionary['type'] == 'test':
            text = get_text_from_dir(dictionary['location'])
        else:
            text = get_text_from_site(dictionary['location'])
        sentences_data = extract_sentences(text)
        save_csv_file(sentences_data, dictionary['database'])
###Analysing passive voice, wordiness and other elements of written style

This project uses the Stanford NLP parsing libraries to detect writing style. Specifically, I want to find out if sentences use passive or active voice. 

The Stanford NLP Core Java files can find passive and active voice well enough for comparisons over many, many works

###Analysing sentence structures in the work of George Orwell

I've always been fascinated by George Orwell. I'm also interested in writing (journalism has been my trade for five years now).

Orwell wrote an essay towards the end of his career called 'Politics and the English Language'. In this essay, Orwell sets down six principles that should be followed more often than not. One of those is:

```Never use the passive where you can use the active.```

So I wondered if this principle, and others outlined in the essay, were present in his earlier writings, or if this was a principle Orwell embraced in his later life.

George Orwell also said to use passive voice if it was the obvious thing to do, so I'm not making judgements about his writing style. I'm interested to see if his style developed in his career.

###Installation

I'll leave it to you to use a virtualenv. All necessary Python files can be installed as:

```pip install -r requirements.txt```

The Stanford NLP libraries are way too large for me to upload them to this repo. On my machine, they live in a directory called stanford_NLP - check the stanford_NLTK.py file to see how it was set up.

If you're like me and you don't use Java, getting Python to talk with Java is a challenge.

I recommend this reading material for setting up Java and getting it talking with NLTK (Python language project)

If you read nothing else... 
 - http://stackoverflow.com/questions/13883277/stanford-parser-and-nltk/34112695?noredirect=1#comment58609373_34112695

If you need to set the Java location in virtualenv
 - http://stackoverflow.com/questions/27171298/nltk-stanford-pos-tagger-error-java-command-failed

Exit codes in Java
 - http://stackoverflow.com/questions/14041467/why-do-we-have-exit-codes-in-java

Need version 8 of java to use the latest parsers
 - http://stackoverflow.com/questions/27216038/stanford-tagger-not-working 

###Notes on this project

This project contains a ```run_prog()``` function, which takes a list of dictionaries as an argument. Each dictionary will have details about the text to be scraped using ```requests``` and then parsed into an HTML tree with ```BeautifulSoup```. The scraping with my George Orwell website is very mininal. The project sends a request, and finds the element containing plain text.

The project goes through and finds these characteristics:

	number_of_passive #Integer - number of passive clauses in this sentence
	of_the	#Boolean - using 'of the' is never necessary in any text
	sentence_length_in_characters #Integer 
	sentence_length_in_words #Integer
	longest_word #String - returns the word, not sure if this will be interesting
	longest_word_length #Integer
	punctuation #String - A sentence's punction, with all characters and whitespace removed
	punctuation_length #Integer

These results are inconsistent and need further testing:

	active_clause #Boolean - does this sentence contain an active clause?
	passive_clause #Boolean - does this sentence contain an passive clause?

###Issues

This project splits all sentences, including those inside quotes. Quotes should not be included, since the author is hardly to blame for a character's poor use of English.

Currently, all results are saved to a separate csv file. I will then have to get summarised results for all, which is annoying. Fix that so the program saves summarised results in a single file.



#Process all novels in this dictionary
#run_prog(novels_scrape_dict)

#Run active voice tests
#run_prog(active_tests)

#Run passive voice tests
#run_prog(passive_tests)

#Process all articles in this dictionary
#run_prog(articles_essays_scrape_dict)

#What it says
#test_single_sentence("The man said he didn't like it.")
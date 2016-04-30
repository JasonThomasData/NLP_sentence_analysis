# Single Source Story Index

When a news organisation reports an issue with one voice only, the reader does not have the proper chances to consider an issue from more than one side.
A journalist should not be made fun of for writing a single source story, but over the course of her/his career, it should be plain that person has used many more sources in their stories.

##The problem
Readers would like to know which news organisations are commonly publishing stories that have only a single voice.

##The solution
Crawl news websites, analysing the stories on those.
Use the process below to

### How do we define a single source story?

A story that only has one voice or source.

### How do we find these stories?

####Web crawling
We will create a web crawler that crawls Australian news websites.
It will scrape links to stories, provided the site and link has the target domain name.
These will be a pre-defined list of sites.

####NLP to find single voice
Use the Stanford Core NLP library to analyse the structure of sentences.
These sentences should be analysed by finding instances of verbs that are 'said', 'says', 'explained', etc.
These should also take the subject, and check if it's a proper noun.
If the subject (noun performing the action) is a proper0 noun and the verb matches those cases, then we know the subject is a source, so we can push that to a list of sources for this story.

At the end, we'll have a list of all sources, and most stories should have more than one.

Requirements -

unicodecsv/ sqlite3
requests
beautifulsoup

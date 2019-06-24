# Lyrics Crawler
A basic Python script that takes a song query input from the user and displays its lyrics directly taken from songmeanings.com Repo remains private until we're sure robots.txt on the parsing website allows our crawler to use their lyrics.

Currently the script is in a nascent development stage (subject to further dev co-operation), it runs the query through Google using google module in Python, gets the first URL that points to the song name, requests data from the link and displays song lyrics. 

Known issues:
1. Only English songs can be obtained from songmeanings.com 
2. It does not spell-check or verify if the song exists, it will just return the most relevant search result and proceed with displaying lyrics. 
3. It returns a blank (None) line with no feedback when no song is found. 
4. You tell me .... 

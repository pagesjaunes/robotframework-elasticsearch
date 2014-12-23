robotframework-elasticsearch
============================

ElasticSearch library for RobotFramework

# Presentation
This lib provides basic keywords to interact with elasticsearch in a RobotFramework testsuite.
It allows to query, count, create or delete an index.

# Install


```
	> pip install robotframework-elasticsearch
```

	Or clone the repo and launch this command from the root dir :

```
	> python setup.py install
```
# Example of use

```
	*** Settings ***
	Library 	ElasticSearchLib

	*** Testcases ***
	Number of docs must be equal to 85431
	    ${count}= 	es count 		localhost		9200    my_index
	    Should Be Equal    ${count}		85431
```

# Doc
Read the robot formated doc for more information about how to use the keywords : [RF Doc for ElasticsearchLib](http://htmlpreview.github.io/?https://github.com/pagesjaunes/robotframework-elasticsearch/blob/master/doc/ElasticSearchLib.html)

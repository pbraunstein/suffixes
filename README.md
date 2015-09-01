#Suffixes
##### Philip Braunstein (pbraunstein12@gmail.com)

### Overview
This script uses the database downloaded [dict.cc](http://www.dict.cc/) German English database. It pulls out all the nouns derived from a common suffix supplied by the user.

### Background
The German language is extremely composable such that new words are formed by combining already existing words. This is exemplified by noun formation. For example *Fall* means "case" in English. *Abfall* (literally *awaycase*) means "trash", and *Zwischenfall* (literally *betweencase*) means "incident."

It can be helpful for language learners to see these intrinsic patterns of the language. This script helps students construct these patterns for themselves. In optimal usage, a student might notice a lot of words ending in *Fall* and want to see all of the *Fall* words at once. This script fills this need.

### Usage
The shell script `run.sh` runs some common queries of the script. You can also query your own suffixes by running `python getBySuffix.py suffix_of_interest`

### Data
You can request to download the data [here](http://www1.dict.cc/translation_file_request.php)

### Acknowledgments
Thank you to [dict.cc](http://www.dict.cc/) for keeping making their data freely available


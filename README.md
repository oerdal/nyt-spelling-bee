# New York Times Spelling Bee Possible Solution

## Concept

The spelling bee is a new minigame on the NYT crossword app.

User is given 6 letters and a special 7th letter. User is to make as many words as possible under the following conditions:

* Words must be a minimum length: 4
* Words must all contain the special character
* Words can repeat letters

More information on the game and it's terms and rules can be found on [the NYT website.](https://www.nytimes.com/2021/07/26/crosswords/spelling-bee-forum-introduction.html)

## Tool

The tool aims to generate all possible words from a massive online dictionary downloaded from [this](https://github.com/dwyl/english-words) github repo.

They have compiled the list into an ready to use `json` format.

Currently, the tool oversuggests due to the size of the input dictionary.

### _TODO_

* Find a more representative dictionary.
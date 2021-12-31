# New York Times Spelling Bee Possible Solution Generator

## Concept

The spelling bee is a new minigame on the NYT crossword app.

User is given 6 letters and a special 7th letter. User is to make as many words as possible under the following conditions:

* Words must be a minimum length: **4**
* Words must all contain the special character
* Words can repeat letters

More information on the game and it's terms and rules can be found on [the NYT website.](https://www.nytimes.com/2021/07/26/crosswords/spelling-bee-forum-introduction.html)

## Tool

The tool aims to generate all possible words from a massive online dictionary downloaded from [this](https://github.com/dwyl/english-words) github repo.

They have compiled the list into an ready to use `json` format.

Currently, the tool oversuggests due to the size of the input dictionary.

### _TODO_

* Find a more representative dictionary.

## Usage

Enter the characters from the NYT spelling bee puzzle. **Note: the special (center) character must be entered first.**

### Example

![Sample for 'WADEHIN'](sample_nyt_sb.jpg)

This puzzle arrangement would have the 'W' as the special character (which must be used in each valid word). To enter this into the puzzle solver, the user would (when prompted) enter **any string of letters with w as the first letter**: "_whedani_", "_winadeh_", and "_WAINDHE_" are all examples of words that may be entered. The input is _not_ case-sensitive.



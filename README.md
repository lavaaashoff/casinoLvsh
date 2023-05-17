# Casino
**This is my educational project.** There may be a lot of bad code here, I'm trying to fix it.
___

You need to have Python installed on your computer to play. Also, the program uses external libraries *(In the future I will try to somehow fix this so that all of them are inside the application)*
.To install them, write in the terminal:

`pip install colorama`


If all this is installed, just run the file `main.py`
___

Here you can play casino. *(So far, there are only 3 symbols that can drop, they all have the same chance.)*

By default, the game starts with a balance of 500, but you can change this by changing the value in the file `main.py`. Just change `StartBalance`
``` python
StartBalance = 500
```

When outputting a database, write `(id bet, balance after bet, bet, symbols, win/lose)`

#### Dropped symbols and their odds
`777` -> x10

`$$$` -> x5

`###` -> x3

### Plans
 - [ ] Create bot in telegram
 - [x] Make a color bet result
 - [ ] Make different odds for symbols


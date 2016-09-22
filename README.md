# Vocabulary Pet
a vocabulary learning game that features a pet alien

## Features ##

- [x] learn words
- [x] edit words
- [x] pets gets hungry
- [x] speech bubbles indicate pet status
- [x] check status of pet
- [x] check player status
- [x] trade points for food
- [x] feed the pet

Planned features:
- [ ] add your own words
- [ ] change player name
- [ ] change pet name
- [ ] change pet looks
- [ ] pet dies of hunger
- [ ] export words to json
- [ ] user manual
- [ ] progress  bar

No-anytime-soon - Features:
- [ ] pet 'say'/shows words from word list
- [ ] more moods + items + speech bubbles
- [ ] multiple choice learning mode
- [ ] flash card learning mode
- [ ] word import from csv or json files 
- [ ] different language versions + manuals 
- [ ] pet gets level + exp
- [ ] pet grows/evolves 
- [ ] show user statistics with matplotlib


## Getting Started
These instructions will get you a copy of the project up and running on your local machine.
Download the file from git hub, unzip file if necessary.
Follow the installation instructions. 

Or if Bottle is already installed open the program’s folder with terminal/shell and run the game.py:
```
python3 game.py
```

This will start the bottle server. 
See the Fourth Step of Installing Instructions for more advice.
 

### Prerequisites
You need python3 and the bottle-framework on your machine.

### Installing
Step Zero:
Check if you have python3 by typing in the shell/terminal:
```
python3
```

You should see something like this:

```
Python 3.4.2 (default, Oct  8 2014, 13:14:40) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

If not you need to install python3.

First Step: Install Bottle
Next check if bottle is installed, by typing import bottle in the python shell/terminal.
If not, install bottle using either you favourite package manager or type pip3 install bottle in the python shell. 
For more information see the documentation about bottle at [http://bottlepy.org/docs/0.12/tutorial.html#installation]

Optional Step: The program 'pip3' is currently not installed. You can install it via apt-get or by using the paket manager:

```
sudo apt-get install python3-pip
```
Optional Step: Maybe you need to install setuptools as well:
```
pip3 install setuptools
```

Finally, install the Bottleframework with:
```
pip3 install bottle
```

Third Step:
Edit the file path in hidden_server_data.py
I do not recommend using the program anywhere but locally on you machine.
```
# Name or IP of the machine running vocabulary pet server
HOST = 'localhost' 
# Port Name of vocabulary pet server
PORT = '8080'
```

Attention, this is important. You need to change the file path to the static folder of the project.
It's there the server looks for images, with an incorrect file path the program will start, but it will look very ugly.
The path could look like this: '/home/mint/Downloads/seminar-project-marionline03-master/static' if you have extracted the zip file in the Download folder.
```
# Please fill into the brakets the root directory of vocabulary pet
# Example: STATIC_PATH = '/home/user/vocabulary_pet/static'
STATIC_PATH = '/home/mint/Downloads/seminar-project-marionline03-master/static'
```

Fourth Step:
Navigate to the folder where the program's files are.
```
cd seminar-project-marionline03-master/
```

To start run game.py, type:
```
python3 game.py
```
This will start the bottle server. Use your web browser to navigate to the location if you did not change port and host it will be "localhost:8080".
If everything worked out, you will see the pet's page in your web browser.

## Versioning
I do  not use anything for versioning yet. 
This might change in future versions. 

## Authors
* **marionline** - [HHU-test](https://github.com/HHU-test)

## License
software - not yet choosen
graphics - [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

## Acknowledgments
* Thanks to the bottle project for making bottle :)
* Thanks to Marie for the alien idea
* Thanks to everyone who contributed inspiration, knowledge and encouragement

*template inspired by [https://gist.github.com/PurpleBooth/109311bb0361f32d87a2](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)*

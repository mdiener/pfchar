# Pathfinder Character Manager

The purpose of this project is to create an interactive and dynamic Pathfinder character manager. It should be an easy to use tool for any D&D player wanting to create and maintain a Pathfinder character online. It is aggressively "mobile first" and is designed to be viewed on a phone. That said, it should also work on any other browser/operating system.

## Features
* Simple creation and storage of characters online
* Dynamic values that update:
  * Adjusting an ability will update scores and skills automatically
  * Choosing a talent with a direct bonus to attributes or other parts of your character will be automatically calculated
  * Whenever a talent or features affects some part of your character that part is highlighted and vice versa when something is affected by another part that is shown as well
  * Links to the wonderful Archives of Nethys (https://www.aonprd.com/) for all feats, classes, spells, etc.
* Keeping you in power
  * While many things happen behind the scenes you are in power, you can always adjust abilities, feats, skills, etc. to your liking
  * Everything can be undone and changed at any time, mistakes and erasing to the point of unintelligibility are a thing of the past

## Planned Features
* Extended Dataset
  * Allow unchained and other extended data to be used
* Homebrew
  * Make your own races, feats, classes, etc.
* Generator
  * have Pathfinder Character Manager create your character for you.
  * specify level, constraints, etc. and have it completely built for you!
* 2nd Edition & Starfinder
  * Currently only 1st edition is supported, but 2nd edition will be available in the future
  * Starfinder might also be coming further down the road

## How To Help
Right now this is all still in the early stages so changes are happening very fast. If you'd like to help please let me know through GitHub or email and I will get back to you!

## Building and Running it Yourself
Feel free to run it yourself and experiment with it!

### Requirements
* Python > 3.6
* Redis
* ReJSON redis module
* Node [optional]
* npm [optional]

Make sure you have a Python version greater than 3.6 installed and Redis with the ReJSON module loaded. If you want to also okay around with the JS and CSS you need NPM and Node installed as well.

### Setup
Before you run the server make sure you have all dependencies installed. It is advised you create a virtual environment beforehand. Once done you can install the dependencies with the following command:
```
cd server
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

If you also want to be able to build JavaScript and CSS you will have to setup the npm packages.
```
cd assets
npm install
```

### Run Server
You can then run the server with
```
cd server
source .env/bin/activate
python run.py
```

If you want to rebuild css and js you can do so with the following commands
```
cd assets
npm run prod
```

For testing purposes and for convenience you can use the following command to continuously monitor css and js files and rebuild on any change.
```
cd assets
npm run watch
```

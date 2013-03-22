## Welcome to repostats
repostats: a simple command-line interface to scope out git repositories and get a general view of a codebase.

### Getting started:
```
$ # All you need is git and python before you get started.
$ sudo apt-get install git
$ # Python usually comes standard...

$ git clone https://github.com/gitanalytic/repostats
$ cd repostats
```

### Load a repo into repostats to analyze
```
$ # Got a repo in mind? First load it to repostats:
$ ./repostats.py --load coolUser/awesomeRepo
```

### Then start the analysis!
```
$ # Get a general overview of its contents:
$ ./repostats.py --lang

Cascading Sheet Style file : 2 files
JavaScript Object Notation file : 10 files
HyperTextMarkup Language document : 4 files
...
Text file : 2 files

$ # Huh, how many lines is that then?
$ ./repostats.py --linecount
Number of lines in git repository: 509

$ # See the general structure of the repo:
$ ./repostats.py -ls

/repo
   EveryFileExtension.json
   favicon.png
   github.js
   homepage.css
   homepage.js
   index.html
   package.json
   README
   web.js
   /.git
      config
      description
      HEAD
      index
      packed-refs
      /branches
      /hooks
...

$ # Saw a file format you didn't recognize?
$ ./repostats.py --file script.cl
Common LISP source code file

$ # Ooohhh... old school...
```

### Finishing and cleaning up:
```
$ # Once you're done scoping out the repository,
$ * you can either clear it:
$ ./repostats.py --clear

$ # or save it to the current directory:
$ ./repostats.py --save
$ ls
README.md    log.txt    repostats.py    awesomeRepo

$ # They you're free to investigate the next
$ # cool project you stumble upon!
$ ./repostats.py --load https://github.com/ultimatecoder/awesomeproject
...
```


### Authors
Built by Paul Martinez (@PaulJuliusMartinez), Zach Saraf (@zsaraf), and Calvin Studebaker (@CalvinStudebaker).

# spider.py (Guilhem Mizrahi)

This script is a web crawler in python3.

## How it works
It takes a complete url as input and a number (the maximum requests allowed). It will then harvest all the links on the root page, go to them and harvest the links again etc ...
It is implemented in a way to not get stuck in loops and to not spread too rapidly (it will first look at all the links on the first page, then the second etc ... instead of following a link as soon as it is found)
It will also store the source code of each page in a subfolder called dump.

## How to use

First of all you need to create a dump folder
```
mkdir dump
```
Then run the script providing the complete url and the requests limit.

```
python3 spider.py http://example.com 15
```

# stephjspider.py (Stephen Jones)

This script will harvests resources on a webpage.

## How it works

Takes a URL specified by the user. Get the source code, harvest the links and images and store them in a specific file (/tmp/Web_Crawler/Image_links.txt).
To select which target file you want to use and which tags you want to harvest you can change the syntax in the code.

```
touch /tmp/Web_Crawler/Image_links.txt
```
Then run the script.
```
python3 stephjspider.py
```

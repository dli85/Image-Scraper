# Image Downloader

## Overview

This program downloads all the images from a specified (or multiple) links and combines them into a pdf. 
## Usage

Use the run.py file to start the process. You can extract images from a single link you you can provide a text file with a list of links (one link per line, no commas). 
You must specify to the program where to save the resulting PDF. 

Note: A temp folder will be created inside your designated output folder that will house the images before converting them to a pdf. This folder will be deleted 
when finished.



## Requirements

Use pip to install the required libraries

```bash
pip install beautifulsoup4 PIL
```

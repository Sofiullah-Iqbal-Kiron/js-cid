# About

A utility tool for developers similar to google's [Pycee 2.0](https://pypi.org/project/pycee2/) but for `Javascript`. <br>
Retrieves possible solutions from stackoverflow, gemini and many other resources.

- Reduces inconsistent, time consuming browsing.
- Results directly on your system terminal.
- Rich syntax highlighting for better and fast readability.
- Markdown visualization.
- Open source.
- Interestingly, **_Solution Ranking_** based on Levenshtein Similarity algorithm and most voted countup.
- Followed clean coding methodologies.
- Easy to customize.

# Installation

### Requirments

Install this softwares locally on your machine

- [Python](https://www.python.org/) 3.0 or later to run the tool
- [NodeJS](https://nodejs.org/en) runtime to extract traceback from error prone javascript file

### Steps

1. Clone this repository then change directory to the project root.
2. Create a virtual environment `python -m venv env`
3. Activate virtual environment
   - Windows: `env/Scripts/activate`
   - Unix/Linux: `source env/bin/activate` <br/>
4. Install necessary packages `pip install -r requirements.txt`

# Usage

Once the project requirements are satisfied and virtual environment is activated, open your terminal on project root and type `python main.py <file_name>` then hit enter to see the magic. <br>
Replace the javascript file path _(relative | absolute)_ with `<file_name>`.

# Video Tutorial

Or watch [this](https://youtu.be/6STIHO5lKCI) video tutorial on youtube.

# Todo

- [x] Integrate stackoverflow api
- [x] Integrate gemini api
- [x] Rich and verbose design
- [ ] Implement ranking

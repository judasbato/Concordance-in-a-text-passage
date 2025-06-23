# Concordance in a Text Passage

This repository contains a simple command-line tool for locating all lines in a text file where every word of a query occurs. It can be used to explore collocations or concordances within small text samples.

## Usage

1. Run the program with Python 3:

```bash
python main.py
```

2. When prompted, enter the path to a text file. Example text files (`einstein.txt`, `gettysburg.txt`, `pimpernel.txt`) are included in this repository.
3. After the file is processed, enter a query consisting of one or more words separated by spaces. The program prints the line numbers where all query words occur together. Type `Exit` to quit.

## Example

```
Please enter the path of the file you want to perform the collocation query on:einstein.txt
{'try': [1], 'not': [1], 'to': [1, 2], ... }
Please enter your query sentence, leaving a space between each word.
To exit the program, type 'Exit'.
a man
The lines where all the words in your query appear:
    Line : 1...
```

## Files

- `main.py` – main script implementing the concordance logic.
- `einstein.txt`, `gettysburg.txt`, `pimpernel.txt` – sample texts for testing.

## License

This project is provided without any specific license. Feel free to use and modify it as needed.


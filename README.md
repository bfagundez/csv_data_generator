# csv_data_generator

After looking around for a quick way to generate CSVs for testing and not finding any I decided to create this CLI tool.

Usage is very simple, install with:
```
$ pip install csv_data_generator
```
Run it with:
```
$ csv-data-gen 
```
By default it's going to generate a 5x5 CSV:
```
col1,col2,col3,col4,col5
1,2,3,4,5
1,2,3,4,5
1,2,3,4,5
1,2,3,4,5
1,2,3,4,5
```
It just sends the data to stdout, so you can pipe it to a file or clipboard.

You can give it a number of rows and columns:
```
$ csv-data-gen  --rows 10 --columns 150
```

You can give also make it use random words as filler instead of numbers:
```
$ csv-data-gen  --rows 10 --columns 150 --fill-words
```

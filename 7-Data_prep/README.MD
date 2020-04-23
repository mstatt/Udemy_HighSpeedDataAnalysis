This process takes one file at a time.

You can just extract all of the text reviews by running
>> python extract_all_reviews_only_text.py


For a more precise analysis do the following:
1) Clean up the uneeded columns by running.
>> python 1_amazon_review_column_extract.py

2) Split the original file into seperate files by star rating by running
>> python 2_split_reviews_by_stars.py

3) Extract all of the text reviews from the remaining files by running
>> python 3_multifile_extract_review_only.py





From the Base if you wanted to do it from scratch:
Main Page:
https://s3.amazonaws.com/amazon-reviews-pds/readme.html

Reviews by Products Page:
https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt

Our Data Set:
https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Books_v1_02.tsv.gz

Get the file:
wget https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Books_v1_02.tsv.gz

Unzip the file:
gunzip amazon_reviews_us_Books_v1_02.tsv.gz


Split the file into 100 lines files:
split -l 100 --additional-suffix=.txt amazon_reviews_us_Books_v1_02.tsv reviews_
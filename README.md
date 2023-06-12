# Text-Data-Processing

Code to split corpus text data from the Corpus of Contemporary American English. The corpus is divided into seven genres (academic, fiction, magazine, news, spoken, TV and Movies, blog, web).

Data consist of text files formatted as follows:

Academic, Fiction, Magazine, News and Spoken: 30 files each (labelled by year from 1990 to 2019)
TV and Movies: 30 files each (labelled by year from 1990 to 2019)
Blog and Web: 34 files each, all from year 2012 (labelled 01 to 34)

Each file includes X number of individual text files, each file contained within a single line. Each text file begins with a blank line. Some files have formatting errors, which resulted in extra and missing files (see result achieved for each genre).

Also included in the dataset is a source file (.txt) detailing the sources of text data. 

The codes are for:
1) Splitting each file into the individual text files
2) Name files according to convention: "text_{genre}_{year}_{ID_number}' (utf-8)

Note: Data needs to be purchased for use. The material here does not include corpus data or any of the sources file. When you have purchased the corpus data, you may copy to the empty files as indicated.

For genres: acad, fic,  mag, news,spok,tvm (tv section only)

1) For each file in genre, split file into individual files ('split_files.py')
Result achieved:
acad: 8453 files produced out of expected 25952 (-67.43% files output)
fiction: 25986 files produced out of expected 25992 (-0.02% files output)
mag: 81330 files produced out of expected 85644 (-5.04% files output)
news: 52072 files produced out of expected 88887 (-41.2% files output)
spoken: 44809 files produced out of expected 44595 (+0.47% files output)
tvm (tv section only): 15822 files produced out of expected 15823 (-0.01% files output)

For genre: blog

1) Combine text files to a single file ('combine_blog_web.py)
2) Split file into individual files ('blog.py')
Result achieved: 98762 files produced out of expected 94997 (+3.96% files output)

For genre: web
1) Combine text files to a single file ('combine_blog_web.py, change where necessary)
2) Split file into individual files ('web.py')
Result achieved: 89013 files produced out of expected 85837 (-3.70 % files output)

For genre: movies
1) Split file into individual files using line number from  ('mov.py')
Result achieved: 8152 files produced out of expected 8152 (0.00% files output)

Overall results achieved: 4424393 files produced out of expected 475879 (89.18% success rate)

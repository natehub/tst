# tile-state-imagery

Python tool chain that downloads NAIP imagery in zip file format, extracts the zip files, combines the individual files, reprojects the files, creates larger files for faster tiling, tiles the imagery based on xyz, converts png to jpg and compresses each jpg, and finaly packages everything in a mbtiles sqlite database.

## Setup Python Environment
I am using conda the script needs gdal and imagemagick. I am also using some code from mbutil(mapbox) in this tool chain.

```
conda env create -f env.yml
```

## How To Use The Script

User needs to be cd into the same directory as the get_images script.
To get instructions:
```
python get_images.cpython-36.pyc -h
```

returns:

```
usage: get_images.cpython-36.pyc [-h] [-p PROCESSORS] [-f FILENAME] [-z ZOOM]
                                 [-u DOWNLOADURL]

optional arguments:
  -h, --help            show this help message and exit
  -p PROCESSORS, --processors PROCESSORS
                        How many processors to use. You have 8
  -f FILENAME, --filename FILENAME
                        CSV of names of files to download.
  -z ZOOM, --zoom ZOOM  Zoom levels ie: 1-16.
  -u DOWNLOADURL, --downloadurl DOWNLOADURL
                        url to download from.
```

Example of usage with the supplied media.csv file (it has 10 out of the 6100 file names):

```
python ./get_images.cpython-36.pyc -f media.csv -z 1-16 -p 8 -u 'ftp://ftp.agrc.utah.gov/Imagery/NAIP2016/'
```

This script expects that the files you are downloading are .zip files and the extracted files are .tifs

## Why

I downloaded all the NAIP imagery for Utah, it was about 6100 zip files (50gb). The projected data was in mutiple utm zones and I wanted xzy tiles zoom level 1-16 using the traditional tools the output ends up being hundreds of gigs of data. After running this script my end files size was 100s % smaller. 
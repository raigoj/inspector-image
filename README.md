# Image inspector

This tool helps you explore and analyze images with advanced capabilities for detecting hidden information using steganographic methods. Additionally, it allows you to extract GPS metadata to identify the location where the image was taken. Whether you need to uncover concealed data or investigate image origins, the Image Inspector program provides essential functionalities for efficient image examination and analysis.

# What is steganography?

Steganography is a technique used to hide information, messages, or data within another seemingly innocuous file or medium in a way that conceals the existence of the hidden content. The purpose of steganography is to ensure that the hidden information remains undetected by casual observers, making it a form of security through obscurity.

## How can information be hidden in normal files?

Information can be hidden in normal files through various steganographic techniques. Some common methods include:

1. **Least Significant Bit (LSB) Steganography**: In image files, the least significant bit of each pixel's color channel is replaced with a bit of the hidden data. As the change in pixel color is minor, the human eye cannot detect it, but the hidden data can be extracted by those aware of the technique.

2. **Spread Spectrum Technique**: In audio files, the hidden data is spread across different frequency bands, again making it imperceptible to the human ear. The hidden data can be extracted by a receiver who knows how to decipher it.

3. **Text Steganography**: In text files, hidden information can be embedded using various methods, such as altering the spacing, changing font characteristics, or using invisible characters.

4. **Whitespace Steganography**: In text or HTML files, hidden data can be concealed in the whitespace (spaces, tabs, or line breaks) without affecting the visible content.

5. **File Concatenation**: Concatenating multiple files together can hide data in plain sight, especially when the carrier files are large and complex.

6. **Video Steganography**: In video files, hidden data can be stored in frames or motion vectors without causing noticeable changes in the video quality.

It's important to note that steganography is just one element of a broader set of security measures. It is often used in conjunction with encryption to provide an added layer of protection to sensitive data.

## How does the program work?

The program described functions as a steganography tool with specific functionality.

1. **Image Description and Location Extraction (using -map flag)**:
The program takes an image file as input, which is presumably provided in the project description. When the **`-map`** flag is used, the program extracts GPS data from the image's metadata. This GPS data can reveal the location where the image was taken.

2. **PGP Key Extraction (using -steg flag)**:
When the **`-steg`** flag is used, the program reads the content of the image file as raw bytes. It then identifies the block or section of the image where the PGP (Pretty Good Privacy) key is hidden. The PGP key might have been embedded using a steganographic technique, like LSB or another method. The program locates the starting and ending points of the hidden block and extracts the PGP key from it.

# How to run

Ensure you have Python installed by running the following commands:

    sudo apt update
    sudo apt install python3

## Used pip packages:
- Pillow
    pip install pillow
# Usage
```
$ python image.py -h
usage: image.py [-h] [-steg STEG | -map MAP]

inspector-image

options:
  -h, --help  show this help message and exit
  -steg STEG  Extract PGP key
  -map MAP    Extract location
```
```
$ python image.py -map images/image.jpeg
Lat: 32.0866296534937
Lon: 34.885130555555556
```
```
$ python image.py -steg images/image.jpeg
-----BEGIN PGP PUBLIC KEY BLOCK-----  
Version: 01  
  
mQENBGIwpy4BCACFayWXCgHH2QqXkicbqD1ZlMUALpyGxDFiWh1SErFUPJOO/CgU  
2688bAd26kxDSGShiL9YUOQJ6MS+zJ0KlBkeKPoQlPHRBVpH7vjcRbZNgDxd82uE  
7mhM6AH+W3fAim/PhU3lm661UGMCHM3YLupa/N0Dhhmfimtg+0AimCoXk6Q6WJxg  
ao8XY1Wqacd2L0ssASY5EkMahNgtX0Ri8snbTlImd5Jq/sC4buZq96IlxyhtX0ew  
zD/md0U++8SxG9+gi+uuImqV8Wq1YHvJH5BtIbfcNG9V00+03ikEX9tppKxCkhzx  
9rSqvyH6Uirs3FVhFtoXUSg8IeYgSH6p5tsVABEBAAG0CDAxQDAxLjAxiQEcBBAB  
AgAGBQJiMKcuAAoJEAJuInmYDhhbO3gIAITZhEtLBj524y1oeBKI5fZDwgCQum6B  
D9ZaUq1+dI98HsiRAiUqw1YbuJQgeUVGCmqXeC3E7VTPCPZsaCLfWWZVeosRIqB8  
PwGxcY6vXHYR4S6T8rHwsNASw+Vo2pmQIGn4tABmtyappqJbwSz+5yg73DjYXiX/  
e/f6i9nrFFsfMjjKd71cAyHjV8u0z7fGDXpR22vo7CdloXMxsZRyHjd/4ofUgvu0  
6hWYG2zBWTXpwaYRU9u1NCr1gfKnukm8gbILSSgjr8pQ3OLWHleJXc0sCEJFKSbg  
+I0KJP7Ccrxy0MaKYk0T0tYbBrvqQCzXqzAqcjn+1GoDDS1J8WBJopM=  
=N8hc  
-----END PGP PUBLIC KEY BLOCK-----
```



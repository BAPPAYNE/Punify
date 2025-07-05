# Punify - Puny character converter

Description:
Punify is a Python-based utility that converts normal ASCII text into visually similar Unicode characters (known as homoglyphs or confusables). This is often used for obfuscation, fun text transformation, or understanding potential Unicode security issues.

Features:
- Converts each Latin letter into a randomly selected Unicode homoglyph.
- Supports both lowercase and uppercase letters.
- Optionally prints the full map of characters and their homoglyph variants.

Usage:

1. Run the script:
    ```
   ./puny_converter.py -text "Hello World"
    ```
   Example output:
   Original :
       Hello World
   Converted :
       Нëłłö Щőѓłđ

3. View the map of homoglyphs:
    ```
   ./puny_converter.py --print
    ```
   Example output:
   a : à á â ã ä å ā ă ą ȧ ӓ а 
   b : ƀ ƃ ɓ б в 
   ...
   Z : Ź Ż Ž Ƶ Ȥ

Files:
- puny_converter.py : Main script for conversion.
- confusables.txt : (Optional) Reference list of Unicode confusables.

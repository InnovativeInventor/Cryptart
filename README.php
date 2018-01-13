## Cryptart
A way to easily verify files, keys, and other data using art(words, sounds, images)

This is compatible with openssh's randomart and will produce similar-looking output. But, cryptart, when producing colored or grey output (with the flags -c and -g respectively) is much easier to remember, which makes it harder for attackers to fool you. The ascii-only option is the default.

## Usage

```
Usage: cryptart.py [-h] [--file FILE] [--msg MSG] [--height HEIGHT]
                   [--length LENGTH] [--grey] [--color] [--both] [--text]
                   [--art] [--words] [--num NUM]

A tool to generate cryptart of hashes.

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  Specifies file to output password to.
  --msg MSG, -m MSG     Default message to show.
  --height HEIGHT       Height of the cryptoart.
  --length LENGTH, -l LENGTH
                        Length of the cryptoart.
  --grey, -g            Use different shades of grey instead of ascii art.
  --color, -c           Use colors instead of grey or ascii art.
  --both, -b            Use grey or color with ascii art.
  --text, -t            Input text to hash
  --art, -a             Only display art
  --words, -w           Only display words
  --num NUM, -n NUM     Display specified number of words
```

## Ascii cryptart of cryptart.py (dynamically generated)
`php README.php > README.md`
<?php
$cryptart_ascii = shell_exec('python3 cryptart.py -f cryptart.py');
echo "$cryptart_ascii";
?>

## Contributions and related
I was inspired by openssh's randomart, but felt that colors and more visually recognizable patterns could be used instead. Contributions are always welcome!

#!/usr/bin/env python3

# Made by Innovative Inventor at https://github.com/innovativeinventor.
# If you like this code, star it on GitHub!
# Contributions are always welcome.

# MIT License
# Copyright (c) 2017 InnovativeInventor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import hashlib
from pathlib import Path
import sys
from bitstring import BitArray
import numpy as np
import decimal
# import matplotlib.pyplot as plt
# from sympy import Plane, Point3D
# from sympy.plotting import plot3d_parametric_surface
import argparse
from colr import color
import math as mth
import random
import linecache

def art_file(filename,hashtype="sha256"):
    hashtype = "hashlib." + hashtype
    h = eval(hashtype)()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    digest_hex = h.hexdigest()

    # Convert bytes to bits
    bit = BitArray(bytes=h.digest())
    digest_bits = bit.bin
    random.seed(digest_bits)

    # Call other functions
    if not args.art:
        crypto_words(digest_bits)
    # crypto_art(digest_bits,digest_hex)

    if not args.words:
        drunken_bishop(digest_bits,digest_hex)
    return h.hexdigest()

def art_text(hash_text,hashtype="sha256"):
    hashtype = "hashlib." + hashtype
    h = eval(hashtype)()
    hash_encoded = hash_text.encode('utf-8')
    h.update(hash_encoded)
    digest_hex = h.hexdigest()

    # Convert bytes to bits
    bit = BitArray(bytes=h.digest())
    digest_bits = bit.bin
    random.seed(digest_bits)

    # Call other functions
    if not args.art:
        crypto_words(digest_bits)
    # crypto_art(digest_bits,digest_hex)
    if not args.words:
        drunken_bishop(digest_bits,digest_hex)
    return h.hexdigest()

def drunken_bishop(digest_bits,digest_hex):
    bishop_map = np.zeros((args.length,args.height))
    bishop_dimensions = [args.length,args.height] # defaut width = 17 height = 9
    current_location = [8,4]
    pos_values = [" ",".","o","+","=","*","B","O","X","@","%","&","#","/","^"]

    bits_parsed = [str(digest_bits)[i:i+2] for i in range(0, len(digest_bits), 2)]
    num_location_chuncks = len(digest_bits)/8 # divide by 8 for each binary thingy and * two for each pair

    for chunck_count in range (1,int(num_location_chuncks)+1):
        for bit_count in range (1,5):
            directions = bits_parsed[chunck_count*4-bit_count]
            movement_options = [[-1,-1],[1,-1],[-1,1],[1,1]]
            if not check_north(current_location):
                for coord in movement_options:
                    if coord[1] == -1:
                        coord[1] = 0

            if not check_east(current_location,bishop_dimensions):
                for coord in movement_options:
                    if coord[0] == 1:
                        coord[0] = 0

            if not check_south(current_location,bishop_dimensions):
                for coord in movement_options:
                    if coord[1] == 1:
                        coord[1] = 0

            if not check_west(current_location):
                for coord in movement_options:
                    if coord[0] == -1:
                        coord[0] = 0

            if directions == "00":
                move = movement_options[0]
            elif directions == "01":
                move = movement_options[1]
            elif directions == "10":
                move = movement_options[2]
            elif directions == "11":
                move = movement_options[3]

            current_location=[current_location[0]+move[0],current_location[1]+move[1]]
            bishop_map[current_location[0]] [current_location[1]] += 1

    print_map(bishop_map,bishop_dimensions,pos_values,digest_hex)

def print_map(bishop_map,bishop_dimensions,pos_values,digest_hex):
    repeat_header = (bishop_dimensions[0]-len(args.msg)-4)/2
    round_header = decimal.Decimal(repeat_header).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP)
    repeat_footer = bishop_dimensions[0]
    round_footer = decimal.Decimal(repeat_footer).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP)

    if repeat_header.is_integer(): space=" "
    else: space=""

    # Possible code
    # hex_pairs = [str(digest_hex)[i:i+2] for i in range(0, len(digest_hex), 2)]
    #
    # # Creating list of points
    # points_list = np.zeros((mth.floor(len(hex_pairs)/3),3))
    # for points in range (0,mth.floor(len(hex_pairs)/3)):
    #     points_list[points] = [int(hex_pairs[points], 16), int(hex_pairs[points+1], 16), int(hex_pairs[points+2], 16)]
    #
    # # Going to find average
    # coord_x = []
    # coord_y = []
    # coord_z = []
    # for points in range(0,len(points_list)):
    #     print (points)
    #     coord_x.append(points_list[points][0])
    #     coord_y.append(points_list[points][1])
    #     coord_z.append(points_list[points][2])
    #
    #
    # # Finding equation of line
    # line = Line3D(Point3D(int(hex_pairs[0], 16), int(hex_pairs[1], 16), int(hex_pairs[2], 16)), Point3D(0,0,0))
    # test = []
    # for planes in range (0,mth.floor(len(coord_x)/3)):
    #     print (planes) # debug
    #     # print (coord_z[planes+0])
    #     # defined_planes[planes]
    #     plane = Plane(Point3D(coord_x[planes], coord_y[planes], coord_z[planes]), Point3D(coord_x[planes+1], coord_y[planes+1], coord_z[planes+1]), Point3D(coord_x[planes+2], coord_y[planes+2], coord_z[planes+2]))
    #     # p = plot3d_parametric_surface(Plane(Point3D(coord_x[planes], coord_y[planes], coord_z[planes]), Point3D(coord_x[planes+1], coord_y[planes+1], coord_z[planes+1]), Point3D(coord_x[planes+2], coord_y[planes+2], coord_z[planes+2])))
    #     # p.saveimage('plot.png', format='png')
    #
    # x_avg = round(sum(coord_x)/len(coord_x))
    # y_avg = round(sum(coord_y)/len(coord_y))
    # z_avg = round(sum(coord_z)/len(coord_z))

    header = "+" + "-"*int(round_header) + "[ " + args.msg + space + "]" + "-"*int(round_header) + "+"
    footer = "+" + "-"*int(round_footer) + "+"
    print (header)

    # color code
    red = random.sample(range(255), 14)
    red_sorted = sorted(red, reverse=True)
    green = random.sample(range(255), 14)
    green_sorted = sorted(green, reverse=True)
    blue = random.sample(range(255), 14)
    blue_sorted = sorted(blue, reverse=True)

    for columns in range(0,bishop_dimensions[1]):
        print ("|", end='')
        for rows in range(0,bishop_dimensions[0]):
            value = bishop_map[int(rows)][int(columns)]
            grey_value = 255-(int(value)*25)
            if args.grey:
                print(color(" ", back=(grey_value, grey_value, grey_value)), end='')
            elif args.color:
                print(color(" ", back=(red_sorted[int(value)], green_sorted[int(value)], blue_sorted[int(value)])), end='')
            elif args.both and args.color:
                print(color(pos_values[int(value)], back=(red[value], green[value], blue[value])), end='')
            elif args.both:
                print(color(pos_values[int(value)], back=(grey_value, grey_value, grey_value)), end='')
            else:
                print(pos_values[int(value)], end='')
        print ("|")

    print (footer)

def check_north(current_location):
    if current_location[1]-1 < 0:
        return False
    else:
        return True

def check_east(current_location,bishop_dimensions):
    if current_location[0]+1 >= bishop_dimensions[0]:
        return False
    else:
        return True

def check_south(current_location,bishop_dimensions):
    if current_location[1]+1 >= bishop_dimensions[1]:
        return False
    else:
        return True

def check_west(current_location):
    if current_location[0]-1 < 0:
        return False
    else:
        return True

def crypto_words(digest_bits):
    import git
    current_dir = Path("dict4schools/safedict_full.txt")
    etc = Path("/etc/dict4schools/safedict_full.txt")

    if current_dir.exists():
        g = git.cmd.Git("dict4schools")
        g.pull
        lines = file_len("dict4schools/safedict_full.txt")
    elif etc.exists():
        g = git.cmd.Git("/etc/dict4schools")
        g.pull
        lines = file_len("/etc/dict4schools/safedict_full.txt")
    else:
        git.Repo.clone_from("https://github.com/InnovativeInventor/dict4schools", "/etc/dict4schools")

    for i in range(0,args.num):
        line_num = random.randrange(lines)
        print (linecache.getline("dict4schools/safedict_full.txt", line_num).rstrip(), end=' ')
    print()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

parser = argparse.ArgumentParser(description='A tool to generate random passwords.')
parser.add_argument("--file", "-f", type=str, default="README.md", help="Specifies file to output password to.")
parser.add_argument("--msg", "-m", type=str, default="Cryptoart", help="Default message to show.")
parser.add_argument("--height", type=int, default="9", help="Height of the cryptoart.")
parser.add_argument("--length", "-l", type=int, default="17", help="Length of the cryptoart.")
parser.add_argument("--grey", "-g", help="Use different shades of grey instead of ascii art.", action="store_true")
parser.add_argument("--color", "-c", help="Use colors instead of grey or ascii art.", action="store_true")
parser.add_argument("--both", "-b", help="Use grey or color with ascii art.", action="store_true")
parser.add_argument("--text", "-t", help="Input text to hash", action="store_true")
parser.add_argument("--art", "-a", help="Only display art", action="store_true")
parser.add_argument("--words", "-w", help="Only display words", action="store_true")
parser.add_argument("--num", "-n", type=int, default="3", help="Display specified number of words")
args = parser.parse_args()

input_file = Path(args.file)
if input_file.exists():
    hashes = art_file(args.file)
elif args.text:
    hashes = art_text(args.text)
else:
    print ("Error, file does not exist")
    exit(1)

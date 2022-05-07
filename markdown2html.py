#!/usr/bin/python3
""" Script that takes two arguments for markdown engine
    Arguments
    =========
        First argument is the name of the Markdown file
        Second argument is the output file name
"""
from enum import Flag
from os.path import exists
from sys import argv, stderr


if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    else:
        if not exists(argv[1]):
            print(f"Missing {argv[1]}", file=stderr)
            exit(1)
        else:
            with open(argv[1], mode="r") as file:
                with open(argv[2], mode="w") as new_file:
                    html_lines = []
                    for line in file:
                        split = line.split(" ")
                        if (split[0] == "#"):
                            line = line.replace("# ", "<h1>")
                            line = line[:-1] + "</h1>\n"
                        elif (split[0] == "##"):
                            line = line.replace("## ", "<h2>")
                            line = line[:-1] + "</h2>\n"
                        elif (split[0] == "###"):
                            line = line.replace("### ", "<h3>")
                            line = line[:-1] + "</h3>\n"
                        elif (split[0] == "####"):
                            line = line.replace("#### ", "<h4>")
                            line = line[:-1] + "</h4>\n"
                        elif (split[0] == "#####"):
                            line = line.replace("##### ", "<h5>")
                            line = line[:-1] + "</h5>\n"
                        elif (split[0] == "######"):
                            line = line.replace("###### ", "<h6>")
                            line = line[:-1] + "</h6>\n"
                        elif (split[0] == "-"):
                            if (html_lines[-1][0:5] != "</ul>"):
                                html_lines.append("<ul>\n")
                                html_lines.append("</ul>\n")
                            line = line.replace("- ", "<li>")
                            line = line[:-1] + "</li>\n"
                            html_lines.insert(-1, line)
                            continue
                        html_lines.append(line)
                    new_file.writelines(html_lines)
            exit(0)

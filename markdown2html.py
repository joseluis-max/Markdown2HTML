#!/usr/bin/python3
""" Script that takes two arguments for markdown engine
    Arguments
    =========
        First argument is the name of the Markdown file
        Second argument is the output file name
"""
from os.path import exists
from sys import argv, stderr
import hashlib


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
                        if (line[:2] == "**" and line[-3:-1] == "**"):
                            html_lines.append("<b>" + line[2:-3] + "</b>\n")
                            continue
                        if (line[:2] == "((" and line[-3:-1] == "))"):
                            line = "<p>\n" + line[2:-3] + "\n</p>\n"
                            line = line.replace("c", "")
                            line = line.replace("C", "")
                            html_lines.append(line)
                            continue
                        # if (line[:2] == "__" and line[-3:-1] == "__"):
                        #     html_lines.append("<em>" + line[2:-3] + "</em>\n")
                        #     continue
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
                        elif (split[0] == "*"):
                            if (html_lines[-1][0:5] != "</ol>"):
                                html_lines.append("<ol>\n")
                                html_lines.append("</ol>\n")
                            line = line.replace("* ", "<li>")
                            line = line[:-1] + "</li>\n"
                            html_lines.insert(-1, line)
                            continue
                        else:
                            if (split[0] != "\n"):
                                if (html_lines[-1][-6:] == "\n</p>\n"):
                                    html_lines[-1] = html_lines[-1][:-6] + "\n<br />\n" + line + "</p>\n"
                                    continue
                                elif (html_lines[-1][-5:] == "</p>\n"):
                                    html_lines[-1] = html_lines[-1][:3] + "\n" + html_lines[-1][3:-5] + "\n<br />\n" + line[:-1] + "\n</p>\n"
                                    continue
                                line = "<p>" + line[:-1] + "</p>\n"
                        html_lines.append(line)
                    
                    flag = True
                    flag1 = True
                    flag2 = True
                    for l in html_lines:
                        for i in range(len(l)):
                            if (l[i] == "*" and l[i + 1] == "*"):
                                if (flag):
                                    flag = False
                                    l = l[:i] + "<b>" + l[i+2:]
                                else:
                                    flag = True
                                    l = l[:i] + "</b>" + l[i+2:]
                            if (l[i] == "_" and l[i + 1] == "_"):
                                if (flag1):
                                    flag1 = False
                                    l = l[:i] + "<em>" + l[i+2:]
                                else:
                                    flag1 = True
                                    l = l[:i] + "</em>" + l[i+2:]
                            if (l[i] == "[" and l[i + 1] == "["):
                                counter = i

                                while (l[counter] != "]" and l[counter+1] != "]"):
                                    counter += 1

                                string = l[i+2: counter]
                                result = hashlib.md5(string.encode())
                                result = result.hexdigest()
                                l = l[:3] + "\n" + l[3:i] + result + l[counter+3:4] + "\n</p>\n"
                        new_file.write(l)
            exit(0)

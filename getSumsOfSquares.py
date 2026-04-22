#!/usr/bin/env python3

import os
import sys
import re

def basicTemplateFile(poly, vars):
    temp_file = os.popen('mktemp').read().strip()

    f = open(temp_file, 'w') 
    f.write("needsPackage(\"SumsOfSquares\")\n")
    f.write("R = QQ[" + vars + "]\n")
    f.write(f"p = {poly}\n")
    f.write(f"sol = solveSOS (p, RoundTol => 3, TraceObj => false)\n")
    f.close()

    return temp_file

def runScript(temp_file, deleteQ):
    out = os.popen(f"M2 --script {temp_file}").read().strip()

    if deleteQ == "T":
        os.system(f"rm {temp_file}")
    else:
        print(f">> {temp_file}")

    return out

# TODO Implement getCertificate
def getCertificate(poly, vars, deleteQ):
    temp_file = basicTemplateFile(poly, vars)

    f = open(temp_file, 'a') 
    f.write("s = sosPoly sol\n")
    f.write("coeffs = s#coefficients\n")
    f.write("sosPolys = s#generators\n")
    # f.write("l = #coeffs\n")
    # f.write("exp = for i from 0 to (l-1) list coeffs#i*(sosPolys#i)^2\n")
    # f.write("print (toString exp)\n")
    f.write("print \"coeffs\"\n")
    f.write("print (toString coeffs)\n")
    f.write("print \"generators\"\n")
    f.write("print (toString sosPolys)\n")
    f.close()

    out = runScript(temp_file, deleteQ)
    print(out)

# To process the output in Mathematica, use the command
# ToExpression[<string>, TeXForm]
def printTeXCertificate(poly, vars, deleteQ):
    temp_file = basicTemplateFile(poly, vars)

    f = open(temp_file, 'a') 
    f.write("print tex sosPoly sol\n")
    f.close()

    out = runScript(temp_file, deleteQ)

    out = re.sub(r"\\,", "", out)
    out = re.sub(r"\\:", "", out)
    out = out.split("Rightarrow")

    coeffs = re\
        .search(r"\\left\\{.*\\right\\}", out[1])\
        .group()[7:-8]\
        .split(',')
    gens = re\
        .search(r"\\left\\{.*\\right\\}", out[2])\
        .group()[7:-8]\
        .split(',')

    expr = []
    for i in range(len(gens)):
        expr.append(coeffs[i] + "(" + gens[i] + ")^2")

    print("+".join(expr))

def printTeXGramMatrix(poly, vars, deleteQ):
    temp_file = basicTemplateFile(poly, vars)

    f = open(temp_file, 'a') 
    f.write("print tex sol#GramMatrix\n")
    f.write("print tex sol#Monomials\n")
    f.close()

    out = runScript(temp_file, deleteQ)

    print(out)

if __name__== "__main__":
    if sys.argv[4] == "TeXCertificate":
        printTeXCertificate(sys.argv[1], sys.argv[2], sys.argv[3])
    if sys.argv[4] == "Certificate":
        getCertificate(sys.argv[1], sys.argv[2], sys.argv[3])
    if sys.argv[4] == "TeXGramMatrix":
        printTeXGramMatrix(sys.argv[1], sys.argv[2], sys.argv[3])

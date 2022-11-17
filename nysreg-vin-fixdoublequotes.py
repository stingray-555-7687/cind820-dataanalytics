outFileName = "tmp/nydmvvin-goodhdr/NYDMV-VIN-OUTPUT-merged-fixedquotes.csv"
inFileName = "tmp/nydmvvin-goodhdr/NYDMV-VIN-OUTPUT-merged.csv"

inF = open(inFileName,"r")
outF = open(outFileName,"w")

lineNo = 0

#for line in inF:
while inF:
    line = inF.readline()
    if line == "":
        break
    print("line no =",lineNo,end="")
    # find double quote
    dblQtePos = line.find(', "')
    if dblQtePos < 0:
        outF.write(line)
    else:
        # change double quote to single quote
        newLine = line[:dblQtePos] + ", '"
        while (dblQtePos >= 0):
            dblQtePosEnd = line.find('",',dblQtePos+3)
            for pos in range(dblQtePos+3,dblQtePosEnd):
                # remove single quotes within the double quotes
                if line[pos]!="'":
                    newLine = newLine + line[pos]
            # change closing double quote to single quote
            newLine = newLine + "', "
            dblQtePos = line.find(', "',dblQtePosEnd+1)
            if dblQtePos < 0:
                newLine = newLine + line[dblQtePosEnd+3:]
            else:
                if line.find('",',dblQtePos+3) < 0:
                    # temporary fix, actual problem is text like this: , \'Open, "Generac" Generator sets only\', which is valid
                    # found in entry=5721495, line 5009393
                    newLine = newLine + line[dblQtePosEnd+3:]
                    dblQtePos = -1
                else:
                    newLine = newLine + line[dblQtePosEnd+3:dblQtePos] + ", '"
        print(" - Fixed:",newLine)
        outF.write(newLine)
    lineNo = lineNo + 1
    if lineNo == 5009393 or lineNo == 5009394:
        print("",end="")
    print(end="\r")

print()
inF.close()
outF.close()

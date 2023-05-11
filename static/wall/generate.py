import os, shutil

filelist = os.listdir(".")

excluded = ["index.html","generate.py","index.html.bak",".DS_Store","index.constr"]

# delete old content        
        
#copy and overwrite
shutil.copy2("index.constr", "index.html")

#rename to index.html
#os.rename(targetPath, correctTarget)

for file in filelist:
    if file not in excluded:
        insert = '\n<h4><a href="' + file + '">' + file + '</a></h4>\n'
        
        # write content
        with open("index.html") as myFile:
            for num, line in enumerate(myFile, 1):
                if '<!--start list-->' in line:
                    lineInsert = num + 1
                    f = open("index.html", "r")
                    contents = f.readlines()
                    f.close()

                    contents.insert(num, insert)

                    
                    f = open("index.html", "w")
                    contents = "".join(contents)
                    f.write(contents)
                    f.close()





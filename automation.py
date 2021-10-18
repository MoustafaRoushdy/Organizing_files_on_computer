import os 
import shutil 

current_dir = os.path.dirname(os.path.realpath(__file__))
print(current_dir)
if not os.path.exists("moustafa"):
    os.mkdir("moustafa")

for filename in os.listdir(current_dir):
    if filename.endswith((".png",".jpg",".jpeg","gif")):
        if not os.path.exists("images"):
            os.mkdir('images')
        shutil.copy(filename,"images")
        os.remove(filename)
        print("done")

for filename in os.listdir(current_dir):
    if filename.endswith((".pdf")):
        if not os.path.exists(".pdf"):
            os.mkdir('pdf')
        shutil.copy(filename,".pdf")
        os.remove(filename)
        print("done")

for filename in os.listdir(current_dir):
    if filename.endswith((".word")):
        if not os.path.exists(".word"):
            os.mkdir('word')
        shutil.copy(filename,"word")
        os.remove(filename)
        print("done")

for filename in os.listdir(current_dir):
    if filename.endswith((".ppt")):
        if not os.path.exists(".ppt"):
            os.mkdir('ppt')
        shutil.copy(filename,"ppt")
        os.remove(filename)
        print("done")
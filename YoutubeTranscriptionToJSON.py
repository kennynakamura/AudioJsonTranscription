import json
import os

def line_to_dict(split_Line):

    line_dict = {}
    for part in split_Line:
        key, value = part.split(" ", maxsplit=1)
        line_dict[key] = value

    return line_dict

def convert(file) :
    f = open(file, "r", encoding = "utf-8")
    content = f.read()
    splitcontent = content.splitlines()

    def chunks(l, n):
        n = max(1, n)
        return (l[i:i+n] for i in range(0, len(l), n))

    lines = chunks(splitcontent,6)
    lines = [line_to_dict(l) for l in lines]
    return lines

def listify(arg):
    return arg if isinstance(arg, list) else [arg]

def main():
   count = 0
   d = open("TextoOrganizado.txt", "w")
   #Arquivo de texto com a transcrição do Youtube
   with open("/content/teste.txt") as f:
     read = f.readlines()
     for i, line in enumerate(read[:-2]):
         count += 1
         line.rstrip()
         if (count % 2) != 0:
            lineBegin = "begin " + line.rstrip()[3:] + "\n"
            d.write(lineBegin)
            d.write("children \n")
            d.write("end " + read[i+2].rstrip()[3:] + "\n")
            d.write("id " + str(int(i/2)) +"\n") 
            d.write("language pt\n") 
         else:
            line = "lines " + line.rstrip()
            d.write(line +"\n")
   d.close()

   lines = convert("/content/TextoOrganizado.txt")

   for sub in lines:
       for key in sub:
         if key == "children":
           sub[key] = list(sub[key])
         if key == "lines":
           sub[key] = listify(sub[key])

   with open("YoutubeTranscription.json", 'w') as fout:
        json.dump(lines, fout, indent=4, ensure_ascii=False)
   os.remove("/content/TextoOrganizado.txt")
   return

if __name__ == "__main__":
    main()

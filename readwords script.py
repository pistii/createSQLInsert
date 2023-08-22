lines = []
exportName = open("words_export.txt", "w")

#Kigyűjti az 1 jelentésű szavakat
with open("words.csv", "r") as file:
    for x in file:
        feldolgozott = file.readline().strip(';;;;;;;;;;;;;;;\n')
        darabolt = feldolgozott.split(";")
        if (len(darabolt)<=2 & len(darabolt)>1):
            kt = [
                {"hungarian": darabolt[0],
                "english" : darabolt[1]}
            ]
            lines.append(kt)        
#Kiíratás
for x in lines:
    for j in x:
        hun = j.get('hungarian')
        eng = j.get('english')
        exportName.write(f"INSERT INTO [dbo].[Words] (englishMeaning, hungarianMeaning, rememberanceLevel) VALUES ('{hun}', '{eng}',0);")
        exportName.write("\n")
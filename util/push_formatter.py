def push_formatted(dataJson):
    with open("tobe_sent.txt", 'w') as txtf:
        for k,v in dataJson.items():
            txtf.write(str(k) + ' : ' + str(v) + str("\n"))
        
    with open("tobe_sent.txt", 'r') as txtf:
        textread = txtf.read()
        return textread
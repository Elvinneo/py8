def finder(sentence):
    consonants=['b','c','ç','ğ','ş','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    temp=[]
    for i in sentence:
        if i.lower() in consonants and not i.lower() in temp:
            temp.append(i.lower())
    print(temp)


          

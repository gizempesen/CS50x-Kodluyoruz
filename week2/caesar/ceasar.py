encrypted_message = ''  #şifrelencek mesajı tanımlıyoruz 
 
alphabet=['a','b' ,'c' , 'd', 'e', 'f', 'g' ,'h' ,'i' ,'j','k' ,'l' ,'m' ,'n' ,
    'o' ,'p' ,'r' ,'s' ,'t' ,'u' ,'v', 'y' ,'z']  #alfabenin uzunluğuna ihtiyacımız olucak.
 
message = 'abc'            #Şifrelenecek mesaj giriliyor.
for i in message:           #mesajımızın her karakterine for yardımı ile ulaşırız
       
    encrypted_message += alphabet[(alphabet.index(i)+3) % len(alphabet)]
       #şifrelenmiş mesaja alfabenin i. indexinden +3 miktar uzaktaki karaktere
       #erişiyorum (% len(alphabet)-> eğer +3 yaptığımızda alfabenin uzunluğundan
       #büyük bir index elde edersek hata alırız. Onun için alfabenin boyuna 
       #bölerek mod alıyoruz. Böylelikle, diyelimki 27miktar kaydırma istenildiğinde
       #27%26 = 1 (kalan 1) olacağından 1 ötedeki harfa kaydırma yapılsın.
     
print("The encrypted message is:", encrypted_message)

def ceaser(message, key):
    encrypted_message = ''
 
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    for i in message:
 
        if i not in alphabet:
            encrypted_message += i
        else:
            encrypted_message += alphabet[
                (alphabet.index(i)+shift) % len(alphabet)]
 
    print("The encrypted message is:", encrypted_message)
 
 
shift = int(input('Shift value: '))
 
text = input("Your message: ")
ceaser(text, shift)

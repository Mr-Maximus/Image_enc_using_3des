from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import DES3
from Crypto import Random
from Crypto.Random import get_random_bytes
import time



def _make_des3_encryptor(key, iv):
    encryptor = DES3.new(key, DES3.MODE_CFB, iv)
    return encryptor



def des3_encrypt(key, iv, data):
    encryptor = _make_des3_encryptor(key, iv)
    #pad_len = 8 - len(data) % 8 # length of padding
    #padding = chr(pad_len) * pad_len # PKCS5 padding content
    #data += padding
    return encryptor.encrypt(data)

def des3_decrypt(key, iv, data):
    encryptor = _make_des3_encryptor(key, iv)
    result = encryptor.decrypt(data)
    #pad_len = ord(result[-1])
    #result = result[:-pad_len]
    return result



def encrypt(): 
    try:
        #iv = Random.new().read(DES3.block_size)
        iv = b'=-\x8fD\xa9T\xf4&'
        print(iv)
        key=entry1.get(1.0,END)
        key=key.encode()
        b=65
        if(len(key)<24):
            while(len(key)<24):
                key=key+chr(b).encode()
                b+=1
        print('your key is being generated')
        time.sleep(2)
        print('Your key is generated')
        print('Here is your key : save it to decrypt:',key)
        file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg'),('png file','*.png')])
        fin = open(file1.name,'rb')
        image=fin.read()
        fin.close()
        image=bytearray(image)
    except Exception:
        print('error caught:',Exception.__name__)
    msg=des3_encrypt(key,iv,image)
    image=msg        
    fin = open(file1.name,'wb')   
    fin.write(image)
    fin.close()
    print('encryption done..')
    print('WARNING!! here is your key do not lose it')
    print('Here is your key : save it to decrypt:',key)
    

def decrypt():
    print('we will be decrypting your message')
    print('please provide the key')
    x=entry1.get(1.0,END)
    x=x.encode()
    b=65
    if(len(x)<24):
        while(len(x)<24):
            x=x+chr(b).encode()
            b+=1
    #print('iv')
    #z=input()
    print('your decryption will begin now')
    file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg'),('png file','*.png')])
    fin = open(file1.name,'rb')
    image=fin.read()
    fin.close()
    image=bytearray(image)
    msg=des3_decrypt(x,b'=-\x8fD\xa9T\xf4&',image)
    image=msg        
    fin = open(file1.name,'wb')   
    fin.write(image)
    fin.close()
    print('decryption done..')

root = Tk()
root.geometry("200x120")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg'),('png file','*.png')])
    if file1 is not None:
        file_name = file1.name
        print(file_name)
        key=entry1.get(1.0,END)
        print(file_name,key)
        fi = open(file_name,'rb')
        image=fi.read()
        fi.close()
        image =bytearray(image)
        for index,value in enumerate(image):
            image[index] = value^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()
        
    
b1 = Button(root,text="encrypt",command=encrypt)
b1.place(x=90,y=10)

b2 = Button(root,text="decrypt",command=decrypt)
b2.place(x=30,y=10)

entry1 = Text(root,height=1,width=10)
entry1.place(x=50,y=50)

root.mainloop()

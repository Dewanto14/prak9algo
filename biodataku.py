# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:19:25 2023

@author: Huawei
"""

def writeFile():
    inputnama = input("Masukkan Nama: ")
    inputumur = input("Masukkan Umur: ")
    inputalamat = input("Masukkan Alamat: ")
    inputemail = input("Masukkan Email: ")
    inputdosen = input("Masukkan Dosen Wali: ")
    
    fileWrite = open("Biodata.txt", "w")
    fileWrite.write("nama: " + inputnama + "\numur: " + inputumur + "\nalamat: " + inputalamat + "\nemail: " + inputemail + "\ndosen wali: " + inputdosen)
    fileWrite.close()
    
def readFile():
    fileRead = open("Biodata.txt", "r")
    text = fileRead.read()
    print("Berikut ini Data Kamu")
    print(text)
    fileRead.close()
    
writeFile()
print("\n")
readFile()
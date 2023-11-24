# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:39:58 2023

@author: Huawei
"""

def buat_file():
    file_name = input("Masukkan Nama File: ")
    input_nama = input("Masukkan Namamu: ")
    input_nim = input("Masukkan NIM kamu: ")
    input_angkatan = input("Masukkan tahun angkatanmu: ")
    try:
        with open(file_name,"w") as file:
            file.write("Nama: " + input_nama + "\nNIM: " + input_nim + "\nTahun Angkatan: " + input_angkatan)
            file.close()
            print(f"File {file_name} berhasil dibuat.")
    except Exception as e:
        print(f"Error: {e}")
        
def read_file():
    file_name = input("Masukkan Nama File: ")
    try:
        with open(file_name,"r") as file:
            content = file.read()
            print(f"Isi dari file {file_name}: \n\n\n{content}")
    except FileNotFoundError:
        print(f"File{file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Error: {e}")
        
def add_text_to_file():
    file_name = input("Masukkan Nama File: ")
    input_sahabat = input("Masukkan Nama Sahabatmu: ")
    input_catatan = input("Masukkan Catatan Tambahan Kamu: ")
    try:
        with open(file_name,"a") as file:
            file.write("\nNama Sahabat: " + input_sahabat + "\nCatatan: " + input_catatan)
            file.close()
            print("Data berhasil di tambahkan")
    except FileNotFoundError:
        print(f"File{file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("===== Program File Handling =====")
        print("1. Membuat dan Menulis File")
        print("2. Membaca File")
        print("3. Menambahkan Text Pada File")
        print("4. Keluar dari Program")
        
        choice = input("Masukkan Pilihan Berupa Angka (1/2/3/4): ")
        
        if choice == '1':
            buat_file()
        if choice == '2':
            read_file()
        if choice == '3':
            add_text_to_file()
        if choice == '4':
            print("Terima kasih! Program ditutup.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih 1, 2, 3, atau 4.")
            
main()
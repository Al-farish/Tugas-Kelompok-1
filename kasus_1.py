print("\n===== Silahkan di pilih: \na. Bola\nb. Kubus\nc. Balok")
pilihan_1 = input("Masukan Pilihan anda: ")

## Bola
if pilihan_1 == "a" or pilihan_1 == "A":
    print("\n===== Anda memilih: ", pilihan_1,"\nSilahkan anda memilih statement: ")
    print("1. Keliling\n2. Luas\n3. Volume")
    pilihan_2 = input("Masukan Pilihan anda: ")
    
    if pilihan_2 == "1": # Keliling Bola
        print("\n=== Berikut adalah Rumus Keliling Bola ===")
        r = int(input("Masukan jari-jari Bola: "))
        
        print("Hasilnya ialah: ")
        keliling = (4/3) * (22/7) * (r**2) # rumus keliling bola
        print("Keliling = 4/3 * π * r2\nKeliling = 4/3 * 22/7 *", r**2,"\nKeliling =", keliling, "cm²")
    
    elif pilihan_2 == "2": # Luas Permukaan Bola
        print("\n=== Berikut adalah Rumus Luas Permukaan Bola ===")
        r = int(input("Masukan jari-jari Bola: "))
        
        print("Hasilnya ialah: ")
        luas = 4 * (22/7) * (r**2) # rumus luas permukaan bola
        print("Luas Permukaan = 4 * π * r2\nLuas Permukaan = 4 * 22/7 *", r**2,"\nLuas Permukaan =", luas, "cm²")
    
    elif pilihan_2 == "3": # Volume Bola
        print("\n=== Berikut adalah Rumus Volume Bola ===")
        r = int(input("Masukan jari-jari Bola: "))
        
        print("Hasilnya ialah: ")
        volume = (4/3) * (3.14) * (r**3) # rumus volume bola
        print("Volume = 4/3 * π * r3\nVolume = 4/3 * 3.14 *", r**3,"\nVolume =", volume, "cm³")
    
    else:
        print("\n!!! Data yang anda inputkan tidak Valid !!!")

## Kubus
elif pilihan_1 == "b" or pilihan_1 == "B":
    print("\n===== Anda memilih: ", pilihan_1,"\nSilahkan anda memilih statement: ")
    print("1. Keliling\n2. Luas\n3. Volume")
    pilihan_2 = input("Masukan Pilihan anda: ")
    
    if pilihan_2 == "1": # Keliling Kubus
        print("\n=== Berikut adalah Rumus Keliling Kubus ===")
        s = int(input("Masukan Panjang sisi Kubus: "))
        
        print("Hasilnya ialah: ")
        keliling = 12 * s #rumus keliling kubus
        print("Keliling = 12 * sisi\nKeliling = 12 *", s,"\nKeliling =", keliling, "cm²")
    
    elif pilihan_2 == "2": # Luas Permukaan Kubus
        print("\n=== Berikut adalah Rumus Luas Permukaan Kubus ===")
        s = int(input("Masukan Panjang sisi Kubus: "))
        
        print("Hasilnnya ialah ")
        luas = 6 * (s * s) # rumus luas permukaan kubus
        print("Luas Permukaan = 6 * (s * s)\nLuas Permukaan = 6 *", '(',s,'*',s ,')' ,"\nLuas Permukaan =", luas, "cm²")
    
    elif pilihan_2 == "3": # Volume Kubus
        print("\n=== Berikut adalah Rumus Volume Kubus ===")
        s = int(input("Masukan Panjang sisi Kubus: "))
        
        print("Hasilnnya ialah ")
        volume = s**3 #rumus volume kubus
        print("Volume = s3\nVolume = " ,s,'*',s,'*',s,"\nVolume =", volume, "cm³")
    
    else:
        print("\n!!! Data yang anda inputkan tidak Valid !!!")

## Balok
elif pilihan_1 == "c" or pilihan_1 == "C":
    print("\n===== Anda memilih: ", pilihan_1,"\nSilahkan anda memilih statement: ")
    print("1. Keliling\n2. Luas\n3. Volume")
    pilihan_2 = input("Masukan Pilihan anda: ")
    
    if pilihan_2 == "1": # Keliling Balok
        print("\n=== Berikut adalah Rumus Keliling Balok ===")
        p = int(input("Masukan panjang Balok : "))
        l = int(input("Masukan lebar Balok   : "))
        t = int(input("Masukan tinggi Balok  : "))
        
        print("\nHasilnya ialah: ")
        keliling = 4 * (p + l + t) # rumus keliling balok
        print("Keliling = 4 * (p + l + t)\nKeliling = 4 *", '(',p,'+',l,'+',t,')',"\nkeliling = 4 * ", (p + l + t),"\nKeliling =", keliling, "cm²")
    
    elif pilihan_2 == "2": # Luas Permukaan Balok
        print("\n=== Berikut adalah Rumus Luas Permukaan Balok ===")
        p = int(input("Masukan panjang Balok : "))
        l = int(input("Masukan lebar Balok   : "))
        t = int(input("Masukan tinggi Balok  : "))
        
        print("\nHasilnnya ialah: ")
        luas = 2 * ((p * l) + (p * t) + (l * t)) # rumus luas permukaan balok
        print("Luas Permukaan = 2 * ( p * l + p * t + l * t )\nLuas Permukaan = 2 *",'(',p,'*',l,'+',p,'*',t,'+',l,'*',t,')' ,"\nLuas Permukaan = 2 *", ((p * l) + (p * t) + (l * t)),"\nLuas Permukaan =", luas, "cm²")
    
    elif pilihan_2 == "3": # Volume Balok
        print("\n=== Berikut adalah Rumus Volume Balok ===")
        p = int(input("Masukan panjang Balok : "))
        l = int(input("Masukan lebar Balok   : "))
        t = int(input("Masukan tinggi Balok  : "))
        
        print("\nHasilnnya ialah: ")
        volume = p * l * t # rumus volume balok
        print("Volume = p * l * t\nVolume = ", p,'*',l,'*',t ,"\nVolume =", volume, "cm³")
    
    else:
        print("\n!!! Data yang anda inputkan tidak Valid !!!")

else:
    print("\n!!! Data yang anda inputkan tidak Valid !!!")
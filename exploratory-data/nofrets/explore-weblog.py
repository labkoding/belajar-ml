daftarIpArray = []
countLogin = 0
loginUrlPerIP = {}
with open('../weblog.csv', "r") as f:
    for line in f:
        # count string in line
        if '/login.php' in line:
            countLogin += 1
        hasilSplit = line.split(',')
        # check if string is ip address
        if len(hasilSplit[0].split('.')) == 4:
            # append if not exist
            if hasilSplit[0] not in daftarIpArray:
                daftarIpArray.append(hasilSplit[0])
        
# contoh hasil akhir untuk variable loginUrlPerIP
loginUrlPerIP = {"10.128.2.1": 5}

print(daftarIpArray)
print(countLogin)
print(loginUrlPerIP)
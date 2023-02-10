daftarIpArray = []
countLogin = 0
countLogout = 0
loginUrlPerIP = {}

with open(r"C:\Users\HP\Downloads\belajar-ml\exploratory-data\nofrets\weblog.csv") as f:
    for line in f:
        # count string in line
        if '/login.php' in line:
            countLogin += 1
            hasilSplit = line.split(',')
            if len(hasilSplit[0].split('.')) == 4:
                if hasilSplit[0] in loginUrlPerIP:
                    loginUrlPerIP[hasilSplit[0]] += 1
                else:
                    loginUrlPerIP[hasilSplit[0]] = 1
        if '/logout.php' in line:
            countLogout += 1
        hasilSplit = line.split(',')
        # check if string is ip address
        if len(hasilSplit[0].split('.')) == 4:
            # append if not exist
            if hasilSplit[0] not in daftarIpArray:
                daftarIpArray.append(hasilSplit[0])

# sort daftarIpArray based on the number of login.php accesses
sortedIpArray = sorted(loginUrlPerIP.items(), key=lambda x: x[1], reverse=True)

print(sortedIpArray)
print(countLogin)
print(countLogout)
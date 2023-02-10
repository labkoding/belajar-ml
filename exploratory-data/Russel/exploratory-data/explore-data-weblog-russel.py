daftarIpArray = []
countLogin = 0
countLogout = 0
loginUrlPerIP = {}
logoutUrlPerIP = {}
with open("C:/Users/Asus/belajar-ml/exploratory-data/nofrets/weblog.csv", "r") as f:
    for line in f:
        hasilSplit = line.split(',')
        # check if string is ip address
        if len(hasilSplit[0].split('.')) == 4:
            # append if not exist
            if hasilSplit[0] not in daftarIpArray:
                daftarIpArray.append(hasilSplit[0])
            
            # count the number of login and logout accesses
            if '/login.php' in line:
                countLogin += 1
                if hasilSplit[0] in loginUrlPerIP:
                    loginUrlPerIP[hasilSplit[0]] += 1
                else:
                    loginUrlPerIP[hasilSplit[0]] = 1
            if '/logout.php' in line:
                countLogout += 1
                if hasilSplit[0] in logoutUrlPerIP:
                    logoutUrlPerIP[hasilSplit[0]] += 1
                else:
                    logoutUrlPerIP[hasilSplit[0]] = 1

# sort the daftarIpArray based on the number of login.php and logout.php accesses
daftarIpArray.sort(key=lambda x: (loginUrlPerIP.get(x, 0), logoutUrlPerIP.get(x, 0)))

print(daftarIpArray)
print(countLogin)
print(countLogout)
print(loginUrlPerIP)
print(logoutUrlPerIP)

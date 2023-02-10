daftarIpArray = []
countLogin = 0
countLogout = 0
loginUrlPerIP = {}
with open(r"D:/INFORMATIKA VALDO/belajar-ml/exploratory-data/nofrets/weblog.csv") as f:
    for line in f:
        # count string in line
        if '/login.php' in line:
            countLogin += 1
            hasilSplit = line.split(',')
            # check if string is ip address
            if len(hasilSplit[0].split('.')) == 4:
                # update the count of login URL access by the IP address
                if hasilSplit[0] in loginUrlPerIP:
                    loginUrlPerIP[hasilSplit[0]] += 1
                else:
                    loginUrlPerIP[hasilSplit[0]] = 1
                # append if not exist
                if hasilSplit[0] not in daftarIpArray:
                    daftarIpArray.append(hasilSplit[0])
        if '/logout.php' in line:
            countLogout += 1

print("IP addresses: ", daftarIpArray)
print("Total login attempts: ", countLogin)
print("Total logout attempts: ", countLogout)
for ip, count in loginUrlPerIP.items():
    print("IP address {} has {} login attempts.".format(ip, count))

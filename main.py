def main(): 
    print("Gib deine FTP ein:")
    ftp = int(input())
    print("-----------------------------------")
    print("L1: Aktive Regeneration --> weniger als " + str(int(ftp * 0.55)))
    print("L2: Aerobe Ausdauer --> " + str(int(ftp * 0.56)) + " bis " + str(int(ftp * 0.75)))
    print("L3: Tempo --> " + str(int(ftp * 0.76)) + " bis " + str(int(ftp * 0.9)))
    print("L4: Laktatschwelle --> " + str(int(ftp * 0.91)) + " bis " + str(int(ftp * 1.05)))
    print("L5: VO2 MAX --> " + str(int(ftp * 1.06)) + " bis " + str(int(ftp * 1.2)))
    print("L6: Anerobe Kapazität --> " + str(int(ftp * 1.21)) + " bis " + str(int(ftp * 1.5)))
    print("L7: Neuromuskuläre Leistung --> über " + str(int(ftp * 1.5)))
    print("-----------------------------------")


if __name__ == "__main__":
    main()
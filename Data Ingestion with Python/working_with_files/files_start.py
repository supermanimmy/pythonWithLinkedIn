def main():
    #Open a file for writing and creating it if it doesn't exist.
    #f = open("textfile.txt", "w+")
    #open the file for appending text to the end
    f = open("textfile.txt", "r")


    #write some lines of date to the file
    # for i in range(10):
    #     f.write("This is line" + str(i)+ "\r\n")
    
    #Close the file when done
    #f.close()

    # Open the file back up and read contents
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)
        # contents = f.read() 
        # print(contents)


if __name__ == "__main__":
    main()
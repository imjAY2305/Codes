sam = open("D:\Codes\Python\Data\Email.txt","w")
sam.write("jagu.jdr121@gmail.com\n")
sam.write("imjay2305@gmail.com")
sam.close()
sam = open("D:\Codes\Python\Data\Email.txt","r")
arr = list(sam.readlines())
if("jagu.jdr121@gmail.com"+"\n" in arr):
    print(True)
sam.close()
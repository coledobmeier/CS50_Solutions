file = input("File name: ")

if file.__contains__(".gif"):
    print("image/gif")

elif file.__contains__(".jpg") or file.__contains__(".jpeg"):
    print("image/jpeg")

elif file.__contains__(".png"):
    print("image/png")

elif file.__contains__(".pdf") or file.__contains__(".PDF"):
    print("application/pdf")

elif file.__contains__(".txt"):
    print("text/plain")

elif file.__contains__(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")

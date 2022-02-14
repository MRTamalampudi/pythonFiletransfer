import requests
id="84"
url="https://rguktxp.s3.ap-south-1.amazonaws.com/webcam/"+id+"/" #n160864_52_selfie.jpg"

for i in range(160849,161300):
    a=requests.get(url+"n"+str(i)+"_"+id+"_selfie.jpg")
    b=a
    print(i)
    if b.status_code==200:
        output = open("C:/Users/Manikanta Reddy/Pictures/online exam/"+id+"/photos/"+str(i)+".jpg", "wb")
        output.write(a.content)
        output.close()
import siaskynet as skynet

skylink = skynet.Skynet.upload_file(
    "/Users/xingyue/outcode/git/skynetplay/images.jpg")
print("Upload successful, skylink: " + skylink)

bs = skynet.Skynet.download_file(
    "./download.jpg", "sia://HAEmn5u-0lJDc6qwNhrooJh2SQZSc-QYeKX2ZTVRsGYLZQ")

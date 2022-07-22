import requests

url = "https://random.dog/woof"

for i in range(10):
    # Download the random image name
    image_name = requests.get(url).text
    print("Downloaded random name", image_name)
    image_url = "https://random.dog/" + image_name
    print(image_url)

    # Download the actual image data
    image = requests.get(image_url).content

    # Create a file on the disk and save the image/video
    file = open("dogs/" + image_name, "wb")
    file.write(image)
    file.close()

    input()

    # Open the image/video automatically
    import os
    os.system("start " + "dogs/" + image_name)

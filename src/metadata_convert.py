

def file_process(filename):
    # creating a variable and storing the text
    # that we want to search
    search_text = "ADD_IMAGES_BASE_URI_HERE"
    search_text2 = "ADD_PROJECT_NAME_HERE"
      
    # creating a variable and storing the text
    # that we want to add
    replace_text = "https://gateway.pinata.cloud/ipfs/Qmab3MQwN6nwVjMsBYRvRXUcTNqnXvQfxqA6ynVrwT78A8/"
    replace_text2 = "NFT Image"
      
    with open(filename, 'r') as file:
        data = file.read()
      
        data = data.replace(search_text, replace_text)
        data = data.replace(search_text2, replace_text2)

    target_file = filename + ".json"
      
    with open(target_file, 'w') as file:
        file.write(data)
  
if __name__ == "__main__":

    folder = "../metadata/"

    for i in range(30):
        print("Processing File: " + str(i))

        file_process(folder + str(i))

    print("Process Done")

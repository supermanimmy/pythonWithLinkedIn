"""
Example file for retrieving data from the internet file

"""
import urllib.request

def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    # 200 if everything is ok, 404 if file not found
    print("result code: " + str(webUrl.getcode()))

    data = webUrl.read()
    print(data)


if __name__ == '__main__':
    main()
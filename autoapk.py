import mechanize
apkname = input("whats The app name: ")
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
browser.open("https://m.apkpure.com/ar/search?q="+apkname)

x=0
for link in browser.links():
        x = x+1
        if x == 37:
                search_link=("https://www.apkpure.com"+link.url)
                break

browser.open(search_link)
y=0
for downlink in browser.links():
        y = y + 1
        if y == 50:
                download="https://www.apkpure.com"+downlink.url
                print("")
                print(apkname + ">>")
                print("")
                print(download)
                print("")
                print("done!, Take a Copy and start your Download")

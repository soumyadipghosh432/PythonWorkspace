import webbrowser
 
a_website = "https://www.google.com"
b_website = "https://www.python.org"
 
# Open a web URL
# several functions are available for open
# open(), open_new(), open_new_tab()
# See : https://docs.python.org/3/library/webbrowser.html#webbrowser.register

# get list of available browsers
print(webbrowser._browsers)

webbrowser.get('google-chrome').open(a_website) # for linux need to mention the browser name
webbrowser.get('firefox').open(b_website) # for linux need to mention the browser name

print("Browser runs in parallel with this code. this will be executed even if the browser is open")

webbrowser.open("https://www.python.org/") # for windows if the default browser is set

#if browser is not available and need to register to run
chrome_path="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe" #path for windows system
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
webbrowser.get('chrome').open_new_tab(b_website)

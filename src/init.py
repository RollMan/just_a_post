import dropbox
import os

def Init():

    if os.path.exists("./key.txt"):
        f = open("key.txt", "r")
        r = f.readline()
        f.close()
        return dropbox.client.DropboxClient(r.strip("\n"))
    else:
        app_key = "xxxxxxxx"
        app_secret = "xxxxxxxxxxxxxxx"
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
        authorize_url = flow.start()

        print "1.Go to : " + authorize_url
        print "2.Authorize and get key."
        print "3.Paste it below."
        code = raw_input("Paste here : ").strip()
        access_token, user_id = flow.finish(code)
        
        f = open("key.txt", "w")
        f.write(access_token + "\n" + user_id + "\n")
        f.close

        return dropbox.client.DropboxClient(access_token)

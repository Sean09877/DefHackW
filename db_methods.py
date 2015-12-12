import sqlite3

#File for database methods (registering users, checking if users exist, etc.)

def checkUser(username, password):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT * FROM users;"
    for i in c.execute(q):
        print i
    q = "SELECT Username,Password FROM users;"
    for i in c.execute(q):
        if i[0] == username and i[1] == password:
            return True
    return False
    conn.commit()
    conn.close()

def countUsers():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT UserID FROM users;"
    numUsers = 0
    for i in c.execute(q):
        numUsers += 1
    conn.commit()
    conn.close()
    return numUsers
    
def addUser(username, password):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "INSERT INTO users VALUES('" + username + "','" + password + "'," + str(countUsers()) + ");"
    c.execute(q)
    conn.commit()
    conn.close()

def userExists(username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT Username FROM users;"
    ans = 0
    for i in c.execute(q):
        if i[0] == username:
            ans = True
    if ans != True:
        ans = False
    conn.commit()
    conn.close()
    return ans

def countPosts():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT BlogID FROM blogs;"
    numBlogs = 0
    for i in c.execute(q):
        numBlogs += 1
    conn.commit()
    conn.close()
    return numBlogs

def getUserID(username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT Username,UserID FROM users;"
    UserID = -1
    for i in c.execute(q):
        if i[0] == username:
            UserID = i[1]
    conn.commit()
    conn.close()
    return UserID

def getUsername(ID):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "SELECT * FROM users;"
    name = ""
    for i in c.execute(q):
        if i[2] == ID:
            name = i[0]
    conn.commit()
    conn.close()
    return name

def addPost(title, post, user):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "INSERT INTO blogs VALUES('" + title + "','" + post + "'," + str(countPosts()) + "," + str(getUserID(user)) + ");"
    c.execute(q)
    conn.commit()
    conn.close()

def editPost(content, BlogID):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    q = "UPDATE blogs SET Content='" + content + "' WHERE BlogID=" + BlogID + ";"
    c.execute(q)
    conn.commit()
    conn.close()

def editUserPost(content, BlogID, username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    UserID = getUserID(username)
    q = "SELECT BlogID,UserID FROM blogs;"
    counter1 = -1
    counter2 = -1
    for i in c.execute(q):
        counter2 += 1
        if i[1] == UserID:
            counter1 += 1
            if counter1 == int(BlogID):
                conn.commit()
                conn.close()
                editPost(content, str(counter2))
                break

def getPosts():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    blogList = [] #A list of lists (smaller lists have title and content of one blog post)
    q = "SELECT Title,Content,UserID FROM blogs;"
    for i in c.execute(q):
        username = getUsername(i[2])
        blog = [i[0], i[1], username] #A list with the title and content
        blogList.append(blog)
    conn.commit()
    conn.close()
    return blogList

def getUserPosts(username):
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    blogList = []
    q = "SELECT Title,Content,UserID FROM blogs;"
    for i in c.execute(q):
        dbUsername = getUsername(i[2])
        if username == dbUsername:
            blog = [i[0], i[1]]
            blogList.append(blog)
    conn.commit()
    conn.close()
    return blogList

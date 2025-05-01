from flask import Flask, request, redirect, url_for, abort 
 
app = Flask(__name__) 
 
users = { 
    "admin": "supersecretkjkjkjkjjuqiqu*854q", 
    "guest": "guest" 
} 
 
@app.route('/') 
def index(): 
    return "Welcome guest to the site ! Try /login/admin" 
 
@app.route('/login/<username>') 
def login(username): 
    if username not in users: 
        abort(404) 
 
    host = request.headers.get("Host", "") 
    if username == "admin" and "localhost" in host: 
        return f"Welcome, {username}! Flag: CyberCode{{h05t_h34d3r_4tt4ck_c4n_h31p_s0m3t1m3}}" 
    elif username == "admin": 
        return "Access denied." 
 
    return f"Welcome, {username}!" 
 
@app.route('/admin') 
def admin_panel(): 
    return redirect(url_for('login', username='admin')) 
 
if name == '__main__': 
    app.run(host='0.0.0.0', port=5000)
from flask import Flask,jsonify,request
from mail_notes import send_notes_email
app = Flask(__name__)


@app.route('/submit/<email>/<notes>',methods=['POST','GET'])
def submit(email,notes):
        if request.method == "POST":
            result = send_notes_email(email,notes)
            if result == 'done':
              return jsonify({"key":"sent"})
            else:
              return jsonify({"key":"not sent"})
        else:
           print("only post not get")
         

if __name__ == "__main__":
      app.run(debug=True)   
    
    

    
    
    
    
    
    
    
    
    
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    #@app.route('/check',methods=['POST','GET'])
#def check():
 #   test = ''.join(list(request.form["n1"]+request.form["n2"]+request.form["n3"]+request.form["n4"]+request.form["n5"]+request.form["n6"])) 
 #   otp = request.form['otp']
 #   user = request.form['user']
 #   if test == otp:
 #       return render_template('home.html',rel=user)
  #  return render_template("2_step.html",val="re-enter")
#if __name__ == "__main__":

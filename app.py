from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <head>
    <title> Flask app>\</title>
    </head>

<body>
<h1> Here is a interesting quote for you:</h1>

    <h3>"When you see a good move, look for a better one. - Mr.Robot"</h3>
    <img src="https://pmcdeadline2.files.wordpress.com/2019/08/mrrobot_s4_key_art_final_-1-e1566934598188.jpg?w=681&h=383&crop=1">
<div>
<button> Click here</button>

<style>h1 {
    color: pink;
  }
  button{
    border: 2px #34495e;
    background-color: skyblue;
  }

  
</style>

<script>
document.querySelector("button").addEventListener("click",function(){
    document.body.style.background = randColor();
  })
  function randColor(){
    return '#' + (function co(lor) { return( lor += [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
  [Math.floor(Math.random()*16)])
    && (lor.length == 6) ? lor: co(lor); })(''); 
  }
  </script>
</div>

    </body>
    
    
    """

if __name__ == "__main__":
    app.run()
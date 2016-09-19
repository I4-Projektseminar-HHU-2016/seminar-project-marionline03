<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="01.css" type="text/css"> 
    <title> Hello World! </title>
    <meta charset="utf-8"/>
    <script language="javascript" type="text/javascript" src="pet.js"></script>
</head>
<body>
    <header>
        <nav>
            %for element in menu:
                <a href='{{element[1]}}'>{{element[0]}}</a>
            %end
       </nav>
    </header>
    <div id='box'> 
        <div id='box2'>    
        %if len(msg) > 0:
            %for element in msg:
                <p>{{element}}</p>
            %end
        %end
        </div>
        <div id='box2'>
            <p id='question'>Question: <strong>{{question[1]}}</strong></p>
            <p id='language'>Question Language: {{question[4]}}</p>
            <form action='/learn' method='POST'>
                <input name='answer'/>
                <input type='submit' value='send'/>
            </form>
            <p id='info'> Please translate into {{question[5]}} (and include all given punctuation marks).</p>
        </div>
        <div id='box2'>
            <div id='pet_box'>
                <center>
                    <canvas id="nothing" width=200; height=200;></canvas>
                    <img src='{{body}}' id="body" style="position: absolute; left: 45%; top: -10; z-index: 0;"></img>
                    <img src='{{face}}' id="face" style="position: absolute; left: 45%; top: -10; z-index: 1;"></</img>
                    <img src='{{deco}}' id="deco" style="position: absolute; left: 45%; top: -10; z-index: 2;"></</img>
                </center>
            </div>
        </div>
    </div>
    <footer> {{footer}} </footer>
</body>
</html>

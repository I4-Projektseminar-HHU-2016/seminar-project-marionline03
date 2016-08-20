<!DOCTYPE html>
<html>
<head>
    <title> Workingtitle </title>
    <link rel="stylesheet" href="/01.css" type="text/css"> 
</head>
<body>
    <header>    
        <nav>
            %for element in menu:
                <a href='{{element[1]}}'> 
                    <img src='{{element[2]}}' alt='{{element[0]}}'>
                </a>
            %end
        </nav>
    </header>    
        <section id='box'>
            <p id="a"></p>
            <div id='box2'>
                <p>Please choose your learning mode</p>
                %for element in learning_mode:
                    <a id="box2" href={{element[0]}}>{{element[1]}}</a> <br> <br>
                %end    
            </div>
        <div id='badges_container'>
            <ul>
            %for badge in badges:
                <li>{{badge}}</li>
            %end
            </ul>    
        </div>
        </section>
    </header>
</body>
</html>

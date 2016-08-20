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
                <p> The question was: {{question}} </p>
                <p> You said: {{user_input}}</p>
                <p> You answer is {{result}}. </p>
                %if result == False:
                    <p>The right answer is: {{answer}} </p>
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

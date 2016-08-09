<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="/01.css" type="text/css"> 
    <title> Workingtitle </title>
</head>
<body>
    <header>    
        <nav>
            %for element in menu:
                <a href=' {{element[1]}} '> {{element[0]}} </a>
            %end
        </nav>
        <section id='box'>
            <h1>{{heading}}</h1>
            <div id='box2'>
                <figure><img src='dummy.png' alt="dummy logo of pet monster"> </figure>
                <p> {{content}}</p>
            </div>
        </div>

        </section>
    </header>
</body>
</html>

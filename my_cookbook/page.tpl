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
            <div id='box2'>
                <figure><img src={{pet_image}} alt="dummy logo of pet monster" width='300' height='300'> </figure>
                <p> {{content}}</p>
            </div>
            <div id='box2'>
                <p>Name: ALIEN</p>
                <p>Age: 0 Days</p>
                <p>Level: 0</p>
                <p>Exp: 0/100</p>
            </div>
        </div>

        </section>
    </header>
</body>
</html>

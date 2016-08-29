<!DOCTYPE html>
<html>
<head>
    <title> Workingtitle </title>
    <link rel="stylesheet" href="/01.css" type="text/css"> 
    <!-- use jquery -->
    <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="http://code.jquery.com/jquery-migrate-1.1.0.min.js"></script>
    
    <!-- Script for reloading page-->
    <!-- found at: 
        http://www.w3schools.com/jsref/met_win_setinterval.asp, 
        http://stackoverflow.com/questions/12038183/refresh-page-for-interval-using-js#12038226
        http://stackoverflow.com/questions/12399952/only-reload-a-part-of-a-web-page
    -->
    <script>
        <!-- jQuery('#pet_img').load('/pet_image');-->
        var myVar = setInterval(myTimer, {{interval}} );
        function myTimer() {
            location.reload();
        }
    </script>
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
                <figure><img id='pet_img' src={{pet_image}} alt="dummy logo of pet monster" width='300' height='300'> </figure>
            </div>
            <div id='box2'>
                <p>Name: ALIEN</p>
                <p>Age: 0 Days</p>
                <p>Status: {{pet_status}}<p>
                <p>Hungry in: {{pet_hunger}}</p>
                <p>Level: 0</p>
                <p>Exp: 0/100</p>
            </div>
        </div>
        <div id=test>
            <div>  
                <h2>Due Words:</h2>
                %for element in due_list:
                    <p>{{element.question}}</pp>
                %end      
            </div>
            <div>
                <h2>Words for later:</h2>
                %for element in wait_list:
                    <p>{{element.question}}</pp>
                %end
            </div>
            <form action="/feed_item" method="post">
                <input name="food" value="berry" type="submit">Berry</input>
                <input name="food" value="raspberry" type="submit">Raspberry</input>
            </form>
        </div>
        <div id='badges_container'>
            <ul>
            %for badge in badges:
                <li>{{badge.name}}: {{badge.player_progress_for_badge}}</li>
            %end
            </ul>    
        </div>
        </section>
    </header>
</body>
</html>

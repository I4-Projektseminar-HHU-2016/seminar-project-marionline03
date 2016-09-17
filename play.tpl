<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="01.css" type="text/css"> 
    <title> Hello World! </title>
    <script language="javascript" type="text/javascript" src="pet.js"></script>
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
    var myVar = setInterval(myTimer, 1000);
        function myTimer() {
            //var d = new Date();
            //document.getElementById("demo").innerHTML = d.toLocaleTimeString();
            //jQuery('#part').load('/update')
            $.getJSON('http://localhost:8080/update', function(data){
                console.log(data);
                // data.msg = data['msg'] in python
                //var image= "id='pet_img' src='" + data.image +"'";
                //console.log(image)
                document.getElementById('body').src= data.body;
                document.getElementById('face').src= data.face;
                document.getElementById('deco').src= data.deco;
            });
        }
       
    
    </script>
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
        <div id='pet_box'>
            <center>
                <canvas id="nothing" width=200; height=200;></canvas>
                <img id='body' src='{{body}}' id="body" style="position: absolute; left: 45%; top: -10; z-index: 0;"></img>
                <img id='face'src='{{face}}' id="face" style="position: absolute; left: 45%; top: -10; z-index: 1;"></</img>
                <img id='deco'src='{{deco}}' id="deco" style="position: absolute; left: 45%; top: -10; z-index: 2;"></</img>
            </center>
        </div>
    <div id='box2'>
        <h1>Inventory</h1>
                %if inventory_empty:
                    <p> Oh, noting to eat. No items here.</p>
                    <p> Please find the <a href="/shop">shopping page</a> to change credit points into items.</p>
                    <p> For gaining credit points you can <a href="/learn">pratice vocabulary</a>.</p>
                %end 
                % for element in inventory: 
                    %if element[4] > 0:
                    <p><form action='play' method='POST'>
                        <input type='hidden' name='id' value='{{element[0]}}'></input>
                        <img src='{{element[3]}}'alt='{{element[1]}}'</img>
                        <br><strong>{{element[4]}}</strong> x {{element[1]}}
                        <br>{{element[2]}}
                        <br><button type='submit'>give to pet</button>
                    </p>        </form>
                    %end
                %end
    </div>
    <footer> vocabulary pet game written in python </footer>
</body>
</html>

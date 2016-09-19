<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="01.css" type="text/css"> 
    <title>Wordlist</title>
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
    <div id='box'</div>
        <div id='box2'>
            <table>
                <tr>
                    <th>id</th>
                    <th>name</th>
                    <th>Life Points</th>
                    <th>State</th>
                </tr>
            
                <tr>
                    %for element in data:
                        <td>{{element}}</td>
                    %end
                </tr>
            </table>
            <div id='pet_box'>
                <center>
                    <canvas id="nothing" width=200; height=200;></canvas>
                    <img src='{{body}}' id="body" style="position: absolute; left: 55%; top: -10; z-index: 0;"></img>
                    <img src='{{face}}' id="face" style="position: absolute; left: 55%; top: -10; z-index: 1;"></</img>
                    <img src='{{deco}}' id="deco" style="position: absolute; left: 55%; top: -10; z-index: 2;"></</img>
                </center>
            </div>
        </div>
    </div>
    <!--<h2>Getting started</h2>
    <a href="create_account">Make an account and play!</a>
    <br>
    <a href="information">Learn more about the game!</a>-->
    <footer> {{footer}} </footer>
</body>
</html>

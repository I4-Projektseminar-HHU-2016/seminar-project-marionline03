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
    <div id='box'>
        <div id='box2'>
            <table>
                <tr>
                    <!-- Source: https://wiki.selfhtml.org/wiki/CSS/Eigenschaften/Textausrichtung/text-align-->
                    <th class='center'>id</th>
                    <th class='center'>name</th>
                    <th class='center'>credits</th>
                    <th class='center'>answered right <br> in sequence</th>
                </tr>
            
                <tr>
                    %for element in data:
                        <td class='center'>{{element}}</td>
                    %end
                </tr>
            </table>
        </div>
    </div>
    <footer> vocabulary pet game written in python </footer>
</body>
</html>

<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="01.css" type="text/css"> 
    <title>Shop</title>
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
    <div id='box_wordlist'>
        <div id='box2_wordlist'>
            <p><center>You have <strong>{{money}}</strong> credits.</center></p> 
            <table>
                <tr>
                    <th class='center'>name</th>
                    <th class='center'>price</th>
                    <th class='center'>decription</th>
                    <th class='center'>image</th>
                    <th class='center'>buy?</th>
                </tr>
            %for element in data:
                <tr> 
                    <form action='/shop' method='POST'>
                    <input type='hidden' name='id' value='{{element[0]}}'>
                    <td class='center'>{{element[1]}}</td> <!-- Name  -->
                    <td class='center'><strong>{{element[4]}}</strong></td> <!-- Price -->
                    <td class='center'>{{element[2]}}</td> <!-- Description-->
                    <td class='center'><img name='image' src='{{element[3]}}'></img></td> 
                    <td class='center'><button type='submit'>buy</button></td> 
                    </form> 
                </tr>
            %end
            </table>
        </div>
    </div>
    <footer> {{footer}} </footer>
</body>
</html>

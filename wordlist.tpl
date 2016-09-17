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
    <div id='box_wordlist'></div>
        <div id='box2_wordlist'>
            <table>
                <tr>
                    <th>id</th>
                    <th>question</th>
                    <th>answer</th>
                    <th>question language</th>
                    <th>target language</th>
                    <th>score</th>
                </tr>
            %for element in data:
                <tr> 
                    <form action='/wordlist' method='POST'>
                    <td>{{element[0]}}</td>
                    <input type='hidden' name='id' value='{{element[0]}}'>
                    <td><input name='question' value='{{element[1]}}'></input></td> 
                    <td><input name='answer' value='{{element[2]}}'></input></td> 
                    <td><input name='question_language' value='{{element[4]}}'></input></td> 
                    <td><input name='answer_language' value='{{element[5]}}'></input></td> 
                    <td>{{element[3]}}</td>
                    <td><button type='submit'>submit changes in row</button></td> 
                    </form> 
                </tr>
            %end
            </table>
        </div>
    </div>
    <!--<h2>Getting started</h2>
    <a href="create_account">Make an account and play!</a>
    <br>
    <a href="information">Learn more about the game!</a>-->
    <footer> vocabulary pet game written in python </footer>
</body>
</html>

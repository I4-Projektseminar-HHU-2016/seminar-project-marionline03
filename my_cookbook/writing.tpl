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
                <p id='question'>Question: {{voc.question}}</p>
                <p>Hint:     {{voc.hint}}</p>
                <p>Lesson:   {{voc.lesson}}</p>
                <p>Language  {{voc.language}}</p>
                <form action="/write" method="post">
                    Answer: <input name="answer" type="text" />
                    <input value="submit" type="submit" />
                </form>
            </div>
        <div id='box2'>
            <p>Due:   {{vocs_due}} of {{vocs_all}}</p>
            <p>Known: {{vocs_wait}} of {{vocs_all}}</p>
        <div>    
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

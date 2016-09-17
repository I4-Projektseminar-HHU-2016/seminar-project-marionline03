<html>
    <head>
        <link rel="stylesheet" href="/01.css" type="text/css"> 
        <!-- use jquery -->
        <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
        <script src="http://code.jquery.com/jquery-migrate-1.1.0.min.js"></script>
            <!-- Script for reloading page-->
    <!-- found at: 
        http://www.w3schools.com/jsref/met_win_setinterval.asp, 
        http://stackoverflow.com/questions/12038183/refresh-page-for-interval-using-js#12038226
        http://stackoverflow.com/questions/12399952/only-reload-a-part-of-a-web-page
        http://www.w3schools.com/js/js_htmldom_html.asp
        https://wiki.selfhtml.org/wiki/JavaScript/DOM/Element/innerHTML
        http://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_element_innerhtml2
        http://www.w3schools.com/jsref/prop_html_innerhtml.asp
    -->
        <script>       
        var myVar = setInterval(myTimer, 3500);
        function myTimer() {
            var d = new Date();
            document.getElementById("demo").innerHTML = d.toLocaleTimeString();
            //jQuery('#part').load('/update')
            $.getJSON('http://localhost:8080/update', function(data){
                console.log(data);
                // data.msg = data['msg'] in python
                //var image= "id='pet_img' src='" + data.image +"'";
                //console.log(image)
                document.getElementById('test').src= data.image;
            });
        }
       
        
        /*jQuery('#pet_img').load('/update') 
            var myVar = setInterval(myTimer, 7000);
            function myTimer() {
            location.reload('#test');
            }*/
        </script>
    </head>    
</html>
<body>
    <p id='demo'></p>
    <p id='part'></p>
    <img id='test'></img>
    
</body>

template = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
            crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
            crossorigin="anonymous"></script>
    </head>
    <body>
        <div id="parentDiv"><h1>Welcome to %s!</h1></div>
        <button type="button" class="btn btn-primary" onclick="clickButton()">Click</button>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"
        integrity="sha512-q/dWJ3kcmjBLU4Qc47E4A9kTB4m3wuTY7vkFJDTZKjTs8jhyGQnaUrxa0Ytd0ssMZhbNua9hE+E7Qv1j+DyZwA=="
        crossorigin="anonymous"></script>
        <script type="text/javascript" charset="utf-8">
            var socket = io();

            socket.on('connect', function() {
                socket.emit('join', {data: "I'm connected!"});
            });

            socket.on('my event response', function(response) {
                const parentDiv = document.getElementById("parentDiv");
                const newDiv = document.createElement("div");
                newDiv.textContent = response;
                newDiv.style.color = "#f54242";
                parentDiv.appendChild(newDiv);
            });

            function clickButton() {
                socket.emit('my event');
            }
        </script>
    </body>
</html>"""

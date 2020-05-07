index = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Class</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body>

<nav class="navbar navbar-inverse">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class=
            "navbar-brand" href="#">JavaDoc</a>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
                <li><a href="index.html">Home</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="container-fluid text-center">
    <div class="row content">
        <div class="col-sm-1 sidenav"></div>

        <div class="col-sm-10 text-left">
            <h1 align="center">Java documentation generator</h1>
            <p id="demo" align="center"></p>
            <p align="center">V 1.0</p>
            <hr>


            <h4 align="center"style="color: brown">Modules</h4>
            <table  class="table" style="font-size: 20px;">
                <thead class="thead-dark">
                <tr>
                    <th scope="col">Module</th>
                    <th scope="col">Description</th>
                </tr>
                </thead>
                <tbody>
                {modules}
                </tbody>
            </table>
        </div>
        <div class="col-sm-1 sidenav"></div>
    </div>
</div>

<script>
    var d = new Date();
    document.getElementById("demo").innerHTML = d.toDateString();
</script>
</body>
</html>
"""

modules = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Class</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body>

<nav class="navbar navbar-inverse">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">JavaDoc</a>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
                <li><a href="../index.html">Home</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="container-fluid text-center">
    <div class="row content">
        <div class="col-sm-1 sidenav"></div>

        <div class="col-sm-10 text-left">
            <h2 align="center">Module {module_name}</h2>
            <hr>

            <h4 align="center"style="color: brown">Packages</h4>
            <table class="table" style="font-size: 20px;">
             <thead class="thead-dark">
                </thead>
                <tbody>
                {packages}
                </tbody>
            </table>
        </div>
        <div class="col-sm-1 sidenav"></div>
    </div>
</div>
</body>
</html>
"""

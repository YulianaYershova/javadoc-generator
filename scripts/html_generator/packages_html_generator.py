def generate_html(package_path, package, inner_packages, classes, description):
    try:
        file = open(package_path + '/' + package + '.html', 'w+')
        file.write('<!DOCTYPE html>\n')
        file.write('<html lang="en">\n')
        file.write('<head>\n')
        file.write('    <meta charset="UTF-8">\n')
        file.write('    <title>Home</title>\n')
        file.write(
            '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<nav class="navbar navbar-inverse">\n')
        file.write('<div class="container-fluid">\n')
        file.write('<div class="navbar-header">\n')
        file.write('<a class="navbar-brand" href="#">JavaDoc</a>\n')
        file.write('</div>\n')
        file.write('<div class="collapse navbar-collapse" id="myNavbar">\n')
        file.write('<ul class="nav navbar-nav">\n')
        file.write('<li><a href="../../index.html">Home</a></li>\n')
        file.write('</ul>\n')
        file.write('<ul class="nav navbar-nav navbar-right">\n')
        file.write('</ul>\n')
        file.write('</div>\n')
        file.write('</div>\n')
        file.write('</nav>\n')
        file.write('<div class="container-fluid text-center">\n')
        file.write('<div class="row content">\n')
        file.write('<div class="col-sm-1 sidenav">\n')
        file.write('</div>\n')
        file.write('<div class="col-sm-10 text-left">\n')
        file.write('<h1 align="center"> Package ' + package + '</h1>\n')
        file.write('<hr>\n')
        if len(inner_packages) != 0:
            file.write('<h2 align="center"style="color: brown"> Packages </h2>\n')
            file.write('<table class="table" style="font-size: 20px;">\n')
            file.write('<thead class="thead-dark">\n')
            file.write('</thead>\n')
            file.write('<tbody>\n')
            for package in inner_packages:
                file.write('<tr>')
                file.write('<td><a href="' + package + '/' + package + '.html">' + package + '</a></td>')
                file.write('</tr>')
            file.write('</tbody>\n')
            file.write('</table>\n')
            file.write('<hr>\n')
        if len(classes) != 0:
            file.write('<h2 align="center"style="color: brown"> Classes </h2>\n')
            file.write('<table class="table" style="font-size: 20px;">\n')
            file.write('<thead class="thead-dark">\n')
            file.write('</thead>\n')
            file.write('<tbody>\n')
            for class_name in classes:
                file.write('<tr>')
                file.write('<td><a href="' + class_name + '.html">' + class_name + '</a></td>')
                file.write('</tr>')
            file.write('</tbody>\n')
        file.write('</table>\n')
        file.write('<hr>\n')

        file.write('</div>\n')
        file.write('</div>\n')
        file.write('</div>\n')
        file.write('</body>\n')
        file.write('</html>\n')
        file.close()
    except FileExistsError:
        print('HTML view for this object has already been created.')

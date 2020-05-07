def generate_html(class_path, **class_info):
    class_name = class_info.get('class_name')
    description = str(class_info.get('class_description'))
    imports = class_info.get('imports')
    annotations = class_info.get('annotations')
    constructors = class_info.get('constructors')
    variables = class_info.get('variables')
    methods = class_info.get('methods')
    inner_classes = class_info.get('inner_classes')

    description = description.replace('\n', '</br>')

    try:
        file = open(class_path, 'w+')
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
        file.write('<h1 align="center">' + class_name + '</h1>\n')
        file.write('<p>' + description + '</p>\n')
        file.write('<hr>\n')
        if len(imports) != 0:
            file.write('<h2> Imports </h2>\n')
            for i in imports:
                file.write('<a href="' + i["import_path"] + '">' + i["import"] + '</a> <br>\n')
            file.write('<hr>\n')

        if len(annotations) != 0:
            file.write('<h2> Annotations </h2>\n')
            for i in annotations:
                file.write('<p>' + i + '</p>\n')
            file.write('<hr>\n')

        if len(constructors) != 0:
            generate_table(file, constructors, 'constructor')

        if len(variables) != 0:
            generate_table(file, variables, 'variable')

        if len(methods) != 0:
            generate_table(file, methods, 'method')

        if len(inner_classes) != 0:
            generate_table(file, inner_classes, 'inner_class')

        file.write('</div>\n')
        file.write('</div>\n')
        file.write('</div>\n')
        file.write('</body>\n')
        file.write('</html>\n')
        file.close()
    except FileExistsError:
        print('HTML view for this object has already been created.')


# generate table for constructors, variables, methods, inner_class/inner_interface/inner_enum
def generate_table(file, arr, name):
    if len(arr) != 0:
        file.write('<h4 align="center" style="color: brown">' + name.capitalize() + 's' + '</h4>\n')
        file.write('<table class="table" style="font-size: 20px;">\n')
        file.write('<thead class="thead-dark">\n')
        file.write('<tr>\n<th scope="col">' + name.capitalize() + '</th>\n')
        file.write('<th scope="col">Description</th>\n<tr>\n')
        file.write('</thead>\n')
        file.write('<tbody>\n')
        for i in arr:
            file.write('<tr>')
            file.write('<td><p>' + i[name] + '</p></td>')
            file.write('<td><p>' + i["description"] + '</p></td>')
            file.write('</tr>')
        file.write('<tbody>\n')
        file.write('</table>\n')
    file.write('<hr>\n')

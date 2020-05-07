import os
from scripts.html_generator import packages_html_generator as package_generator
from scripts import classes_parser as parser, templates as templates


# recursive function for search nested packages
def get_classes(module, package):
    packages_list = []
    class_list = []
    packages = []
    classes = []
    package_path_in = input_dir + '/' + module + '/' + package + '/'
    package_path_out = output_dir + '/' + module + '/' + package + '/'
    module_description = ''
    # get class list
    for x in os.listdir(package_path_in):
        if os.path.isfile(package_path_in + x):
            classes.append(x)
            class_list.append(x)
        elif os.path.isdir(package_path_in + x):
            packages_list.append(x)

    if len(packages_list) != 0:
        # parse nested packages
        for x in packages_list:
            os.makedirs(package_path_out + x)
            packages.append(x)
            get_classes(module + '/' + package, x)

            # generate html pages for packages
            package_generator.generate_html(package_path_out, package, packages, classes, module_description)
            # parse all files in the package
            parser.parse_classes(package_path_in, package_path_out, classes)
        return
    else:
        # generate html pages for packages
        package_generator.generate_html(package_path_out, package, packages, classes, module_description)
        # parse all files in the package
        parser.parse_classes(package_path_in, package_path_out, classes)


# get package list and build html pages
def get_packages(module):
    packages_list = list(
        filter(lambda y: os.path.isdir(input_dir + '/' + module + '/' + y), os.listdir(input_dir + '/' + module)))
    packages_table = ''
    module_path = output_dir + '/' + module
    for x in packages_list:
        os.makedirs(module_path + '/' + x)
        packages_table += '<tr> <td> <a href="' + x + '/' + x + '.html">' + x + '</a> </td>\n </tr> \n'
    modules_info = {
        'module_name': module,
        'packages': packages_table
    }
    f = open(output_dir + '/' + module + "/" + module + '.html', 'w+')
    f.writelines(templates.modules.format(**modules_info))
    f.close()
    return packages_list


# get module list and build html pages
def get_modules(directory):
    modules_list = list(filter(lambda y: os.path.isdir(directory + '/' + y), os.listdir(directory)))
    modules_table = ''
    for x in modules_list:
        os.makedirs(output_dir + '/' + x)
        modules_table += '<tr> <td> <a href="' + x + '/' + x + '.html">' + x + '</a> </td>\n'
        try:
            description_file = open(directory + '/' + x + '/module-info.java')
            module_description = description_file.read()
            description_file.close()
            module_description = (module_description.split('/**'))[1].split('*/')[0]
            module_description = module_description.replace('*', '')
            modules_table += '<td>' + module_description + '</td>\n </tr> \n'
        except FileNotFoundError:
            modules_table += '<td>Module description is missed</td>\n </tr> \n'
    index_info = {
        'modules': modules_table
    }
    f = open(output_dir + '/index.html', 'w+')
    f.writelines(templates.index.format(**index_info))
    f.close()
    return modules_list


def build_directory_structure(input, output):
    global input_dir
    input_dir = input
    global output_dir
    output_dir = output

    os.makedirs(output_dir)
    module_list = get_modules(input_dir)
    for module in module_list:
        package_list = get_packages(module)
        for package in package_list:
            get_classes(module, package)

from scripts.html_generator import classes_html_generator as generator


def parse_classes(package_path_in, package_path_out, classes):
    global constructors
    global variables
    global methods
    global inner_classes

    class_modifiers = ['class', 'public class', 'final class', 'abstract class', 'public abstract class',
                       'public final class', 'abstract public class', 'final public class']
    interface_modifiers = ['interface', 'public interface', 'public abstract class']

    enum_modifiers = ['enum', 'public enum']

    for c in classes:
        constructors = []
        variables = []
        methods = []
        inner_classes = []
        imports = []
        annotations = []
        class_description = ''
        class_name = ''
        f_output = package_path_out + c + '.html'
        f_input = open(package_path_in + c, 'r')
        lines = f_input.readlines()
        f_input.close()
        in_class = False
        i = 0
        while i < len(lines):
            line = lines[i]
            line = line.lstrip()

            # parse class description, annotations
            if not in_class:
                # class description
                if line.startswith('/**\n'):
                    while not line.endswith('*/\n'):
                        line = lines[i]
                        class_description += line
                        i += 1
                    class_description = (class_description.split('/**'))[1].split('*/')[0]
                    class_description = class_description.replace(' *', '').rstrip()
                    continue

                # import list
                elif line.startswith('import'):
                    words = line.split(' ')
                    import_line = words[1].replace(';\n', '')
                    imports_dict = {'import': import_line}
                    import_path = import_line.replace('.*', '')
                    import_path = import_path.replace('.', '/').replace('/java', '.java')
                    p = import_path.split('/')
                    pack = p[len(p) - 1]
                    import_path = (('../../' + import_path) + '/' + pack + '.html\n')
                    imports_dict.update({'import_path': import_path})
                    imports.append(imports_dict)

                # annotations
                elif line.startswith('@'):
                    annotations.append(line)
                # class name
                elif any(line.startswith(x) for x in class_modifiers):
                    in_class = True
                    words = line.split()
                    key_words = ['public', 'private', 'protected', 'static', 'abstract', 'final',
                                 'native', 'synchronized', 'transient', 'volatile', 'strictfp', 'abstract', 'extends']
                    for w in words:
                        if any(w in key for key in key_words) or w == 'class':
                            continue
                        else:
                            class_name = 'Class ' + w
                            break
                # interface name
                elif any(line.startswith(x) for x in interface_modifiers):
                    in_class = True
                    words = line.split()
                    key_words = ['public', 'private', 'protected', 'static', 'abstract', 'final',
                                 'native', 'synchronized', 'transient', 'volatile', 'strictfp', 'abstract', 'extends']
                    for w in words:
                        if any(w in key for key in key_words) or w == 'interface':
                            continue
                        else:
                            class_name = 'Interface ' + w
                            break
                # enum name
                elif any(line.startswith(x) for x in enum_modifiers):
                    in_class = True
                    words = line.split()
                    key_words = ['public', 'private', 'protected', 'static', 'abstract', 'final',
                                 'native', 'synchronized', 'transient', 'volatile', 'strictfp', 'abstract', 'extends']
                    for w in words:
                        if any(w in key for key in key_words) or w == 'enum':
                            continue
                        else:
                            class_name = 'Enum ' + w
                            break

            # parse class constructors, methods, variables, inner_class/inner_interface/inner_enum
            elif line.startswith('/**'):

                description = ''

                if line.endswith('*/\n'):
                    description = line
                    i += 1

                while not line.endswith('*/\n'):
                    line = lines[i]
                    description += line
                    i += 1
                description = (description.split('/**'))[1].split('*/')[0]

                if line.startswith('/*'):
                    break

                code_scope = ''

                while i != len(lines) and not lines[i].lstrip().startswith('/*'):
                    line = lines[i].lstrip()
                    if not line.lstrip().startswith('@'):
                        code_scope += line
                    i += 1
                i -= 1
                code_scope = code_scope.replace('\n', '')
                description = description.replace(' *', '').lstrip()

                parse_class_element(code_scope, class_name, description)
                continue
            i += 1

        class_info = {
            'imports': imports,
            'class_description': class_description,
            'class_name': class_name,
            'annotations': annotations,
            'constructors': constructors,
            'variables': variables,
            'methods': methods,
            'inner_classes': inner_classes
        }

        generator.generate_html(f_output, **class_info)


# define class element (constructor ot methods or variable or inner_class/inner_interface/inner_enum)
def parse_class_element(code_scope, class_name, description):
    key_words = ['public', 'private', 'protected', 'static', 'abstract', 'final',
                 'native', 'synchronized', 'transient', 'volatile', 'strictfp', 'abstract', 'extends']
    words = code_scope.split(' ')

    if code_scope.find('{') >= 0 or code_scope.find('(') >= 0 \
            and code_scope.find(')') >= 0:
        declaration = ''
        for w in words:
            declaration += w
            if any(w in key for key in key_words):
                continue
            elif w.startswith(class_name + '('):
                a = code_scope.split('{')
                code_scope = a[0]
                global constructors
                constructor_dict = {'constructor': code_scope.replace('{\n', ''), 'description': description}
                constructors.append(constructor_dict)
                return
            elif w == 'class' or w == 'interface' or w == 'enum':
                a = code_scope.split('{')
                code_scope = a[0]
                global inner_classes
                inner_classes_dict = {'inner_class': code_scope.replace('{\n', ''), 'description': description}
                inner_classes.append(inner_classes_dict)
                return
            else:
                a = code_scope.split('{')
                code_scope = a[0]
                global methods
                methods_dict = {'method': code_scope.replace('{\n', ''), 'description': description}
                methods.append(methods_dict)
                return
    else:
        global variables
        variables_dict = {'variable': code_scope.replace(';', ''), 'description': description}
        variables.append(variables_dict)
        return

def createIndex(absolute_output_path):
    '''
    Creates an index.php on the root directory of the output folder
    Note: the index.php will be used as a common entry point
    @Param absolute_output_path: Path where the hole output is going to be written
    '''

    index = open(absolute_output_path + '/index.php', 'w')

    index.write('<?php\r\n')
    index.write('\r\n')
    index.write('define(\"DEFAULT_CONTROLLER\", \"Index\");\r\n')
    index.write('define(\"DEFAULT_ACTION\", \"index\");\r\n')
    index.write('\r\n')
    index.write('\r\n')
    index.write('function run(){\r\n')
    index.write('\ttry{\r\n')
    index.write('\t\tif(!isset($_GET[\"controller\"])){\r\n')
    index.write('\t\t\t$_GET[\"controller\"] = DEFAULT_CONTROLLER;\r\n')
    index.write('\t\t}\r\n')
    index.write('\t\tif(!isset($_GET[\"action\"])){\r\n')
    index.write('\t\t\t$_GET[\"action\"] = DEFAULT_ACTION;\r\n')
    index.write('\t\t}\r\n')
    index.write('\r\n')
    index.write('\t\t$controller = loadController($_GET[\"controller\"]);\r\n')
    index.write('\r\n')
    index.write('\t\tinclude (string)$controller;\r\n')
    index.write('\r\n')
    index.write('\t} catch(Exception $ex){\r\n')
    index.write('\t\tdie(\"An exception has occured: \" . $ex->getMessage());\r\n')
    index.write('\t}\r\n')
    index.write('}\r\n')
    index.write('\r\n')
    index.write('function loadController($controllerName){\r\n')
    index.write('\t$controllerClassName = __DIR__.\"/Controllers/\".$controllerName.\"_Controller.php\";\r\n')
    index.write('\treturn $controllerClassName;\r\n')
    index.write('}\r\n')
    index.write('\r\n')
    index.write('run();\r\n')
    index.write('?>\r\n')

    index.close()

from constants import *

def generateModel(entityName, attributesList, absolute_output_path):
    '''
    Model Generator
    @Param entityName: Name of the entity.
    @Param attributesList: List of all attributes of the entity.
    @Param absolute_output_path: Path where the hole output is going to be written
    '''

    entityName = entityName.lower()
    entityName = entityName.title()
    entityName = entityName.replace(" ", "_")

    model = open(absolute_output_path +'/Models/' + entityName + "_Model.php", 'w')

    model.write('<?php' + EOL)
    model.write(EOL)
    model.write('class ' + entityName + '_Model{' + EOL)
    model.write(EOL)
    for attribute in attributesList:
        model.write(ST + 'var $' + attribute +';' + EOL)
    model.write(ST + 'var $db;' + EOL)
    model.write(EOL)
    model.write(ST + 'function __construct(')
    for i in range(0,len(attributesList)):
        model.write('$' + attributesList[i])
        if i != (len(attributesList) - 1):
            model.write(',')
    model.write('){' + EOL)
    for attribute in attributesList:
        model.write(DT + '$this->' + attribute + ' = $' + attribute + ';' + EOL)
    model.write(DT + '//include_once __DIR__.\'/../Functions/FillWithDBConnection.php\';' + EOL)
    model.write(DT + '$this->db = \"something\";//Fill with connection method' + EOL)
    model.write(ST + '}' + EOL)
    model.write(EOL)
    model.write('}' + EOL)
    model.write(EOL)
    model.write('?>' + EOL)

    model.close()

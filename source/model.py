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

    model.write('<?php\r\n')
    model.write('\r\n')
    model.write('class ' + entityName + '_Model{\r\n')
    model.write('\r\n')
    for attribute in attributesList:
        model.write('\tvar $' + attribute +';\r\n')
    model.write('\tvar $db;\r\n')
    model.write('\r\n')
    model.write('\tfunction __construct(')
    for i in range(0,len(attributesList)):
        model.write('$' + attributesList[i])
        if i != (len(attributesList) - 1):
            model.write(',')
    model.write('){\r\n')
    for attribute in attributesList:
        model.write('\t\t$this->' + attribute + ' = $' + attribute + ';\r\n')
    model.write('\t\t//include_once __DIR__.\'/../Functions/FillWithDBConnection.php\';\r\n')
    model.write('\t\t$this->db = \"something\";//Fill with connection method\r\n')
    model.write('\t}\r\n')
    model.write('\r\n')
    model.write('}\r\n')
    model.write('\r\n')
    model.write('?>\r\n')

    model.close()

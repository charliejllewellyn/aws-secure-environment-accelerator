import os
import json
import yaml
import argparse

parser = argparse.ArgumentParser(description='Config Parser')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('--file', 
                    help='path to file', required=True)
requiredNamed.add_argument('--outputpath', 
                    help='path to output files', required=True)
args = parser.parse_args()

def loadFile():
    with open(args.file, 'r') as jsonFile:
        jsonObj = json.load(jsonFile)
    return jsonObj

def getTopLevelKeys(jsonObj):
    return jsonObj.items()

def determineType(jsonObj, parent=None, parentList=[], nestDict=None):
    print(parent, nestDict)
    if parent != None: 
        jsonObj=jsonObj[parent]
    if nestDict != None:
        jsonObj=jsonObj[0]
    root={}
    parentDict={}
    for key, v in getTopLevelKeys(jsonObj):
        if isinstance(v, dict):
            root['<a href=#' + key + '>' + key + '</a>']=key
            determineType(jsonObj, key, parentList + [key])
        elif isinstance(v, list):
            root['<a href=#' + key + '>' + key + '</a>']="List"
            if len(v) != 0:
                if isinstance(v[0], dict):
                    determineType(jsonObj, key, parentList + [key], v[0].keys()[0])
        elif isinstance(v, bool):
            root['<a href=#' + key + '>' + key + '</a>']="Boolean"
        else:
            root['<a href=#' + key + '>' + key + '</a>']="String"
    if parent == None:
        filename = args.outputpath + '/config.md'
        f = open(filename, "w")
        f.write("### JSON \n")
        f.write("<pre> \n")
        f.write(json.dumps(root, indent=4, sort_keys=True))
        f.write("</pre> \n")
        f.write("### YAML \n")
        f.write("<pre> \n")
        yaml.safe_dump(root, f, encoding='utf-8', allow_unicode=True, indent=4, default_flow_style=False)
        f.write("</pre> \n")
        f.close()
    else:
        filename = args.outputpath + "/" + "/".join(parentList) + ".md"
        print(filename)
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                pass
        f = open(filename, "w")
        parentDict[parent]=root
        jsonOut = json.dumps(parentDict, indent=4, sort_keys=True)
        f.write("### JSON \n")
        f.write("<pre> \n")
        f.write(jsonOut)
        f.write("</pre> \n")
        f.write("### YAML \n")
        f.write("<pre> \n")
        yaml.safe_dump(parentDict, f, encoding='utf-8', allow_unicode=True, indent=4, default_flow_style=False)
        f.write("</pre> \n")
        f.close()

def writeParams(jsonObj, parent=None, parentList=[], nestDict=None):
    if parent != None:
        jsonObj=jsonObj[parent]
    if nestDict != None:
        jsonObj=jsonObj[0]
    root=[]
    parentDict={}
    for key, v in getTopLevelKeys(jsonObj):
        if isinstance(v, dict):
            if parentList == []:
                filename1 = key + ".md"
            else:
                filename1 = "/".join(parentList) + "/" + key + ".md"
            root.append('<a name= "' + key + '" href="' + filename1 + '">`' + key + '`</a> \\' + '\nPlace holder text for what the parameter does \\' + '\n*Required*: Yes \\' + '\n*Type*: ' + key + ' \\' + '\n*Allowed Values*: Place holder for allowed values\n')
            writeParams(jsonObj, key, parentList + [key])
        elif isinstance(v, list):
            root.append('`' + key + '`  <a name="' + key + '"></a> \\' + '\nPlace holder text for what the parameter does \\' + '\n*Required*: Yes \\' + '\n*Type*: List \\' + '\n*Allowed Values*: Place holder for allowed values\n')
            if len(v) != 0:
                if isinstance(v[0], dict):
                    writeParams(jsonObj, key, parentList + [key], v[0].keys()[0])
        elif isinstance(v, bool):
            root.append('`' + key + '`  <a name="' + key + '"></a> \\' + '\nPlace holder text for what the parameter does \\' + '\n*Required*: Yes \\' + '\n*Type*: Boolean \\' + '\n*Allowed Values*: True | False\n')
        else:
            root.append('`' + key + '`  <a name="' + key + '"></a> \\' + '\nPlace holder text for what the parameter does \\' + '\n*Required*: Yes \\' + '\n*Type*: String \\' + '\n*Allowed Values*: Place holder for allowed values\n')
    if parent == None:
        filename = args.outputpath + '/config.md'
        f = open(filename, "a")
        f.write('\n' + '\n')
        for row in root:
            f.write(str(row) + '\n')
        f.write("%s\n" % root)
        f.close()
    else:
        filename = args.outputpath + "/" + "/".join(parentList) + ".md"
        print(filename)
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                pass
        f = open(filename, "a")
        f.write('\n' + '\n')
        for row in root:
            f.write(str(row) + '\n')
        f.close()
        
determineType(loadFile())
writeParams(loadFile())

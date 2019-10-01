#! usr/bin/python
# -*- coding: utf-8 *-*
import os
import argparse
import pkg_resources
import json
import yaml

def main():
    # initiate the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Required. Set name of project")
    parser.add_argument("-t", "--type", help="Required. Set type of project. Can be Technical (T), Use (U)", 
        choices=['T', 'U'])
    parser.add_argument("-d", "--dest", help="Required. Set destination of documentation. Can be API (A), Module (M), Custom (C)", 
        choices=['A', 'M', 'C'])

    # read arguments from the command line
    args = parser.parse_args()
    if args.name and args.type and args.dest:             
        createProject(args.name)
        if os.name == 'nt':
            createProjectFoldersWindows(args.name,args.type,args.dest)
        else:
            createProjectFoldersLinux(args.name,args.type,args.dest)        
    else:        
        cmd = 'python mkdocscreator.py -h'
        os.system(cmd)

def test():
    createProject("Prueba1")
    createProjectFoldersLinux("Prueba1","U","A")    

def createProject(name):
    cmd = 'mkdocs new %s' % name
    os.system(cmd)
    create_yaml_file(name)

def createProjectFoldersLinux(name,typeDoc,typeDest):
    try:
        file_path = os.popen('pwd').read()+'/'+ name +'/docs'
        file_path = file_path.replace('\n','')  
        Create_index_file_linux(name)
        folders_structure =  Load_type_documentation(typeDoc,typeDest)
        options = folders_structure.keys()
        for entry in options:
            cmd = 'mkdir ' + name +'/docs/' + entry
            os.system(cmd) 
            if '.md' in folders_structure[entry]:
                cmd = 'touch ' + name +'/docs/' + entry + '/' + folders_structure[entry]
                os.system(cmd) 
                file = open(name +'/docs/' + entry + '/' + folders_structure[entry],"w")  
                file.write("# Summary")    
                file.write("\n")
                file.write("\n")    
                file.write("Write documentation here")
                file.close()
            else:
                for index, line in enumerate(folders_structure[entry]):
                    cmd = 'mkdir ' + name +'/docs/' + entry + '/' + line
                    os.system(cmd) 
                    if '.md' in folders_structure[entry][line]:
                        cmd = 'touch ' + name +'/docs/' + entry + '/' + line + '/' + folders_structure[entry][line]
                        os.system(cmd)   
                        file = open(name +'/docs/' + entry + '/' + line + '/' + folders_structure[entry][line],"w")  
                        file.write("# Summary")    
                        file.write("\n")  
                        file.write("\n")  
                        file.write("Write documentation here")
                        file.close()                                             
    except Exception as ex:
        print ('\nError creating subfolders structure: %s' % str(ex))

def createProjectFoldersWindows(name,typeDoc,typeDest):    
    try:
        file_path = os.popen('echo %cd%').read()+'/'+ name +'/docs'
        file_path = file_path.replace('\n','')  
        Create_index_file(name)       
        folders_structure =  Load_type_documentation(typeDoc,typeDest)
        options = folders_structure.keys()
        for entry in options:
            cmd = 'md ' + name +'/docs/' + entry
            os.system(cmd) 
            if '.md' in folders_structure[entry]:
                cmd = 'NUL > ' + name +'/docs/' + entry + '/' + folders_structure[entry]
                os.system(cmd) 
                file = open(name +'/docs/' + entry + '/' + folders_structure[entry],"w")  
                file.write("# Summary")    
                file.write("\n")
                file.write("\n")    
                file.write("Write documentation here")
                file.close()
            else:
                for index, line in enumerate(folders_structure[entry]):
                    cmd = 'md ' + name +'/docs/' + entry + '/' + line
                    os.system(cmd) 
                    if '.md' in folders_structure[entry][line]:
                        cmd = 'NUL > ' + name +'/docs/' + entry + '/' + line + '/' + folders_structure[entry][line]
                        os.system(cmd)   
                        file = open(name +'/docs/' + entry + '/' + line + '/' + folders_structure[entry][line],"w")  
                        file.write("# Summary")    
                        file.write("\n")  
                        file.write("\n")  
                        file.write("Write documentation here")
                        file.close()                                            
    except Exception as ex:
        print ('\nError creating subfolders structure: %s' % str(ex))

def Create_index_file(name):
    cmd = 'del ' + name +'/docs/index.md'
    cmd = 'NUL > ' + name +'/docs/index.md'
    file = open(name +'/docs/index.md',"w")  
    file.write("# Summary")    
    file.write("\n")
    file.write("\n")    
    file.write("Write Summary here")
    file.close()
    os.system(cmd) 

def Create_index_file_linux(name):
    cmd = 'rm -f ' + name +'/docs/index.md'
    cmd = 'touch ' + name +'/docs/index.md'
    file = open(name +'/docs/index.md',"w")  
    file.write("# Summary")    
    file.write("\n")
    file.write("\n")    
    file.write("Write Summary here")
    file.close()
    os.system(cmd) 

def Load_type_documentation(docType,destType):
    configuration_file = 'configuration.json'
    if docType == 'T':
        docType = 'Technical'
    elif docType == 'U':
        docType = 'Use'

    if destType == 'A':
        destType = 'API'
    elif destType == 'C':
        destType = 'Custom'
    elif destType == 'M':
        destType = 'Module'

    with open(configuration_file) as file:
        filejson = json.load(file)
    folders_structure =  filejson[docType][destType]
    return folders_structure

def create_yaml_file(name):
    try:
        file_path = os.popen('pwd').read()+'/'+ name + '/mkdocs.yml'
        file_path = file_path.replace('\n','')
        mkdoc = {
            "site_name": "Documentation name",
            "site_description": "Documentation Description",
            "repo_url": "http://repourl.com",
            "site_author": "Creator Name",
            "theme":{
                "name": "material",
                "palette":{
                    "primary": "Orange",
                    "accent": "Orange"
                },   
                "font":{
                    "text": "Ubuntu",
                    "code": "Ubuntu Mono"
                },   
                "language": "es"
            }  
        }
        with open(file_path, "w") as f:
            yaml.safe_dump(mkdoc, f, default_flow_style=False)
    except Exception as ex:
        print ('\nError creating yaml file: %s' % str(ex))
    
if __name__ == '__main__':
    main()
    #test()
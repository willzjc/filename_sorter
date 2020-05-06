import os
import shutil

path='C:/local/download'

def main():
    for base,dirs,files in os.walk(path):
        if os.path.abspath(base) == os.path.abspath(path):
            for file in [ f for f in files if
                    not any( extension in f for extension in ['.crdownload','.pyc'] )
                ] :
                # print(file)
                destination_folder=file
                for delimiter in ['-','.','_x64','_x84']:
                    destination_folder=destination_folder.split(delimiter)[0].strip()

                for delimiter in ['_', ' ']:
                    if delimiter in destination_folder:
                        elements=destination_folder.split(delimiter)
                        base_element=elements[0]
                        for i,element in enumerate(elements):
                            if i > 0 and len(element) > 4:
                                base_element = base_element + '_' + element

                        destination_folder=base_element

                print("%s --> %s"%(file,destination_folder))

                destination_folder_path=os.path.join(base,destination_folder)
                if not os.path.isdir(destination_folder_path):
                    print("Creating path: %s"%destination_folder_path)
                    os.mkdir(destination_folder_path)

                destination_file_path=os.path.join(base,destination_folder,file)
                print("Moving file %s to : %s"%(file,destination_file_path))
                shutil.move(src=os.path.join(base,file),dst=destination_file_path)



if __name__ == '__main__':
    import sys
    print(sys.version)
    # a=['123','456','xxx']
    # b=['def','yyy','xx']
    # s='abcabcabc789abc'
    # print( any( (lambda x : x in s, a) ) )
    #
    # matches = [ x for x in a if any(w in x for w in b)]
    # print(matches)

    # from collections import OrderedDict
    # data ={1:2, 3:4, 5:0}
    # print(dict((k, v) for k, v in sorted(data.items(), key=lambda x : x[1])))
    # print([ y for y in ['a','b','c'] if (lambda x : x+y , '1') ])
    main()

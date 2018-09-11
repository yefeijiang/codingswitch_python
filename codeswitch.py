import sys
import os
import chardet
import codecs  
#---------------------------------------------------------
'''
title:     UltraReplace_python
version:   v1.0
author:    yefeijiang
email:     fjye@qq.com
python:    2.7.3
'''
#---------------------------------------------------------
def codeswitchfile(filename,tocode):
    
    fp=open(filename,'r');  
    alllines=fp.read();  
    fp.close();                
    coding = chardet.detect(alllines)['encoding'];
    if coding==None:
        return;    
    #print coding;
    print ("fromcode:"+coding.ljust(10)+" tocode:"+tocode.ljust(10)+filename);
                
    fp=codecs.open(filename,'r',coding);
    alllines = fp.read();
    #print alllines;
    fp.close(); 
 
    fp=codecs.open(filename,'w',tocode);
    fp.writelines(alllines);  
    fp.close();
    if tocode.upper()=="UTF-8":
        fp=codecs.open(filename,'r',"utf-8-sig");
        alllines = fp.read();
        fp.close(); 
 
        fp=codecs.open(filename,'w',tocode);
        fp.writelines(alllines);  
        fp.close();       
#---------------------------------------------------------    
def allcodeswitch(path,ext,tocode):
    ext = ext.replace('*','');
    ext = ext.split(';');
    for root,dirs,files in os.walk(path):
        for fn in files:
            filename=root+'\\'+fn;
            filetype = (os.path.splitext(filename))[1];
            if filetype in ext:
                codeswitchfile(filename,tocode);
           
#---------------------------------------------------------
def main():
    # if len(sys.argv)<4:
        # print ("usage:python.exe codeswitch.py path ext tocode");
        # print ("example:python.exe codeswitch.py \"D:\\Python27\\test\" \"*.txt;*.ini\" \"utf-8\" ");
        # print ("tocode:GB2312|UTF-16BE|UTF-16LE|UTF-8|utf-8|utf-8-sig");
        # return;
    # if not os.path.exists(sys.argv[1]):
        # print ("path:"+sys.argv[1]+" is not exist");
        # return;
    # if sys.argv[3]=="":
        # print ("tocode is empty");
        # return;
    allcodeswitch('D:\\Python27\\test','*.txt;*.ini','utf-8-sig');
    #allcodeswitch(sys.argv[1],sys.argv[2],sys.argv[3]);

###############################################################################
if __name__=="__main__":
    main();


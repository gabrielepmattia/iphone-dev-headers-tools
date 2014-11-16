iPhoneHeadersTools
==================
*gabry3795*

This repo contains a series of tool for iPhone headers, made by me.

Tools included
--------------
1. **SearchAndReplaceImport** | If you have downloaded headers, you can notice that every file *.h has 
  #import "Something.h"
this can be very harmful. With my python script you have only to input the main directory of your files, for example
  D:\\include\\
where you have (for example)
  D:\include\PrivateFrameworks
  D:\include\SpringBoard
  D:\include\Frameworks
and my script will replace
  #import "Something.h"
with
  #import <CorrectFolder/Something.h>
searching *Something.h* in every subfolder

*Other tools soon..*

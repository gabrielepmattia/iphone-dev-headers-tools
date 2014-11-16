iPhoneHeadersTools
==================
*gabry3795*

This repo contains a series of tool for iPhone headers, made by me.

Tools included
--------------
1. **SearchAndReplaceImport**  If you have downloaded headers, you can notice that every file *.h has

  <code>#import "Something.h"</code>

  this can be very harmful. With my python script you have only to input the main directory of your files, for example

  <code>D:\\include\\</code>
  
  where you have (for example)

  <code>D:\include\PrivateFrameworks
  D:\include\SpringBoard
  D:\include\Frameworks</code>
  
  and my script will replace

  <code>#import "Something.h"</code>
  
  with

  <code>#import &lt;CorrectFolder/Something.h></code>
  
  searching *Something.h* in every subfolder

2. *Other tools soon..*
